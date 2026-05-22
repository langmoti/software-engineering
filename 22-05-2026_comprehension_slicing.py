###############################################################################
# Intro to Comprehension
#
# Comprehension ist eine Kurzform um eine Liste / Dictionary / ... zu erstellen. 
# Man nutzt dazu nur Dinge, welche ihr schon kennt. 
# Bei einer List Comprehension, welche eine Liste erstellt: List, For, If
# 
# Als Beispiel: Eine Liste mit drei Elementen ist gegeben
example = ['a', 'b', 'c']
# Ihr wollt daraus nun eine neue Liste formen ohne 'b' und dazu List Comprehension nutzen.
# Das wuerde dann so ausschauen:
result = [element for element in example if element != 'b']
# Lesen kann man es so: fuege das element der Liste hinzu fuer jedes element der Liste example, wenn das element nicht gleich 'b' ist.
# Vorne steht also, was in die Liste kommt (das erste Wort element)
# Dahinter dann was das element erzeugt (for element in example) i
# Am Schluss ist eine Kondition moeglich, wann das element hinzugefuegt werden soll. Dies ist optional.
# In Langform waere das:
result = []                # -> Die Liste, welche das Ergebnis beinhaltet
for element in example:    # -> der Erzeuger von Element als For Loop in der Mitte
  if element != 'b':       # -> die Kondition am Ende 
    result.append(element) # -> erstes Wort element 

# Angenommen ihr wollt noch eine Operation mit element machen. Bspw. zu jedem element aus example einen String hinzufuegen.
# Das macht man dann vorne beim ersten Wort element
result = [element+' ein Beispiel String' for element in example if element != 'b']
# In der Langform vorhin wuerde mans beim Append dazuschreiben:
#    result.append(element+' ein Beispiel String') # -> erstes Wort element 
# Hier kann man alles machen, was Python erlaubt. Also Strings hinzufuegen zu Strings, eine Zahl potenzieren, addieren, etc.
# Beispiel wenn element eine Zahl waere und mit 2 multipliziert sein soll in der neuen Liste:
# result = [element*2 for element in example]

# Es ist also nur eine andere Schreibweise eines for loops, womit ihr euch direkt eine Liste generieren lassen koennt.
# Das einzige, was ihr dabei bedenken solltet: macht das eher nur, wenn es nicht zu lange wird.
# Hier das Beispiel von einer vorherigen Aufgabe als List Comprehension anstelle der in der Aufgabe erstellten Funktion:
#result = list({tuple(sorted((strecke, element))) for strecke in strecken for element in strecken if strecke != element and strecke + element == ziel})
# Ihr sehr sicherlich, dass es keine Freude macht, diesen nested For Loop zu lesen und zu raetseln, was nun am Ende element denn ist und wieso tuple(sorted()) usw.
# Bei sowas verringert ihr die Code Lesbarkeit schnell, wenn ihr solche langen Comprehensions nutzt.

# Natuerlich kann man neben Listen auch Dictionaries und anderes erzeugen. Hier, da wohl neben List am meisten genutzt, die Erzeugung eines Dictionaries:
# Ziel: Die Zahl zu entfernen und nur Strings als Values im Dictionary zu haben (also key3 zu entfernen).
example = {'key1': 'value1', 'key2': 'value2', 'key3': 123}
# Man macht einen Loop ueber das Dictionary mit items(), wo man key, value zurueck kriegt.
# Und als if kann man dann isinstance(<variable>, <type>) nehmen. Das gibt True, wenn <variable> vom Typ <typ> ist, sonst False.
result = {key: value for key, value in example.items() if isinstance(value, str)}
# Man muss dabei natuerlich die richtigen Klammern {} nutzen und key:value hinschreiben, da ein Dictionary so aufgebaut ist. 
# Dabei ist nicht wichtig, ob ihr key:value oder test:test2 nutzt. Die Namen der Variablen sind nicht wichtig, der : ist es. 
# Andernfalls generiert ihr noch ein Set, was auch die Klammern {} nutzt.
###############################################################################

###############################################################################
# Einschub zip():
# Ihr koennt auch ein Dictionary mittels zip() ein Dictionary zweier Listen erstellen.
# Beispiel:
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
result = dict(zip(numbers, letters))
# zip alleine erstellt nur einen Generator fuer euch (spaeter mal ein Thema). 
# dict() wandelt euch diesen dann in ein Dictionary, was dann so ausschaut:
# result = {1: 'a', 2: 'b', 3: 'c'}
# Das hat nun keinen besonderen Vorteil, ausser evtl. kurz zu sein.
# Es ist nur ein Weg von vielen um Daten zu veraendern. Es hat keinen besonderen Vorteil oder aehnliches.
###############################################################################

###############################################################################
# Intro to Slicing
# Guter Overiew mit Details: https://bas.codes/posts/python-slicing
# Slicing erlaubt euch, Strings und Listen zuzuschneiden, wenn ihr nur einen Teil davon braucht.
# Syntax = [start:stop:steps]
# Das schreibt man direkt nach der Liste/dem String hin.
# Beispiel:
example = 'this is a string'
result = example[4:].strip()
# result ist nun 'is a string' (dank strip() ohne Leerzeichen vorher). 
# Also vom vierten Buchstaben als start gibt es bis zum Ende den String zurueck. Alles vor dem vierten Buchstaben wurde abgeschnitten.
# Und auch direkt sichtbar: step muss nicht angegeben werden. Default ist dann einfach alles.

result = example[2::2]
# Nun ist result 'i sasrn', da es ab dem zweiten Buchstaben (also 0 1 2 -> i) jeden zweiten Buchstaben (wozu auch die Leerzeichen zaehlen) ausgibt.
# Das liegt an der letzten 2 nach dem zweitem :. Es muessen hier 2 Mal :: sein, da ansonsten die zweite 2 als Ende angenommen wird und ihr dann von 2 bis 2 habt. 

# Das funktioniert auch bei Listen sehr gut:
example = ['this', 'is', 'a', 'list']
result = example[::-1]
# Hier ist result die Liste example aber umgedreht von hinten nach vorne.
# [start:stop:step] heisst hier ist -1 der step und da start stop leer sind, meint es die gesamte Liste example

# Eine Liste in einem Loop sollte nicht geaendert werden. Man kann aber die ganze Liste kopieren fuer den Loop:
# for element in example[:]: 
# [:] erstellt dann eine Kopie der Liste und man kann example selbst modifizieren, ohne einen Fehler zu riskieren. 
# Also selbst bei Modifikation von example with die Kopie, welche [:] erstellte, nicht veraendert und daher wird jedes element im Loop dran kommen.
# [:] erstellt also nicht nur einen Verweis auf das gleiche Listen Objekt im Python Speicher. 
# Es erstellt ein neues Python Liste Objekt, welches nicht mehr von Aenderungen von example abheangig ist.
###############################################################################
