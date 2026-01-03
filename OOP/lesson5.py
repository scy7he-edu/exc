# Singleton. Метод __new__ 
class AppSettings():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, theme):
        self.theme = theme

s1 = AppSettings('Dark')
s2 = AppSettings('Light')
print(id(s1) == id(s2))
print(s1.theme)
