import memory_graph as mg

class Testing:
  """
  This class tests the memory graph.
  """

  def __init__(self, argument):
    self.argument = argument
    return 

  def append_argument(self, appendix):
    """
    Adds appendix to self.argument.
    """
    self.argument += ' '+appendix
    return self.argument

  def __repr__(self):
    return f"This instance of class Testing contains as argument {self.argument}."

  def show_graph(self):
    mg.render(self, 'in.png')
    self.argument = 'Bye World'
    self.tester = {'purpose': 'shows a nested dict', 'nesting': {'question': 'answer'}}
    mg.render(self, 'out.png')
    return


def main():
  """
  Execute class Testing.
  """
  #mg.show(Testing(argument='Hello'))
  #mg.show(Testing(argument='Hello').append_argument(appendix='World'))
  tester = Testing(argument='Hello')
  tester.append_argument(appendix='World')
  tester.show_graph()
  return 'Tester ran'

if __name__ == '__main__':
#  mg.show(main())
  main()

