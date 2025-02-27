class Car:
    color = None  
    fuel = None   
    model = None
    year = None  
    def go(self):
        print(f"{self.model} едет.")

    def turn(self):
        print(f"{self.model} поворачивает.")

    def stop(self):
        print(f"{self.model} остановился.")

    def display_info(self):
        print(f"Модель: {self.model}")
        print(f"Цвет: {self.color}")
        print(f"Год выпуска: {self.year}")
        print(f"Количество топлива: {self.fuel} литров")
myCar = Car()
myCar.color = 'красный'  
myCar.fuel = 50         
myCar.model = 'Toyota' 
myCar.year = 2020        
myCar.display_info()
myCar.go() 
myCar.turn() 
myCar.stop() 
