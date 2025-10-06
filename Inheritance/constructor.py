class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def dispaly(self):
        print(f"name:{self.name},Age:{self.age}")

a=person("pratik",20)
a.dispaly()