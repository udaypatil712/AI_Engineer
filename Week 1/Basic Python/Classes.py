class Student:
    def __init__(self , name : str, age: int) -> None:
        self.name = name
        self.age = age

    def printHello(self) -> None:
        # print("hii "+ self.name , self.age)
        return f"hii {self.name} , {self.age}"
    
student1 = Student("uday" , 23)
print(student1.printHello())


class Car:
    def __init__(self , brand:str , price:int , model:str) -> None:
        self.brand = brand
        self.price = price
        self.model = model
    def getDetails(self) -> None:
        return f"car details {self.brand} {self.price} ,{self.model}"  

car1 = Car("MG" , 25000000 , "Hector")
car2 = Car("Toyata" , 25000000 , "Fortunar")
print(car1.getDetails())
print(car2.getDetails())