###############################################################################
# Mini-Workshop For Schleifen
# Scheiben Sie eine Funktion print_all(items: list), die die Elemente der Liste items auf dem Bildschirm ausgibt.
# Pro Zeile ein Element.
# Was passiert, wenn man diese Funktion mit einem String als Argument aufruft? Beispiel: print_all("abc")
#
# Einkaufsliste
# Variablen: meine_einkaufsliste: Liste mit Strings Tee und Kaffee
#            eine_andere_einkaufsliste: Liste mit Strings Tee und Kaffee
# Erstelle die Funktion drucke_einkaufsliste(einkaufsliste), welche die Elemente der Liste ausgibt.
# Definiere Funktion kaufe(produkt, einkaufsliste), die produkt hinzufuegt.
# Fuege Butter und Brot zu meine_einkaufsliste hinzu.
# Gib beide Listen nochmals aus.
# Fuege nochmals Butter und Brot zu meine_einkaufsliste hinzu. Was passiert?

# Erster Teil: Ausgabe for-loop des Strings 'abc'
def print_all(eine_liste):
  """
  Gibt Eintraege der eine_liste aus. Pro Zeile ein Eintrag.
  """
  for item in eine_liste:
    print(f"Eintrag der Liste: {item}")
  return

# Einkaufsliste
def drucke_einkaufsliste(einkaufsliste):
  """
  Gibt Eintraege der einkaufsliste aus. Pro Zeile ein Eintrag.
  """
  for item in einkaufsliste:
    print(f"Kaufe: {item}")
  return

def kaufe(produkt, einkaufsliste):
  """
  Fuegt der einkaufsliste das produkt hinzu und gibt neue Liste zurueck.
  """
  return einkaufsliste + [produkt]

###############################################################################

if __name__ == '__main__':

#  print_all('abc')

  meine_einkaufsliste = ['Tee', 'Kaffee']
  eine_andere_einkaufsliste = ['Tee', 'Kaffee']

#  drucke_einkaufsliste(meine_einkaufsliste)
#  meine_einkaufsliste = kaufe('Butter', meine_einkaufsliste)
#  meine_einkaufsliste = kaufe('Brot', meine_einkaufsliste)
#  drucke_einkaufsliste(meine_einkaufsliste)
#  drucke_einkaufsliste(eine_andere__einkaufsliste)
