###############################################################################
# finde_strecken_paar: Gibt eine Liste aus, wo die Summe jedes Elements eine Ziel Zahl ergeben
# Die Funktion erhaelt als Paramter die Ziel Zahl und eine Liste an Zielzahlen
# Falls kein Ergebnis: Gebe None zurueck
# Nutze ein Set in der Funktion

def finde_strecken_paar(strecken, ziel, anzahl=None):
  """
  Returns list of possible paths.
  Possible paths sum is equal to ziel.
  If no possible path exists, None is returned.
  Bonus: Returns a wished amount of results using optional anzahl parameter
  """
  # Ergebnis Liste 
  result = []

  # By forming a set, duplicates are removed.
  strecken = set(strecken)
  
  # Run loop for every element in set
  for _ in range(len(strecken)):
    # Get an element
    strecke = strecken.pop()
    # Iterate over rest
    for element in strecken:
      # Check if element + strecke are a possible combination
      if element + strecke == ziel:
        result.append((strecke, element))

      # Return if amount of examples is reached
      if anzahl and len(result) == anzahl: return result
  return result
###############################################################################

###############################################################################
# 01 Dictionaries Mini-Workshop
# Liste Kleidung und Dictionary mit Preisen dieser Kleidung
# Gib Summe aller Preise aus

def gesamtpreis(kleidungsstuecke: list[str] | None = None, preise: dict | None = None) -> float:
  """
  Returns float sum of all kleidungsstuecke if they possess corresponding price in preise.
  """
  # If no kleidungsstuecke or preise directly return 0.0
  if not kleidungsstuecke or not preise: return 0.0

  # Good habit: standardize the input -> set all strings to lower
  kleidungsstuecke = [kleidungsstueck.lower() for kleidungsstueck in kleidungsstuecke]
  preise = {k.lower(): v for k, v in preise.items()}

  # Sum up prices
  result = 0.0
  for kleidungsstueck in kleidungsstuecke:
    result += preise.get(kleidungsstueck, 0.0)
  return result
###############################################################################


if __name__ == '__main__':

  # Welche der Aufgaben ausgefuhert werden soll -> Setze es auf True
  strecken = False
  dictionaries01 = True

  if strecken:
    strecken = [400, 500, 300, 600, 150, 250]
    ziel = 650
    # Alle Ergebnise
    print(f"Alle Ergebnisse der Funktion finde_strecken_paar: {finde_strecken_paar(strecken, ziel)}")
    # Nur ein Ergebnis
    print() # Nur fuer Abstand 
    print(f"Ein Ergebnis der Funktion finde_strecken_paar: {finde_strecken_paar(strecken, ziel, 1)}")
    
    # Edge Cases immer bedenken, welches Verhalten gewuenscht ist:
    # Was, wenn strecken Element == ziel ist? Funktion oben wuerde das nicht inkludieren. 

    # Beispiel Einzeiler:
    # tuple(sorted(x,y)) sortiert x, y immer und verhindert, dass (x, y) und (y, x) vorkommen, da sortiert es immer gleich waere und ein Set {} dann es als Duplikat ignorieren wuerde.
    result = list({tuple(sorted((strecke, element))) for strecke in strecken for element in strecken if strecke != element and strecke + element == ziel})
    print() # Nur fuer Abstand 
    print(f"Alle Ergebnisse des Einzeilers: {result}")

  if dictionaries01:
    kleidungsstuecke = ['Wintermantel', 'Cordhose', 'Smoking']
    preise = {'Wintermantel': 12.3, 'Cordhose': 45.2, 'Smoking': 123.49}
    print(f"Gesamtpreis der Kleidungsstucke: {gesamtpreis(kleidungsstuecke, preise)}")

    # Beispiel Einzeiler:
    # Dieser ist aber Case sensitive!
    print() # Nur fuer Abstand 
    preis = sum(preise.get(kleidungsstueck, 0.0) for kleidungsstueck in kleidungsstuecke)
    print(f"Gesamtpreis der Kleidungsstucke als Einzeiler: {preis}")

# Hinweis:
# Man kann zwei Dictionaries miteinander vereinen indem man dict1 | dict2 schreibt.
# Dann ueberschreibt dict2 jene key: values welche auch in ditc1 vorkommen.
# Also dict1['x'] = 1 und dict2['x'] = 2 wird bei dict3 = dict1 | dict2 zu dict3['x'] = 2
# Werte, welche nur in einem der beiden Dicts vorkommen bleiben in dict3 erhalten.
# 
# Bspw. sinnvoll, wenn man Default Einstellungen hat und diese dann durch eine Konfigurationsdatei vom Nutzer auch setzen lassen will.
# Jene werte (dict2 dann), welche er gesetzt hat, werden ueberschrieben.
# Bei jenen, welche er nicht setzte sind weiterhin die Default Einstellungen aus dict1 gueltig/vorhanden. 
