"A class representing a couple of kittens"

class Animal():
	name = "jellona"

	def sound(self):
		return "Some jellona sounds"

def __repr__(self):
    return f"<Animal {self.name}>"

class Kitten(Animal):
	def sound(self):
		return "Miau!"

def main():
	kitten = Kitten()
	print(kitten.sound())
	print(kitten.name)


if __name__ == "__main__":
	main()