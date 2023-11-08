# Multilevel Inheritance
#Level - GF -> F -> S


class Grandparent:
    def grandparent_method(self):
        return "Grandparent's method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"

class Child(Parent):
    def child_method(self):
        return "Child's method"

child = Child()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())
