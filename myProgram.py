print('Testing')

class Computer:
    def __init__(self, type_of_computer, color_of_pc, price_of_pc, brand_of_pc):
        self.type_of_computer = type_of_computer
        self.color_of_pc = color_of_pc
        self.price_of_pc = price_of_pc
        self.brand_of_pc = brand_of_pc

    def playGame(self,game):
        print("The name of the game is",game)

laptop = Computer('laptop','Rose Gold',1300,'Asus')
print(laptop.type_of_computer)
print(laptop.color_of_pc)
print(laptop.price_of_pc)
print(laptop.brand_of_pc)

laptop.playGame("call of duty")

class laptop1(Computer):
    def __init__(self,color_of_pc, price_of_pc, brand_of_pc):
        Computer.__init__(self,'laptop',color_of_pc,price_of_pc,brand_of_pc)

Mac = laptop1('rose gold', '1600', 'Mac')
print(Mac.type_of_computer)
print(Mac.color_of_pc)
print(Mac.price_of_pc)
print(Mac.brand_of_pc)
Mac.playGame("MapleStory")

class desktop1(Computer):
    def __init__(self,color_of_pc, price_of_pc, brand_of_pc):
        Computer.__init__(self,'desktop',color_of_pc,price_of_pc,brand_of_pc)

Dell = desktop1('silver', 2400,'Dell')
print(Dell.type_of_computer)
print(Dell.color_of_pc)
print(Dell.price_of_pc)
print(Dell.brand_of_pc)
Dell.playGame("Auditionsea")

print('hello world')