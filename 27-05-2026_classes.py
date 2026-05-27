###############################################################################
# Klassen Teil 2 und Methoden Mini Workshop
#
# Definiere Klasse KFZ mit Attributen hersteller und kennzeichen.
# Ergeuze zwei Fahrzeuge: 
#     Variable bmw mit BMW mit Kennzeichen M-BW 123
#     Variable vw mit VW mit Kennzeichen WOB-VW 246
#     Variable bmw2 mit BMW mit Kennzeichen M-BW 123
# Vergleiche ob bmw2 gleich bmw ist.
# Methode melde_um, welche Kennzeichen auf Argument neues_kennzeichen veraendert.
# Melde VW auf neues Kennzeichen BGL-A 9 um und pruefe Erfolg
# Melde bmw auf F-B21 um und pruefe ob bmw2 sich aendert

class KFZ:
  
  def __init__(self, hersteller, kennzeichen):
    self.hersteller = hersteller
    self.kennzeichen = kennzeichen

  def __str__(self):
    return f"Car with number plate {self.kennzeichen} is made by {self.hersteller}."

  # Methode melde_um, welche Kennzeichen auf Argument neues_kennzeichen veraendert.
  def melde_um(self, neues_kennzeichen):
    self.kennzeichen = neues_kennzeichen
    return 

def klassen_workshop():
  bmw = KFZ('BMW', 'M-BW 123')
  vw = KFZ('VW', 'WOB-VW 246')

  bmw2 = KFZ('BMW', 'M-BW 123')

  # Vergleiche ob bmw2 gleich bmw ist.
  if str(bmw2) == str(bmw):
    print("bmw and bmw2 are identical.")

  print()

  # Melde VW auf neues Kennzeichen BGL-A 9 um und pruefe Erfolg
  vw.melde_um('BGL-A 9')
  if vw.kennzeichen == 'BGL-A 9':
    print('Change of number plate of VW succeeded.')
    print(vw)

  print()

  # Melde bmw auf F-B21 um und pruefe ob bmw2 sich aendert
  bmw.melde_um('F-B21')
  if str(bmw2) != str(bmw):
    print('Change of number plate of bmw without interacting with bmw2 succeeded.')
    print(f"bmw -> {str(bmw)}")
    print(f"bmw2 -> {str(bmw2)}")
  return

###############################################################################

if __name__ == '__main__':
  
  # Klassen Teil 2 Mini Workshop
  klassen_workshop()
