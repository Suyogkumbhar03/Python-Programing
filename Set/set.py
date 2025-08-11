# a=set(input("Enter the elements of the set:"))
# print(a)

# a.add(input("Add a new set element:"))
# print(a)

# a.remove(input("Enter the element to remove:"))
# print(a)

# a.pop()
# print("after pop delete random element: ",a)
# a.update(input("Add a new set element:"))
# print(a)



x=set(input("Enter the elements of the set 1:"))
y=set(input("Enter the elements of the set 2:"))

print("Union: ",x.union(y))
print("Intersection",x.intersection(y))
print("Subset",x.issubset(y))
print("Super set",x.issuperset(y))

