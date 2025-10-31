# Kalkulačka v Pythonu (wxPython)

Jednoduchá grafická kalkulačka vytvořená v **Pythonu** s využitím knihovny **wxPython**.  
Podporuje běžné matematické operace, funkce `sin`, `cos`, `tan`, `log`, `ln`, přepínání mezi **stupni** a **radiány**, a ukládá **historii výpočtů**.

---

## Funkce

✅ Základní operace: `+`, `-`, `*`, `/`, `%`  
✅ Mocniny (`x²`), logaritmy (`log`, `ln`), goniometrické funkce (`sin`, `cos`, `tan`)  
✅ Přepínání režimu **deg / rad**  
✅ Automatické doplňování závorek  
✅ Historie posledních výpočtů  
✅ Rozhraní v **wxPython**

## Instalace

1. Ujisti se, že máš nainstalovaný **Python 3.10+**  
   Ověříš to v terminálu (cmd/powershell):

   python --version
   
2. Nainstaluj potřebnou knihovnu wxPython:

   pip install wxPython

## Spuštění
V příkazové řádce spusť:

   python kalkulacka.py

Otevře se okno s grafickým rozhraním kalkulačky.

## Tipy k používání

Kliknutím na deg/rad přepínáš mezi stupni a radiány.

deg → funkce jako sin(90) = 1

rad → funkce jako sin(π/2) = 1

Tlačítko H zobrazí / skryje historii.

Po kliknutí na = se výsledek zobrazí v poli — při dalším psaní se původní příklad smaže.

## Příklady pro testování
Výraz	Očekávaný výsledek (v režimu deg)
2 + 2 =	4
5 * (3 + 2) =	25
sin(90) =	1
cos(0) =	1
tan(45) =	1
ln(2.71828)	≈ 1
log(1000) =	3
π * 2	≈ 6.28318
10 % =	0.1
3^2 nebo 3 x² =	9
