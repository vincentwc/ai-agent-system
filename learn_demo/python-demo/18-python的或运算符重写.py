
class Test(object):
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        return MySequence(self, other)
      
    def __str__(self):
        return self.name

class MySequence(object):
    def __init__(self, *items):
        self.sequence = []
        for item in items:
            self.sequence.append(item)
    def __or__(self, other):
      self.sequence.append(other)
      return self
    def run(self):
      for i in self.sequence:
        print(i)
      
if __name__ == '__main__':
  a = Test('a')
  b = Test('b')
  c = Test('c')
  e = Test('e')
  f= Test('f')
  g = Test('g')

  d = a | b | c | e | f | g
  d.run()
  print(type(d))