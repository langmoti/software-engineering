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

# Hinweis: Kaufe prueft hier auch, ob genug Geld vorhanden ist. 
#          Nur wenn noch genug Geld vorhanden ist, fuegt es das Produkt zur Einkaufsliste hinzu.

# Erster Teil: Ausgabe for-loop des Strings 'abc'
def print_all(eine_liste):
  """
  Gibt Eintraege der eine_liste aus. Pro Zeile ein Eintrag.
  """
  for item in eine_liste:
    print(f"Eintrag der Liste: {index} {item}")
  return

# Einkaufsliste
def drucke_einkaufsliste(einkaufsliste):
  """
  Gibt Eintraege der einkaufsliste aus. Pro Zeile ein Eintrag.
  """
  for item in einkaufsliste:
    print(f"Kaufe: {item}")
  return

def kaufe(produkt, einkaufsliste, geld):
  """
  Fuegt der einkaufsliste das produkt hinzu und gibt neue Liste zurueck.
  """
  einkaufsliste2 = einkaufsliste
  if produkt == 'Butter' and geld >= 60: 
    geld = geld - 60
    einkaufsliste2 = einkaufsliste + [produkt] 
  if produkt == 'Brot' and geld >= 60: 
    geld = geld - 60
    einkaufsliste2 = einkaufsliste + [produkt] 
  return einkaufsliste2, geld

###############################################################################

if __name__ == '__main__':

  #print_all('abc')

  meine_einkaufsliste = ['Tee', 'Kaffee']
  eine_andere_einkaufsliste = ['Tee', 'Kaffee']
  geld = 130

  #drucke_einkaufsliste(meine_einkaufsliste)
  #meine_einkaufsliste, geld = kaufe('Butter', meine_einkaufsliste, geld)
  #meine_einkaufsliste, geld = kaufe('Brot', meine_einkaufsliste, geld)

  # Oder in kurz um direkt das Produkt hinzuzufuegen 
  #meine_einkaufsliste.append('Butter')
  #meine_einkaufsliste.append('Brot')

  #drucke_einkaufsliste(meine_einkaufsliste)
  #drucke_einkaufsliste(eine_andere_einkaufsliste)

# Es gibt auch Steuerungsmoeglichkeiten fuer einen Loop:
# continue: gehe direkt zum naechsten Element und ueberspringe den restlichen Loop
# break: beende die Loop Ausfuehrung fuer alle Elemente und mache mit anderem Code weiter
# enumerate:
#    for index, item in enumerate(['a', 'b', 'c']):
#  Das enumerate zaehlt euch automatisch hoch. So koennt ihr sagen: Dieser Loop soll nur dreimal laufen: if index >= 3: break
#  Er zaehlt von 0 los, index == 3 ist also die vierte Iteration. Und es ist wichtig, 2 Variablen zu nutzen, also hier index und item.
#  for item in enumerate(...) wird einen Fehler verursachen. Die erste Variable ist der Zaehler von enumerate und die zweite das Element der Liste.
