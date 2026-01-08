# Навигатор для марсохода по станциям. Ищет самый дешевый (менее энергозатратный) путь до нужной станции.
class Station: # инициализация класса для станций

    def __init__(self, name, _energy_res): # инициализация объекта класса Station (создание станции с атрибутами: имя, запас энергии, связь)
        self.name = name
        self.energy_res = _energy_res
        self.connections = {}

    def __str__(self): # метод возврата имени станции вместо названия объекта класса для строки 83.
        return self.name
    @property
    def energy_res(self):
        return self._energy_res
    
    @energy_res.setter
    def energy_res(self, energy_res):

        if energy_res < 0:
            raise ValueError('Значение запаса энергии не может быть отрицательным числом')
        else:
            self._energy_res = energy_res

    def add_connection(self, other_station, cost): # метод для добавления связи между двумя станциями 
        self.connections[other_station] = cost
        other_station.connections[self] = cost

class Map: # инициализация класса для карты станций

    def __init__(self): # инициализация объекта класса. Карта станций
        self.stations = {}

    def add_station(self, station): # метод для добавления станции на карту

        if len(station.name) < 1:
            raise ValueError('Имя станции должно состоять хотя бы из одного символа')
        else:
            self.stations[station.name] = station

    def add_route(self, station_name1, station_name2, cost): # метод для добавления "взвешенного" пути. Указываем стоимость(энергия) перехода от одной станции к другой
        
        if station_name1 not in self.stations or station_name2 not in self.stations:
            raise KeyError('Станция не найдена')
        else: 
            station1 = self.stations[station_name1]
            station2 = self.stations[station_name2]
            station1.add_connection(station2, cost)

    def get_fastest_route(self, start_name, end_name): # метод для поиска самого "дешевого" пути от одной станции к другой.
        costs = {}
        parents = {}
        checked = set()

        if start_name not in self.stations or end_name not in self.stations:
            raise KeyError('Путь не найден. Вероятно, одна, или обе станции отсутствуют на карте.')
        else:
            start_station = self.stations[start_name]
            end_station = self.stations[end_name]
            costs[start_station] = 0
            for station in self.stations.values():
                costs[station] = float('inf')
                parents[station] = None
            costs[start_station] = 0
            node = self.find_lower_cost_node(costs, checked)

            while node:
                current_node_cost = costs[node]
                for neighbor in node.connections:
                    new_cost = current_node_cost + node.connections[neighbor]
                    if new_cost < costs[neighbor]:
                        costs[neighbor] = new_cost
                        parents[neighbor] = node
                checked.add(node)
                node = self.find_lower_cost_node(costs, checked)

            path = []
            current = end_station
            while current:
                path.append(current.name)
                current = parents[current]

            path.reverse()

            return f'Маршрут от {start_station} до {end_station}: {' -> '.join(path)}\n Потрачено энергии: {costs[end_station]}'


    @classmethod
    def find_lower_cost_node(self, costs, checked): # метод для поиска самой дешевой станции
        lowest_price = float('inf')
        lowest_node = None

        for node in costs:
            node_cost = costs[node]
            if node_cost < lowest_price and node not in checked:
                lowest_price = node_cost
                lowest_node = node
        
        return lowest_node

# тест
if __name__ == "__main__":

    mars_map = Map()

    s1 = Station("Base Alpha", 100)
    s2 = Station("Crater X", 50)
    s3 = Station("Valley Y", 80)
    s4 = Station("Canyon Z", 60)

    mars_map.add_station(s1)
    mars_map.add_station(s2)
    mars_map.add_station(s3)
    mars_map.add_station(s4)

    mars_map.add_route("Base Alpha", "Valley Y", 5)
    
    mars_map.add_route("Base Alpha", "Crater X", 15)

    mars_map.add_route("Valley Y", "Crater X", 2)

    mars_map.add_route("Valley Y", "Canyon Z", 20)

    mars_map.add_route("Crater X", "Canyon Z", 5)

    print("--- Тест навигации ---")

    print(mars_map.get_fastest_route("Base Alpha", "Canyon Z"))