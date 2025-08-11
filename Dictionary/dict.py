name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

d = {"name": name, "age": age, "city": city}


print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())

print("Get name:", d.get("name"))


d["age"] = int(input("Enter updated age: "))
d["country"] = input("Enter country: ")

# city_to_remove = input("Enter city to remove: ")
# d.pop(city_to_remove, None) 


d.update({"city": input("Enter new city: ")})

print("Updated Dictionary:", d)
