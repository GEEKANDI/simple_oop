#this is our class
class pet:
    no_of_legs = 0

#these are methods of the class
    def sleep(self):
        print('zzz')

    def count_legs(self):
        print('I have %s legs' %self.no_of_legs)

"""
This is inheritance
The class dog inherit from the parent class pet but still have other attributes not in the pet class
"""
class dog(pet):

#this is instance of class pet which is an OBJECT 1
doug = pet()

doug.no_of_legs = 4
print('Doug has %s number of legs' %doug.no_of_legs)
doug.sleep()
doug.count_legs()

#another instance of clas pet -> object 2
nemo = pet()
nemo.no_of_legs = 0
nemo.count_legs()