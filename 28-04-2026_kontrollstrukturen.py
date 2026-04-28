###############################################################################
# Zahl Ratespiel
# 1. Rechner generiert eine Zahl zwischen 1 und 10
#
# 2. Der Spieler gibt eine Zahl zwischen 1 und 10 ein
#
# 3. Stimmt eingegebene mit generierter Zahl ueberein: gebe "Horaaaa! Deine Zahl {eingabe} ist richtig." aus
#
# 4. Stimmt eingegebene mit generierter Zahl nicht überein: gebe "Oh je! Leider ist deine eingegebene Zahl {eingabe} nicht korrekt. Die richtige Zahl waere {generated} gewesen." aus


# 1. Rechner generiert eine Zahl zwischen 1 und 10
def generate_number(bottom, top):
  """
  Generates a number between bottom and top limits. Limits are included as options.
  """
  import random
  return random.randint(bottom, top)

# 2. Der Spieler gibt eine Zahl zwischen 1 und 10 ein
def read_number(bottom, top):
  """
  Reads a number as input and checks if its within bottom and top limits. Limits are included as options.
  """
  while True:
    eingabe = input(f"Enter a number between {bottom} and {top}: ")
    print()
    try:
      number = int(eingabe)
      if bottom <= number <= top:
        return number
      else:
        print(f"The entered number {number} is not between {bottom} and {top}.")
    except ValueError:
      print(f"The entered value {eingabe} is not a number.")
    

# 3. Stimmt eingegebene mit generierter Zahl überein: gebe "Horaaaa! Deine Zahl {eingabe} ist richtig." aus
# 4. Stimmt eingegebene mit generierter Zahl nicht überein: gebe "Oh je! Leider ist deine eingegebene Zahl {eingabe} nicht korrekt. Die richtige Zahl waere {generated} gewesen." aus
def check_number(eingabe, generated):
  """
  Check if read number eingabe and generated number are equal or not.
  """
  if eingabe == generated:
    print(f"Horaaaa! Deine Zahl {eingabe} ist richtig.")
  elif eingabe != generated:
    print(f"Oh je! Leider ist deine eingegebene Zahl {eingabe} nicht korrekt. Die richtige Zahl waere {generated} gewesen.")
  else:
    print(f"Die eingegebene Zahl {eingabe} und generierte Zahl {generated} sind weder gleich noch ungleich...")
  return
###############################################################################


###############################################################################
# 04 Kontrollstrukturen (if)
# 1. Funktion ist_gerade(zahl), welche True zurueckgibt, wenn zahl gerade
#
# 2. Schreibe Funktion drucke_ist_gerade(zahl): Print "<zahl> ist gerade" falls ist_gerade(zahl) is True, else "<zahl> ist ungerade".

# 1. Funktion ist_gerade(zahl), welche True zurueckgibt, wenn zahl gerade
def ist_gerade(zahl):
  """
  Returns True if zahl is even, else false.
  """
  #if (int(zahl) % 2) == 0: 
  #  return True
  #else: 
  #  return False

  # Man kann es in kurz dann so schreiben:
  return True if (int(zahl) % 2) == 0 else False

# 2. Schreibe Funktion drucke_ist_gerade(zahl): Print "<zahl> ist gerade" falls ist_gerade(zahl) is True, else "<zahl> ist ungerade".
def drucke_ist_gerade(zahl):
  """
  Prints "<zahl> ist gerade" falls ist_gerade(zahl) is True, else "<zahl> ist ungerade"
  """
  if ist_gerade(zahl):
    print(f"{zahl} ist gerade")
  else:
    print(f"{zahl} ist ungerade")
  return
###############################################################################

###############################################################################
# 04 Kontrollstrukturen (if)
# 1. Funktion fits_in_line(text, line_length): True wenn len(text) <= line_length, else False
#
# 2. Funktion print_line(text, line_length): Print text if fits_in_line is True, else print('...')


# 1. Funktion fits_in_line(text, line_length): True wenn len(text) <= line_length, else False
def fits_in_line(text, line_length):
  """
  Returns True if len(text) <= line_lnegth else False
  """
  return True if len(text) <= line_length else False

# 2. Funktion print_line(text, line_length): Print text if fits_in_line is True, else print('...')
def print_line(text, line_length):
  """
  Prints line if fits_in_line is True else prints ...
  """
  if fits_in_line(text, line_length):
    print(text)
  else:
    print('...')
  return

###############################################################################


if __name__ == '__main__':

  #check_number(read_number(1, 10), generate_number(1, 10))
  
  # Obige Zeile ist eine Kurzform fuer diese einzelne Schritte:
  #eingabe = read_number(1, 10)
  #generierung = generate_number(1, 10)
  #check_number(eingabe, generierung)

  assert ist_gerade(0) is True, f"Expected True, but ist_gerade(0) returned {ist_gerade(0)}"
  assert ist_gerade(1) is False, f"Expected False, but ist_gerade(1) returned {ist_gerade(1)}"
  assert ist_gerade(8) is True, f"Expected True, but ist_gerade(8) returned {ist_gerade(8)}"
  
  # Ruft ersten Teil von 04 Kontrollstrukturen (if) auf
  #drucke_ist_gerade(8)

  # Ruft zweiten Teil von 04 Kontrollstrukturen (if) auf
  #print_line('Hallo', 5)

# Das angesprochene Beispiel wie man eine zufaellig langen String erhaelt:
#import random
#import string
#
# Define the pool of characters (letters and digits)
#characters = string.ascii_letters + string.digits
#
# Generate a random string of length 10
# random.choices returns a list, so we "".join() it
#random_string = ''.join(random.choices(characters, k=10))
#
#print(random_string)
