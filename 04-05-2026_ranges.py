###############################################################################
# Mini-Workshop Ranges
# Schreibe pring_squares(n), welche die Quadrate der Zahlen von 1 bis n ausgibt.
#
# Schreibe sum_squares(n), welche die Summe der ersten n Quadratzahlen zureuckgibt.

def print_squares(n):
  """
  Gibt die Quadrate von 1 bis n aus.
  """
  for number in range(1,n+1):
    print(f"Quadrat von {number} ist {number**2}.")
  return

# Note: oben ist range(1,n+1) und unten nur (n+1) -> inkludiert/startet dann von 0 nicht 1
#       Ansonsten wuerde es oben 0**2 auch ausgeben, was vermieden werden soll.
#       Unten ist aber nur die Summe gefragt und da 0**2 auch 0 ist, aendert es die Summe nicht.
#       Es kann also sowohl (1, n+1) gemacht werden als wie auch (n+1).

def sum_squares(n):
  """
  Gibt die Summe der Quadrate bis n zurueck.
  """
  # Lange Version:
  #summe = 0
  #for number in range(n+1):
  #  summe += number**2
  #return summe
  return sum(number**2 for number in range(n+1))

###############################################################################

###############################################################################
# Mini-Workshop String-Interpolation
# Schreibe Funktion drucke_begruessung(name), die eine personalisierte Begruessung ausgibt.

# Note: <string>.capitalize() -> Es schreibt den ersten Buchstaben gross und den Rest klein. 
#       Dann kann 'test' zu Test und 'teSTINg' zu Testing werden. 
def drucke_begruessung(name: str) -> None:
  """
  Gibt individualisierte Begruessung aus.
  """
  print(f"Hallo, {name.capitalize()}!", "Schoen Sie heute wieder bei uns begruessen zu duerfen.", f"Wir wuenschen Ihnen viel Spass, {name.capitalize()}.")
  return

# \n steht fuer newline und macht einen Zeilenumbruch

# Multiline ist auch moeglich:
#f"""\ -> \ zeigt an, dass das Kommando in der naechsten Zeile weitergeht, trailing white spaces aufpassen bei sowas
#zweite Zeile\
#dritte Zeile\
#""" -> Multiline String ist nun beendet

# Auch mehrere Strings koennen innerhalb einer Klammer ausgegeben werden. Sie Beispiel oben im druecke_begruessung print Statement.

# Trick zum Variablen testen, Annahme test = 10:
#print(f"{test = }") gibt dann automatisch 'test = 10' aus, gibt also Name und Wert aus. 
# Oder: print(f"{5 ** 3 = }") ergibt 5 ** 3 = 125

# Kann auch nested werden:
# f"{f"{f"{f"{f"{f"{1+1}"}"}"}"}"}" ergibt '2'

# Oder padding mit 0, Annahme x = 5
# Dann macht print(f"{x:02}") ein '05' daraus (zB. fuer Datumangabe

# Am Besten einfach Google suche fuer Tips und Tricks wie zB.
#https://www.reddit.com/r/learnpython/comments/1aqdwht/what_are_some_cool_fstring_tricks_that_youve/
# Es gibt da noch manche Beispiele oder eben auch Python Doku zu f Strings fuer formalere Version.
# Jedenfalls koennen f Strings noch viel mehr als das hier gezeigte. 

###############################################################################

###############################################################################
# Typannotationen
# Schreibe Funktion repeat(s: str, n: int) -> str, welche s n mal zurueck gibt
#
# `pip install pylance pylint` fuer die noetigen Python Pakete/Extensions in VSCode 
# 
# -> <type> fuer den Return Wert nach den () der Parameter.
# : <type> fuer die Parameter Typen
# Python selbst ignoriert diese Angaben. Dienen nur fuer den Entwickler als Hilfe.

def repeat(s: str, n: int) -> str:
  """
  Gibt String s n mal zurueck.
  """
  return s * int(n)

###############################################################################

###############################################################################
# Import von Modulen
# Schreibe Python Funktion, welche mittels Modul os die Funktion getcwd() aufruft.
# getcwd() gibt das Arbeitsverzeichnis aus.

def get_cwd() -> str:
  """
  Gibt das derzeitige Arbeitsverzeichnis aus.
  """
  # Note: Man kann/soll meist ganz am Anfang einer Datei die Import Statements schriebem.
  # Hier innerhalb der Funktion macht man es, wenn man os/getcwd nur in der Funktion verfuegbar machen will.
  from os import getcwd as arbeitsverzeichnis_ausgabe
  return arbeitsverzeichnis_ausgabe()

###############################################################################

if __name__ == '__main__':

# Mini-Workshop Ranges
  #print_squares(4)
  assert sum_squares(10) == 385
  #tester = 10
  #print(f"Fuer die Zahl {tester} betraegt die Summe aller Quadratzahlen {sum_squares(tester)}")

# Mini-Workshop String-Interpolation
  #drucke_begruessung('testINGg')

# Typannotationen
  #print(repeat('test', 3))
  # Da s * int(n) wird '3' zu 3 umgewandelt. Andernfalls erzeugt '3' einen Fehler.
  # Andere Strings wie 'a' statt '3' erzeugen aber auch weiterhin Fehler.
  #print(repeat('test', '3'))

  # Help ist auch in vim nutzbar
  #help(drucke_begruessung)

# Import von Modulen
  #print(get_cwd())
