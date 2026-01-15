from math import sqrt, pow

class RatingVar:

    @classmethod
    def verify_rating(cls, rating: int):
        if not isinstance(rating, int) or rating not in range(1, 6):
            raise TypeError('Рейтинг должен быть целым числом от 1 до 5')
        
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.verify_rating(value)
        instance.__dict__[self.name] = value


class User:

    comedy = RatingVar()
    action = RatingVar()
    drama = RatingVar()
    horror = RatingVar()
    melodrama = RatingVar()

    def __init__(self, name, comedy, action, drama, horror, melodrama):
        self.name = name
        self.comedy = comedy
        self.action = action
        self.drama = drama
        self.horror = horror
        self.melodrama = melodrama
        self._add_ratings()

    def __str__(self):
        return f'Имя пользователя: {self.name}\nРейтинг комедий: {self.comedy}\nРейтинг боевиков: {self.action}\nРейтинг драмы: {self.drama}\nРейтинг хорроров: {self.horror}\nРейтинг мелодрам: {self.melodrama}'

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Имя пользователя должно иметь строковый тип данных')
        else:
            self._name = name

    def _add_ratings(self):
        self.user_ratings = []
        self.user_ratings.append(self.comedy)
        self.user_ratings.append(self.action)
        self.user_ratings.append(self.drama)
        self.user_ratings.append(self.horror)
        self.user_ratings.append(self.melodrama)

    @staticmethod
    def euclidean_distance(rat1: list, rat2: list):
        if len(rat1) != len(rat2):
            raise ValueError('Списки оценок долнжы иметь одинаковую длину')
        else:
            sum_squared_diffs = 0
            for i in range(len(rat1)):
                diff = rat1[i] - rat2[i]
                sum_squared_diffs += pow(diff, 2)

            distance = sqrt(sum_squared_diffs)
            return distance
        
    @staticmethod
    def find_k_nearest(users: dict, target_name: str, k = 3):
        if target_name not in users:
            return []
        
        target_ratings = users[target_name]
        distances = []

        for user, ratings in users.items():
            if user == target_name:
                continue

            dist = User.euclidean_distance(target_ratings, ratings)
            distances.append((user, dist))

        distances.sort(key=lambda x: x[1])
        return distances[:k]


usr1 = User('Ivan', 5, 1, 5, 2, 5)
usr2 = User('Fedor', 3, 1, 4, 2, 5)
usr3 = User('Petr', 1, 5, 2, 5, 1)
usr4 = User('Oleg', 2, 5, 1, 4, 2)
usr5 = User('Maria', 5, 2, 4, 1, 5)
usr6 = User('Svetlana', 1, 5, 2, 4, 1)
usr7 = User('Target', 4, 2, 5, 2, 5)

keys = [usr1.name, usr2.name, usr3.name, usr4.name, usr5.name, usr6.name, usr7.name]
values = [usr1.user_ratings, usr2.user_ratings, usr3.user_ratings, usr4.user_ratings, usr5.user_ratings, usr6.user_ratings, usr7.user_ratings]

usr_db = {}
usr_db.update(zip(keys, values))

nearest = User.find_k_nearest(usr_db, usr7.name)

print(f'Пользователь "{usr7.name}" имеет вкусы: {usr7.user_ratings}')
print(f'3 ближайших соседей:')
for name, dist in nearest:
    print(f' -- {name} (Расстояние: {dist:.1f}) -> Вкусы: {usr_db[name]}')