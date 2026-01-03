# Поиск в ширину, хэш таблица, FIFO, LIFO.
from collections import deque

graph = {}
graph['you'] = ['Alice', 'Bob', 'Michael']
graph['Alice'] = ['Vincent']
graph['Bob'] = ['Tony']
graph['Michael'] = ['Helen']
graph['Vincent'] = ['Clem']
graph['Tony'] = ['Bob']
graph['Helen'] = ['Michael']
graph['Clem'] = ['Vincent']

def is_seller(person):
    return True if person[-1] == 'm' else False

def seller(name):
    search_queue = deque([name])
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_seller(person):
                print(f'The person {person} is a mango seller! | {is_seller(person)}')
                break
            else:
                search_queue += graph[person]
                searched.append(person)
    else:
        print(f'No one is the mango seller :(')

seller('you')