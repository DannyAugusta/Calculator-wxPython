import wx
import math

class Kalkulacka(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Kalkulačka", size=(380, 520))
        self.SetBackgroundColour("white")
        self.historie = []
        self.vysledek_predchozi = ""
        self.rezim_radiany = True
        self.novy_vyraz = True
        self.vytvor_gui()
        self.Centre()
        self.Show()

    def vytvor_gui(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.vstup = wx.TextCtrl(panel, style=wx.TE_RIGHT)
        self.vstup.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        vbox.Add(self.vstup, 0, wx.EXPAND | wx.ALL, 8)

        grid = wx.GridSizer(6, 5, 5, 5)
        tlacitka = [
            "7", "8", "9", "/", "C",
            "4", "5", "6", "*", "⌫",
            "1", "2", "3", "-", "H",
            "0", ".", "=", "+", "π",
            "(", ")", "x²", "log", "ln",
            "sin", "cos", "tan", "deg/rad", "%"
        ]

        for label in tlacitka:
            btn = wx.Button(panel, label=label)
            btn.Bind(wx.EVT_BUTTON, self.stisk)
            grid.Add(btn, 1, wx.EXPAND)

        vbox.Add(grid, 1, wx.EXPAND | wx.ALL, 8)

        self.hist = wx.ListBox(panel)
        vbox.Add(self.hist, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 8)

        panel.SetSizer(vbox)

    def stisk(self, e):
        label = e.GetEventObject().GetLabel()

        # Po "=" začíná nový výraz
        if self.novy_vyraz and label not in ["=", "H", "C", "⌫", "deg/rad"]:
            self.vstup.SetValue("")
            self.novy_vyraz = False

        if label == "C":
            self.vstup.SetValue("")
        elif label == "⌫":
            self.vstup.SetValue(self.vstup.GetValue()[:-1])
        elif label == "=":
            self.vyhodnot()
            self.novy_vyraz = True
        elif label == "x²":
            self.vstup.SetValue(self.vstup.GetValue() + "**2")
        elif label == "π":
            self.vstup.SetValue(self.vstup.GetValue() + "π")
        elif label in ["sin", "cos", "tan", "log", "ln"]:
            self.vstup.SetValue(self.vstup.GetValue() + label + "(")
        elif label in ["deg/rad", "deg", "rad"]:
            self.rezim_radiany = not self.rezim_radiany
            e.GetEventObject().SetLabel("rad" if self.rezim_radiany else "deg")
        elif label == "H":
            self.zobraz_historii()
        else:
            text = self.vstup.GetValue()
            if label == "." and text.endswith("."):
                return
            self.vstup.SetValue(text + label)

    def vyhodnot(self):
        expr = self.vstup.GetValue()
        if not expr:
            return
        try:
            expr = expr.replace("^", "**")
            expr = expr.replace("log", "math.log10")
            expr = expr.replace("ln", "math.log")
            expr = expr.replace("%", "/100")
            expr = expr.replace("π", str(math.pi))

            # Automatické doplnění závorek
            otevrene = expr.count("(")
            zavrene = expr.count(")")
            if otevrene > zavrene:
                expr += ")" * (otevrene - zavrene)

            # Bezpečné prostředí pro eval
            fce = {"math": math, "__builtins__": None}

            # Trigonometrické funkce podle režimu
            if self.rezim_radiany:
                fce.update({
                    "sin": math.sin,
                    "cos": math.cos,
                    "tan": math.tan,
                })
            else:
                fce.update({
                    "sin": lambda x: math.sin(math.radians(x)),
                    "cos": lambda x: math.cos(math.radians(x)),
                    "tan": lambda x: math.tan(math.radians(x)),
                })

            vysl = eval(expr, fce, {})
            vysl = round(vysl, 10)

            self.historie.insert(0, f"{expr} = {vysl}")
            self.hist.Set(self.historie[:20])
            self.vstup.SetValue(str(vysl))
            self.vysledek_predchozi = str(vysl)
            self.novy_vyraz = True

        except ZeroDivisionError:
            wx.MessageBox("Dělení nulou není možné.", "Chyba")
        except Exception:
            wx.MessageBox("Chybný nebo neúplný výraz.", "Chyba")

    def zobraz_historii(self):
        if self.hist.IsShown():
            self.hist.Hide()
        else:
            self.hist.Show()
        self.Layout()


if __name__ == "__main__":
    app = wx.App(False)
    Kalkulacka()
    app.MainLoop()
