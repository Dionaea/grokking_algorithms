from collections import deque


graph = dict()
graph['you'] = ['alice', 'clair', 'bob']
graph['alice'] = ['peggy']
graph['clair'] = ['tom', 'johny']
graph['bob'] = ['peggy', 'anuj']
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def is_mango_seller(name):
    if name[-1] == 'm':
        return True
    return False


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    checked_people = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in checked_people:
            if is_mango_seller(person):
                return person
            else:
                search_queue += graph[person]
        else:
            checked_people.add(checked_people)


search("you")
