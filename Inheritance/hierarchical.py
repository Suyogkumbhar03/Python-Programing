class Parent:
    def show(self):
        print("Parent class")

class Child1(Parent):
    def child1_info(self):
        print("Child1 class")

class Child2(Parent):
    def child2_info(self):
        print("Child2 class")

c1 = Child1()
c2 = Child2()

c1.show()
c1.child1_info()

c2.show()
c2.child2_info()