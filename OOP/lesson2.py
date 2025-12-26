# методы внутри класса, использование параметра self
class Video:

    def set_review(self, rating):
        self.rating = rating

    def get_review(self):
        print(f'Рейтинг видео: {self.rating}')

vid = Video()
vid.set_review(5)
vid.get_review()
