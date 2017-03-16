from debug import DebugClass

class Inky(metaclass=DebugClass):
   def blinky(self):
       pass
   def stinky(self):
       pass
   def slinky(self):
       pass
   def kinky(self):
       pass
   def pinky(self):
       pass

class Oopy(metaclass=DebugClass):
   def snoopy(self):
       pass
   def loopy(self):
       pass
   def droopy(self):
       pass


k = Inky()
k.blinky()
k.stinky()

k = Oopy()
k.snoopy()
k.loopy()
k.droopy()

print(type(k))
print(type(type(k)))
print(type(type(type(k))))
