import math

print("Enter all known variables, leave anything unknown blank")
class Equation:
  def __init__(self, vInitial = None, vFinal = None, timeElapsed = None, acceleration = None, displacement = None) :
    self.vInitial = vInitial
    self.vFinal = vFinal
    self.timeElapsed = timeElapsed
    self.acceleration = acceleration
    self.displacement = displacement
  def FindGivens(self):
    unknowns = []
    for key in self.__dict__.keys():
      if self.__dict__[key] == "":
        unknowns.append(key)
    return unknowns

  def solveFirstKinematic(self):
    unknowns = self.FindGivens()
    if('vFinal' in unknowns): 
      self.vFinal = self.vInitial + self.acceleration *  self.timeElapsed
      print("Final Velocity: " + str(self.vFinal))
    elif('vInitial' in unknowns):
      self.vInitial = self.vFinal - self.acceleration * self.timeElapsed
      print("Initial velocity: " + str(self.vInitial))
    elif('acceleration' in unknowns):
      self.acceleration = (self.vFinal - self.vInitial)/self.timeElapsed
      print("Acceleration: " + str(self.acceleration))
    else:
        self.timeElapsed = (self.vFinal - self.vInitial)/self.acceleration

        ##Velocity check

        print("Time elapsed: " + str(self.timeElapsed))

  def solveKinematic(self):
    unknowns = self.FindGivens()
    #Finding first unknown
    if('displacement' in unknowns):
      self.solveFirstKinematic()
    elif('acceleration' in unknowns):
      if('timeElapsed' in unknowns):
        self.timeElapsed = abs(2 * self.displacement/(self.vFinal + self.vInitial))
        print("Time: " + self.timeElapsed)
      elif("vInitial" in unknowns):
        self.vInitial = 2 * self.displacement/self.timeElapsed - self.vFinal
        print("Initial velocity: " + str(self.vInitial))
      else:
        self.vFinal = 2 * self.displacement/self.timeElapsed - self.vInitial
        print("Final Velocity: " + str(self.vFinal))
    elif("vInitial" not in unknowns):
      self.vFinal = pow(pow(self.vInitial, 2) + 2 * self.acceleration * self.displacement, 1/2)
      if (self.vFinal *self.vFinal <= 2 * self.acceleration *self.displacement):
        self.vFinal *= -1
      #Velocity check needed

      print("Final Velocity: " + str(self.vFinal))
    elif("vFinal" not in unknowns):
      self.vInitial = pow(abs(self.vFinal * self.vFinal - 2* self.acceleration * self.displacement), 1/2)

      if (self.vFinal - self.vInitial)/self.acceleration < 0:
        self.vInitial *= -1
      #Velocity check needed

      print("Initial Velocity: " + str(self.vInitial))
    else:
      self.vInitial = (self.displacement - 0.5 * self.acceleration * self.timeElapsed * self.timeElapsed)/self.timeElapsed

      #Velocity check needed NOT REALLY?

      print("Initial Velocity: " + str(self.vInitial))


    ##Second unknown
    if('displacement' not in unknowns):
      self.solveFirstKinematic()
    else:
      self.displacement = (self.vInitial + self.vFinal)/2 * self.timeElapsed
      print("Displacement: " + str(self.displacement))

print("Intial Velocity: ")
vInitial = input()
try:
    vInitial = float(vInitial)
except:
    vInitial = vInitial
print("Final Velocity: ")
vFinal = input()
try:
    vFinal = float(vFinal)
except:
    vFinal = vFinal
print("Time Elapsed: ")
timeElapsed = input()
try:
    timeElapsed = float(timeElapsed)
except:
    timeElapsed = timeElapsed
print("Acceleration: ")
acceleration = input()
try:
    acceleration = float(acceleration)
except:
    acceleration = acceleration
print("Displacement: ")
displacement = input()
try:
    displacement = float(displacement)
except:
    displacement = displacement
e = Equation(vInitial, vFinal, timeElapsed, acceleration, displacement)

e.solveKinematic()


