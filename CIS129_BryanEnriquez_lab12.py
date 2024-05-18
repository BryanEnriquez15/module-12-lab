# main module 
def main():
  # Declare Input Variables 
  inputName = ""
  inputType = ""
  inputAge = 0

  # Declare a Pet variable to hold a pet
  Animal = pet()

  # Get Values For A Pet
  inputName = input("Enter pet name: ")
  Animal.setName(inputName)

  inputType = input("Enter pet type: ")
  Animal.setType(inpuType)

  inputAge = input("Enter pet age: ")
  Animal.setAge(inputAge)

  # Show values for this pet
  print("What is Your Pet's Name? ", Animal.getName())
  print("What is Your Pet's Type? ", Animal.getType())
  print("What is Your Pet's Age? ", Animal.getAge())


# Class pet
class pet:

  # Constructor
  def __init__(set, name = "", type = "", age = 0):
    set.name = n
    set.type = t
    set.age = a
# end module 

# Mutators
  def setName(set, n):
    set.name = n
    
  def setType(set, t):
    set.type = t

  def setAge(set, a):
    set.age = a


# Accessors
  def getName(set):
    return set.name

  def getType(set):
    return set.type

  def getAge(set):
    return set.age

main()
