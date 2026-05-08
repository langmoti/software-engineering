###############################################################################
# Range Einfuehrung
# Range gibt eine Liste von inklusive Start bis exklusive Ende aus.
# Die Syntax dafuer ist: range(start, ende, schritte)
#
# Beispiel: Eine Range, welche von 0-10 zaehlt in Einser-Schritten:
beispiel = range(0,11,1)
# 11 da das Ende nicht inkludiert wird. Damit 10 inkludiert ist, muss 11 genommen werden.
#
# Ausgabe der Range als Liste:
print(list(beispiel))
# Es kann wie bei einer Liste aber auch nur ein Element ausgegeben werden:
print(beispiel[2])
# Das gibt das dritte Element der Range aus (hier 0 1 2 -> es gibt eine 2 aus)
#
# Eine Range kann auch rueckwaerts zaehlen, also von hoch zu niedrig:
rueckwaerts = range(11,0,-1)
print(list(rueckwaerts))
#
# Die Schritte koennen natuerlich auch andere Werte als 1 oder -1 haben. 
# Um nur gerade Zahlen zu erhalten, kann man zB. es so machen:
gerade = range(2,11,2)
print(list(gerade))
# Es wird mit 2 gestartet und dann immer 2 addiert, bis 10 als hoechsten moeglichen Wert.
#
# Hinweis: Wenn man nur einen Wert an range gibt, dann wird automatisch zu diesem Wert in Einer-Schritten gezaehlt:
defaults = range(11)
print(list(defaults))
###############################################################################

###############################################################################
# Print info: 
# Print gibt am Ende automatisch immer ein \n dazu, was eine neue Zeile nach der Ausgabe einfuegt.
# Man kann das mit dem 'end' im Print Aufruf steuern:           
print('This print makes 2 newlines at the end:', end='\n\n')
#
# Der Default ist also print('...', end='\n'). 
# Man kann hier aber auch nur end='' oder end='abc' und vieles mehr machen.
###############################################################################

if __name__ == '__main__':
  print(f"Das Program fuehrt dazu, dass Beispiele der Range ausgegeben wurden.\nIn der Datei erklaeren Kommentare kurz, was wir heut angeschaut haben.")
