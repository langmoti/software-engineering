###############################################################################
# Aufgabe, Anzahl und Location eines Elements in einer Matrix zu finden

def find_element(matrix, element):
  """
  Returns location of element in matrix.
  """
  results = []
  line_counter = 0
  for line in matrix:
    line_counter += 1
    entry_counter = 0
    for entry in line:
      entry_counter += 1
      if entry == element:
        results.append((line_counter, entry_counter))
        #results.append((line_counter, line.index(entry)))
  return results
###############################################################################

###############################################################################
def number_list(liste): 
  """
  Prints a numbered list using liste.
  """
  for number, entry in enumerate(liste):
    print(f"{number+1}. {str(entry).capitalize()}")
  return
###############################################################################

if __name__ == '__main__':

# Beispiel Matrix und gesuchtes Element
  matrix = [[1,4,3],[1,3,3],[1,2,3]]
  element = 3

# Funktion findet wo Element in Matrix ist
  results = find_element(matrix, element)

# Ort und Anzahl (len(results) Ausgabe
  print(f"\nDas Element {element} kommt {len(results)} Mal in der Matrix vor.\nGefunden an folgenden Stellen: {results}\n\nMatrix: {matrix} - Element: {element}\n")
###############################################################################

# Beispiel Teilnehmer
  teilnehmer = ['Uwe', 'Daniel', 'Noe', 'Matthias']

# Funktion gibt nummerierte Liste aus
 # print(); number_list(teilnehmer); print()
