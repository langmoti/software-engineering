#############################################################################
# Python Datenmodell
# Link zur Python Doku: https://docs.python.org/3/reference/datamodel.html
#
# Es geht ansonsten im Video vor allem um __eq__ und die __repr__ Thunder-Methoden.

# Beispielklasse
class Example:

  def __init__(self, x):
    self.x = x

  def __eq__(self, other):
    """
    Self ist die eigne Objekt, other das Objekt gegen man vergleicht.
    self -> example1 | other -> example2
    """
    if isinstance(other, Example):
      return self.x == other.x
    else:
      print('other is not of class Example -> can not do __eq__ with it!')
      return False

  def __repr__(self):
    """
    Sollte immer einen String zurueckgeben, welcher das Objekt erzeugen wuerde.
    Also den man kopieren koennte und dann var = <return von __repr__> machen koennte.
    """
    return f"Example(x={self.x})"

  def __str__(self):
    """
    Gibt eher etwas leserfreundliches fuer nicht Programmierer zurueck. 
    """
    return f"This is an object of class Example with the Attribute x equal to {self.x}."

def datenmodell():
  # Erzeuge 2 Objekte der Klasse Example mit dem gleichen Attribut
  example1 = Example(x=2)
  example2 = Example(x=2)

  # Ohne __eq__ wuerde das hier unten nicht funktionieren:
  print(example1 == example2)
  # Denn es wuerde die Speicheradresse zurueckgeben, was wie Adresse 1 != Adresse 2 ein False erzeugt.
  # Daher die __eq__, welche sagt, was vom Objekt mit dem anderen Objekt verglichen werden soll.
  # Dabei akzeptiert __eq__ als Argument self und other, other ist dann das andere Objekt und man vergleicht self.x == other.x etc.
  # Rueckgabe sollte dann True oder False.
  # Weitere Argumente duerfen nicht genutzt werden, da diese dann Fehler triggern wuerden.

  # Die Methode oben prueft auch, ob es ein Objekt der Klasse Example erhaelt und andernfalls gibt es eine Warnung aus und return False.
  print(example1 == 'test')

  # Das hier gibt dann __repr__ zurueck:
  print(repr(example1))

  # Dabei ist es wichtig, dass man return <string> macht und nicht print().
  # Damit der Aufrufer entscheiden kann, was er mit dem String macht.
  # Beispiel:
  my_examples = [example1, example2]
  my_examples_repr = [repr(example) for example in my_examples]
  # Hier soll eine Liste der __repr__ Strings gemacht werden und das geht nicht, wenn die Methode __repr__ print() macht statt return <string>.
  # Der Return Value waere dann None und my_examples_repr hat dann [None, None] statt den String. (print() hat keinen Rueckgabewert und daher None als Default Rueckgabe.)
#############################################################################

#############################################################################
# Dataclass
# Dataclass muss importiert werden und soll einem vor allem einiges an Boilerplate Code ersparen.
# Es erstellt automatisch __init__, __repr__ und __eq__.

# Import
from dataclasses import dataclass, field

# Dataclass Definition braucht einen Dekorator 
@dataclass
class DataExample:
  x: int = field(default=1)
  # field(default=1) setzt den Default Wert fuer x, __init__ etc muss nicht geschrieben werden.
  # Man braucht also kein:
  # def __init__(self, x=1):
  #    self.x = x

  def add(self, number):
    """
    Addiert number zu x hinzu
    """
    self.x += number
    return

# Erstellt einen Default als leere Liste indem es default_factory nutzt
@dataclass 
class DataExample2:
  x: list = field(default_factory=list)
  # nicht: x: list = field(default_factory=list()) -> keine ()! 
  # Klammen wuerden die Funktion/Klasse direkt aufrufen. Man gibt das Callable (Name Klasse/Funktion ohne ()), welches auf diese verweist.
  # Bei der Instanzierung ruft default_factory dann es auf und list() gibt einfach [] zurueck. 

  def append_item(self, number=0):
    """
    Fuegt number der Liste x hinzu
    """
    self.x.append(number)
    return

