from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(person):
    if person == 'peggy':
        return True
    else:
        return False


def bf_search(name):
    not_sellers = set()
    search_queue = deque(graph[name])
    while search_queue:
        person = search_queue.popleft()
        if person not in not_sellers:
            if person_is_seller(person):
                return person
            else:
                search_queue.extend(graph[person])
                not_sellers.add(person)
    return False


print(bf_search("you"))
