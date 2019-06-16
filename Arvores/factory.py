class Person:
    def __init__(self, name):
        self.name = name


class Man(Person):
	def __init__(self, name):
		super().__init__(name)
		print("Olá Sr", self.name)
		

class Woman(Person):
	def __init__(self, name):
		super().__init__(name)
		print("Olá Sra", self.name)
		

class FactoryPerson:
	def __init__(self):
		pass

	def factoryMethod(self, name, sex):
		if sex == "M":
			return Man(name)
		else:
			return Woman(name)


if __name__ == "__main__":
    factory = FactoryPerson()
    pessoa = factory.factoryMethod("João", "M")
    