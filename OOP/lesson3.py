# инициализатор, передача атрибутов новому объекту и финализатор
class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        print('Объект создан')
    
    def __del__(self):
        print('Объект удален')

e1, e2, e3 = Point(1, 2), Point(10, 20), Point()
points = [e1.__dict__, e2.__dict__, e3.__dict__]
print(points)