from debug import debugmethods

@debugmethods
class Inky:
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

@debugmethods
class Oopy:
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
