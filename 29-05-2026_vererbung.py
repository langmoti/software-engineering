###############################################################################
# Vererbung von Klasse zu Klasse
# class Kindklasse(Elternklasse):
# Die Kinderklasse hat dann alle Methoden von Elternklasse verfuegbar, sofern sie nicht in der Kinderklasse ueberschrieben/neu definiert wurden.
# 
# Dadurch erlaubt isinstance(variable_kindklasse, Elternklasse), da Python Verbindung Kindklasse von Elternklasse ist.
# Natuerlich auch isinstance(variable_kindklasse, Kindklasse).
# 
# Um zB. __init__ zu erweitern in Kindklasse ohne jene von Elternklasse zu ersetzen:
# def __init__(...alle Parameter):
#     super().__init__(Param fuer Elternklasse)
#     self.example = Parameter der Kindklasse
# super() ruft in der geerbeten Methode die Methode der Elternklasse auf
# self muss beim Aufruf dabei nicht mitgegeben werden. 
###############################################################################

###############################################################################
# Abstrakte Klassen
# Klasse, die nur Verhalten fuer Kindklasse bereitstellt, aber ab min. 1 @abstractmethod nicht selbst instanziert werden kann (Error wird geworfen).
# Haben die Klasse abc.ABC als Basisklasse
# Erlauben die Nutzung von @abstractmethod zur Erstellung abstrakter Methoden deren Rumpf oft nur ... (=Ellipsis) ist 
# Jede @abstractmethod muss in Kindklasse ueberschrieben werden
# Hat die Klasse nur abstrakte Methoden -> Interface genannt.
# Beispiel Syntax:
# class Employee(ABC):
#    @abstractmethod
#    def method1(self):
#       ...
# Info: super().method1() kann auch genutzt werden, um sie zu ueberschreiben. 
#       Hilfreich, wenn abstrate Methode Elternklasse statt ... weitere Funktionalitaet bereitstellt.
# Vorteil Interfaces/abstrakte Methoden: Man ist sicher, dass jede Kindklasse die Methode bereitstellen wird.
###############################################################################
