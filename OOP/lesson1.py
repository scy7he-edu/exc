# Объявление класса, создание объектов класса, присваивание локальных атрибутов объектам класса, изменение атрибутов и вывод атрибутов
class TravelBlog:
    total_blogs = 0
    name = ''
    days = 0
blog_1 = TravelBlog()
blog_2 = TravelBlog()
blog_1.name = 'Greece'
blog_1.days = 10
blog_2.name = 'France'
blog_2.days = 7
print(getattr(blog_1, 'name'))
setattr(blog_2, 'days', 14)
print(blog_1.__dict__, blog_2.__dict__)