from collections import deque

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = set()

    def add_friend(self, other_user):
        self.friends.add(other_user)
        other_user.friends.add(self)

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age not in range(0, 121):
            raise ValueError('Некорректный возраст')
        else:
            self._age = age

class SocialNetwork:

    def __init__(self):
        self.people = []

    def add_user(self, user):
        self.people.append(user)

    def check_connection(self, user1, user2):
        c_queue = deque([(user1, 0)])
        checked = {user1}

        while c_queue:
            current_user, level = c_queue.popleft()
            if current_user == user2:
                return level
            
            for friend in current_user.friends:
                if friend not in checked:
                    checked.add(friend)
                    c_queue.append((friend, level + 1))

        return -1


# if __name__ == "__main__":
#     import random

#     net = SocialNetwork()

#     names = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
#     users = []

#     print("--- Регистрация пользователей ---")
#     for name in names:
#         age = random.randint(18, 90)
#         u = User(name, age)
#         users.append(u)
#         net.add_user(u)
#         print(f"Пользователь {u.name} ({u.age} лет) зарегистрирован.")

#     print("\n--- Установка связей ---")
#     for _ in range(15):
#         u1 = random.choice(users)
#         u2 = random.choice(users)
        
#         if u1 != u2 and u2 not in u1.friends:
#             u1.add_friend(u2)
#             print(f"{u1.name} теперь дружит с {u2.name}")

#     print("\n--- Проверка рукопожатий (BFS) ---")
#     for _ in range(5):
#         start_user = random.choice(users)
#         end_user = random.choice(users)
        
#         print(f"Ищем связь: {start_user.name} -> {end_user.name}")
#         level = net.check_connection(start_user, end_user)
        
#         if level == -1:
#             print(f"   Результат: Связи нет ❌")
#         else:
#             print(f"   Результат: Связь есть! Рукопожатий: {level} ✅")