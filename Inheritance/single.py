class animal:
    def speak(self):
        print("The animal make a sound")
class dog(animal):
    def bark(self):
        print("dog is barking")
d=dog()
d.speak()
d.bark()
