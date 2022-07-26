import math

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
      if self.__dict__[key] == None:
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

      if (self.vFinal - self.vInitial)/self.acceleration < 0:
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



def SimpleKinematicChosen():
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

def UnknownInitials():
  print("Type 1 for: Range, change in height, angle given")
  print("Type 2 for: Max height, range given")
  print("Type 3 for: Vector magnitude, range, time given")
  choice = int(input())

  if(choice == 1):
    print("Range: ")
    horizDisplacement = float(input())
    print("Veritical Displacement: ")
    vertDisplacement = float(input())
    print("Angle")
    theta = float(input()) * math.pi/180
    if(theta >= 0):
      vectorMagnitude = horizDisplacement/math.cos(theta)* pow(-4.9/(vertDisplacement-horizDisplacement*math.tan(theta)), 0.5)
      print("Vector Scalar: " + str(vectorMagnitude))
      print("Vertical Components: ")
      e = Equation(vectorMagnitude*math.sin(theta),None,None,-9.8,vertDisplacement)
      e.solveKinematic()
      print("Initial velocity: " + str(vectorMagnitude*math.sin(theta)))

  elif(choice == 2):
    print("Range: ")
    horizDisplacement = float(input())
    print("Max Height: ")
    maxHeight = float(input())
    theta = math.atan(4*maxHeight/horizDisplacement) #Theta in radians

    vectorMagnitude = abs(-4.9/(maxHeight - horizDisplacement/(2) * math.tan(theta)))

    vectorMagnitude = horizDisplacement/(2*math.cos(theta))*pow(vectorMagnitude, 0.5)
    print("Angle" + str(theta * 180/math.pi))
    print("Vector Scalar: " + str(vectorMagnitude))
    print("Vertical Components: ")
    e = Equation(vectorMagnitude*math.sin(theta), None, horizDisplacement/(vectorMagnitude*math.cos(theta)), -9.8, None)

    e.solveKinematic()
    print("Initial velocity: " + str(vectorMagnitude*math.sin(theta)))
    print("Time In Motion : " + str(horizDisplacement/(vectorMagnitude*math.cos(theta))))

  elif(choice == 3):
    print("Initial Velocity: ")
    vectorMagnitude = float(input())
    print("Range: ")
    horizDisplacement = float(input())
    print("Time: ")
    timeElapsed = float(input())
    theta = math.acos(horizDisplacement/(vectorMagnitude*timeElapsed))
    e = Equation(vectorMagnitude*math.sin(theta),None, horizDisplacement/(vectorMagnitude*math.cos(theta)), -9.8, None)
    e.solveKinematic()
    print("Angle: " + str(theta * 180/math.pi))


print("Enter: \n 1 for Simple Kinematic \n 2 for Unknown Initials")
choice = int(input())
if(choice == 1):
  SimpleKinematicChosen()
elif(choice == 2):
  UnknownInitials()
