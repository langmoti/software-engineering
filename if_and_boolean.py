###############################################################################
# Vorgriff: Kontrollstrukturen if/elif/else
# Python, wie viele andere Sprachen, hat if/elif/else als Kontrollstrukturen.
# Das heisst, dass man die Ausfuehrung eines Code Blocks an eine oder mehrere Bedingungen knuepfen kann.
# Diese muessen als Resultat wahr ergeben, damit der nachfolgende Code Block ausgefuehrt wird.
# Andernfalls wird der Code Block nicht ausgefuehrt.

# Die Kontrollstruktur hat drei Begriffe:
# if -> Deutsch wuerde man Wenn sagen. Also "Wenn das wahr ist, fuehre den Code danach aus, sonst nicht"
# elif -> Einfach ein zweites If, wenn das erste nicht wahr war. 
# else -> Wenn kein if oder elif in der Kette wahr war, wird das ausgefuehrt.

# Hinweise: 
# 1. Das erste wahre If/elif wird ausgefuehrt und die anderen dann uebersprungen. 
#    Hat man if ...: und elif ....: und if ....: ist korrekt, wird elif gar nicht erst angeschaut.
# 2. Es koennen beliebig viele elif's nach dem ersten If noch kommen. 
# 3. Am Ende kommt maximal ein else, welches immer ausgefuehrt wird, wenn alle if/elif falsch waren. Ein Default sozusagen.
# 4. Code block jeweils unter if/elif/else einruecken. Die Einrueckung sagt aus, was zum Code Block gehoert.

# Beispiel fuer ein if:
#number = 2
#if number == 2:
#  print(f"Die Number {number} ist gleich 2.")
#print('Die If Anweisung ist zu Ende da dies nicht eingrueckt ist.')

# Beispiel fuer ein if mit else:
#number = 3
#if number == 2:
#  print(f"Die Number {number} ist gleich 2.")
#else: 
#  print(f"Die Number {number} ist nicht gleich 2.")

# Beispiel fuer ein if mit elif:
#number = 3
#if number == 2:
#  print(f"Die Number {number} ist gleich 2.")
#elif number == 3: 
#  print(f"Die Number {number} ist gleich 3.")

# Beispiel fuer ein if mit elif und else:
#number = 4
#if number == 2:
#  print(f"Die Number {number} ist gleich 2.")
#elif number == 3: 
#  print(f"Die Number {number} ist gleich 3.")
#else:
#  print(f"Die Number {number} ist weder gleich 2 noch gleich 3.")
###############################################################################

###############################################################################
# Vorgriff: Boolean
# Es gibt in Python natuerlich auch einen Namen fuer wahr und falsch. Solche Werte heissen Boolean.
# Boolean ist ein Typ der entweder wahr -> True oder falsch -> False sein kann. 

# Als Code waere das:
#boolean_var = False
#if boolean_var is True:
#  print(f"Boolean variable boolean_var ist wahr.")
#elif boolean_var is False:
#  print(f"Boolean variable boolean_var ist falsch.")

# Es gibt bei Python dabei auch das Truthy und Falsy.
# Das meint, dass ein Wert als True zaehlt, auch wenn er nicht explizit True ist.
# Dabei prueft man aber nicht mehr mit 'is True', da dies genau prueft.
# Das is prueft naemlich genau, ob die Variable von Typ Boolean und True ist.
# Daher schreibt man entweder 'if <variable>:' was bedeutet: Wenn <varibale> truthy, fuehre den Code aus. 
# Oder man kann auch explizit 'if <variable> == 'truthy Fall': schreiben. 
# Beispiel: Ein leerer String ist falsy, ein nicht leerer String truthy.
#           Ein leerer String ist aber kein Boolean, auch wenn er leer ist. 
#           Daher wird ein 'if <string> is True:' auch hier weiterhin in False/Falsch resultieren.
#boolean_string = ''
#if boolean_string:
#  print(f"Boolean variable boolean_string ist truthy.")
#else:
#  print(f"Boolean variable boolean_string ist falsy.")

# Das aehnliche gilt auch fuer Zahlen:
# 0 und 0.0 gelten hier als falsy
#boolean_number = 0
#if boolean_number:
#  print(f"Boolean variable boolean_number ist truthy.")
#else:
#  print(f"Boolean variable boolean_number ist falsy.")
###############################################################################
