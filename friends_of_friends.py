def dfs(persons, used, person, depth):
    used[person] = True
    if depth == 0:
        return {person}

    result = set()

    for friend in persons[person]:
        if not used[friend]:
            result |= dfs(persons, used, friend, depth - 1)

    return result


def bfs(persons, used, person):
    result = []
    pull = [(person, 0)]
    used[person] = True

    while pull:
        current_person, current_depth = pull.pop(0)

        if current_depth < 2:
            for friend in persons[current_person]:
                if not used[friend]:
                    pull.append((friend, current_depth + 1))
                    used[friend] = True
        else:
            result.append(current_person)

    return result


persons = {}
used = {}

while person12 := input():
    if person12 == '\n':
        break

    person1, person2 = person12.split()

    if person1 not in persons:
        persons[person1] = set()

    if person2 not in persons:
        persons[person2] = set()

    persons[person1] |= {person2}
    persons[person2] |= {person1}

    used[person1] = False
    used[person2] = False

for person in sorted(persons.keys()):
    current_used = used.copy()
    result = sorted(bfs(persons, current_used, person))
    result = ', '.join(result)
    print(f'{person}: {result}')
