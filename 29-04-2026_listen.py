###############################################################################
# Programmiert bitte 5 Funktionen
# Funktion 1: addiert zwei Zahlen und gibt das Ergebnis zurück
# Funktion 2: subrahiert eine Zahl von einer anderen und gibt das Ergebnis zurück
# Funktion 3: multipliziert zwei Zahlen 
# Funktion 4: dividiert eine Zahl durch eine andere 
# Funktion 5: Gibt den Rest von einer Division von Zahl 1 durch Zahl 2

# Funktion 1: addiert zwei Zahlen und gibt das Ergebnis zurück
def funktion_1(zahl1, zahl2):
  """
  Addiert zwei Zahlen und gibt das Ergebniss zurueck.
  """
  return zahl1 + zahl2

# Funktion 2: subrahiert eine Zahl von einer anderen und gibt das Ergebnis zurück
def funktion_2(zahl1, zahl2):
  """
  Subtrahiert zahl2 von zahl1 und gibt das Ergebnis zurueck.
  """
  return zahl1 - zahl2

# Funktion 3: multipliziert zwei Zahlen 
def funktion_3(zahl1, zahl2):
  """
  Multipliziert zwei Zahlen und gibt das Ergebnis zurueck.
  """
  return zahl1 * zahl2

# Funktion 4: dividiert eine Zahl durch eine andere 
def funktion_4(zahl1, zahl2):
  """
  Teilt zahl1 durch zahl2 und gibt Ergebnis zurueck.
  Edge Case: Division durch Null gibt None zurueck.
  """
  return zahl1 / zahl2 if zahl2 > 0 else None

# Funktion 5: Gibt den Rest von einer Division von Zahl 1 durch Zahl 2
def funktion_5(zahl1, zahl2):
  """
  Teilt zahl1 durch zahl2 und gibt den Rest als Ergebnis zurueck.
  Edge Case: Division durch Null gibt None zurueck.
  """
  return zahl1 % zahl2 if zahl2 > 0 else None
###############################################################################

###############################################################################
# 05 Listen Mini-Workshop
# Definieren Sie eine Variable grundfarben, die eine Liste mit den Strings "Rot", "Gruen" und "Blau" enthaelt
# Definieren Sie eine Variable mischfarben, die eine Liste mit den Strings "Cyan", "Gelb" und "Magenta" enthaelt
# Erzeugen Sie eine Liste farben, die die Elemente von grundfarben gefolgt von den Elementen von mischfarben enthaelt
# Erzeugen Sie die Liste ["r", "g", "b"] aus dem String "rgb"
def listen_workshop():
  """
  Listen_workshop bildet die obigen Aufgaben on 05 Listen ab.
  """
  grundfarben = ['Rot', 'Gruen', 'Blau']
  mischfarben = ['Cyan', 'Gelb', 'Magenta']
  farben = grundfarben + mischfarben
  rgb = list('rgb')
  print(f"Liste grundfarben: {grundfarben}\nListe mischfarben: {mischfarben}\nListe farben: {farben}\nListe rgb: {rgb}")
  return

###############################################################################


if __name__ == '__main__':

  #listen_workshop()

# Dinge die eine Liste kann
# Aufruf Beispiel: grundfarben.clear()
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
