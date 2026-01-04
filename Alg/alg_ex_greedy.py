# Жадные алгоритмы. Пример с радиостанциями и покрытием из книги.
stations = {}
stations['Mayak'] = set(['Moscow', 'Tyumen', 'Tver'])
stations['Zvezda'] = set(['Tyumen', 'Pskov', 'Kaliningrad'])
stations['Maximum'] = set(['Tver', 'Arkhangelsk', 'Simferopol'])
stations['Record'] = set(['Orel', 'Ryazan', 'Moscow'])

needed_states = set(['Moscow', 'Orel', 'Ryazan', 'Arkhangelsk'])

final_stations = set()

while needed_states:
    best_station = None
    states_covered = set()
    for station, station_states in stations.items():
        covered = needed_states & station_states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    needed_states -= states_covered
    final_stations.add(best_station)

print(final_stations) #{'Maximum', 'Record'}
