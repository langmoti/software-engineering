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

if __name__ == '__main__':

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