# Factory braucht es, damit immer eine neue Liste erstellt wird. 
# Hat man als Beispiel func(arg=[]) nur, dann wird eine leere Liste erstellt und jeder Aufruf referenziert nur dieses eine Objekt.
# Also func() und ernerut func() verweisen als Default Wert auf die gleiche leere Liste.
# Modifiziert sie ein func() Aufruf, dann ist sie bei allen folgenden func() Aufrufen auch nicht mehr leer. 
# default_factory nimmt das Callable und ruft es auf, wodurch quasi das passiert:
# def func(self, arg=None):
#   if arg is None: self.arg = []
#   else: self.arg = arg
# Das heisst der Default Wert ist None und dieser wird nicht modiziert. Falls aber nicht von einem wirklichen Wert ueberschrieben, so bleibt er None.
# Dann kann mittels if ein neues Listen Objekt erstellt werden, welches bei jedem Aufruf extra erzeugt wird und nicht vom Python Interpreter einmal im Hintergrund, wenn er den Code liest.
# Das oben ist daher im Effekt gleich mit field(default_factory: list).
# Factory entsprechend auch Fabrik gut benannt, da es eben wie eine Fabrik eine beliebige Menge an leeren List Objekten erstellen kann. Damit jeder Aufruf/Instanzierung der Klasse ein eigenes Objekt hat.

def dataclass_example():
  
  # Erstellt Objekt der DataExample:
  example1 = DataExample()
  # Addiere Wert 10 zu x
  example1.add(10)
  # Gib die Klasse aus indem man das automatisch generierte __repr__ nutzt:
  print(example1)

  # Erstellt Objekt der DataExample2:
  example2 = DataExample()
  # Fuege den Wert 10 als Element der Liste hinzu
  example2.append_item(10)
  # Gib die Klasse aus indem man das automatisch generierte __repr__ nutzt:
  print(example2)


#############################################################################

#############################################################################
# Workshop vom Video 09. Objektmodell und Magic Methods - 02. Dataclass
from dataclasses import dataclass, field

@dataclass
class ShoppingListItem:
  product: str
  price: float
  amount: int = field(default=1)

  def total_price(self):
    """
    Returns the total price
    """
    return self.amount*self.price


@dataclass
class ShoppingList:
  items: list = field(default_factory=list[ShoppingListItem])

  def add_item(self, item: ShoppingListItem):
    """
    Adds an element to items
    """
    self.items.append(item)
    return

  def total_price(self):
    """
    Computes price of all items
    """
    return sum(item.total_price() for item in self.items)

  def __len__(self):
    """
    Provides amount of items
    """
    return len(self.items)

  def __getitem__(self, index):
    """
    Access to element of items using index
    """
    if len(self.items) >= index:
      return self.items[index]
    else: return None
#############################################################################

if __name__ == '__main__':

  dataclass_workshop = False
  datenmodell = False
  dataclass = False

  if datenmodell is True:
    datenmodell()
  elif dataclass is True:
    dataclass_example()
  elif dataclass_workshop is True:
    meine_einkaufsliste = ShoppingList()
    meine_einkaufsliste.add_item(ShoppingListItem(product='Tee', price=1.99, amount=2))
    meine_einkaufsliste.add_item(ShoppingListItem(product='Kaffee', price=6.99, amount=1))
  
    print()
    print(f"Die Einkaufsliste als print:\n{meine_einkaufsliste}")
    print()
    print(f"Das erste Element der Einkaufsliste: {meine_einkaufsliste.__getitem__(index=0)}")
    print()
    print(f"Der gesamte Preis fuer alle Elemente der Shoppingliste ist: {meine_einkaufsliste.total_price()} Euro.")
    print()
