#хотел закинуть в папку ООП, но это комплексное задание сразу по нескольким урокам Балакирева от гемини.

class BrightnessValue:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        val = max(0, min(100, value))
        setattr(instance, self.name, val)

class Device:
    __slots__ = ('__name', '__brand')

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    @property
    def name(self): return self.__name
    
    @name.setter
    def name(self, value):
        if not value: 
            raise ValueError("Имя не может быть пустым")
        
        self.__name = value

    @property
    def brand(self): return self.__brand
    
    @brand.setter
    def brand(self, value): self.__brand = value

    def __str__(self):
        return f'[Устройство: {self.name} | Бренд: {self.brand}]'

class SmartLight(Device):
    __slots__ = ('_brightness',) 
    brightness = BrightnessValue()

    def __init__(self, name, brand, brightness):
        super().__init__(name, brand)
        self.brightness = brightness

class Office:
    def __init__(self):
        self.devices = []

    def __add__(self, other):
        if isinstance(other, Device):
            self.devices.append(other)
            return self
        raise TypeError("Можно добавлять только объекты Device")
    
    def __len__(self):
        return len(self.devices)

off = Office()
bulb1 = SmartLight('Smart Bulb', 'Xiaomi', 150)
bulb2 = SmartLight('Smart Bulb', 'Kojima', -20)

off + bulb1 
off + bulb2

print(f"Всего устройств: {len(off)}")
print(f"Яркость первой лампы: {bulb1.brightness}") # Выведет 100