import argparse

def question_1():
  """
  Question: Wandel 1.5 in einen String um.
  """
  value = 1.5
  print(f"Um den value 1.5 in einen String umzuwandeln kann man str() nutzen.")
  print(f"Gerade ist 1.5 ein {type(value)}.")
  print(f"Mit str(value) wird nun ein String daraus: {type(str(1.5))}.")
  return

def question_2():
  """
  Question: Bestimmte das Maximum der Werte 2.5 & 1.7.
  """
  print(f"Um das Maximum der Werte 2.5 und 1.7 zu bestimmen kann man max(wert1, ..., wertn) nutzen.")
  print(f"Mit max(2.5, 1.7) erhaehlt man also: {max(2.5, 1.7)}")
  return

def question_3():
  """
  Question: Wandel den String "1.234" in eine Zahl um und addiere 2.345.
  """
  value = "1.234"
  print(f"Um einen String in eine Zahl umzuwandeln kann man float() benutzen.")
  print(f"Das heisst für value {value} schreibt man float(value) und eraehlt: {float(value)}")
  print(f"Danach muss man nur noch mit 2.345 addieren, was nun einfach float(value) + 2.345 ist.")
  print(f"Die Addition ergibt dann: {float(value) + 2.345}")
  return

def bonus(value):
  """
  Bonus: Erstelle eine Funktion, welche nicht wie round() bei 0,5 zur naechsten geraden Zahl rundet.
         Also alles ab x,4 aufrundet und alles inkl. x,4 abrundet.
  """
  if int(value) % 2 == 0 and round(value) == int(value) and str(value).split('.')[1][:1] == "5": 
    print(f"Value {value} gerundet ist {round(value) + 1}.")
  else: 
    print(f"Value {value} gerundet ist {round(value)}.")
  return
  

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
                    prog='Project',
                    description='Contains the project.',
                    epilog='')
  parser.add_argument('-q', '--question', nargs=1, type=int, default=[0])    
  parser.add_argument('-v', '--value', type=float, default=2.5, required=False)    
  args = parser.parse_args()
  print()
  match args.question[0]:
    case 0:
      bonus(args.value)
    case 1:
      question_1()
    case 2:
      question_2()
    case 3:
      question_3()
    case _:
      print(f"There is no question {args.question[0]}.")
  print()
