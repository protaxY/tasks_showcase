from itertools import product, permutations

suits_map = {'буби': 'бубен',
             'пики': 'пик',
             'трефы': 'треф',
             'черви': 'червей'}

suits = {'бубен', 'пик', 'треф', 'червей'}
values = {'10', '2', '3', '4', '5', '6', '7', '8', '9',
          'валет', 'дама', 'король', 'туз'}

mandatory_suit = input()
excluded_value = input()

previous_triple = tuple([tuple(pair.split()) for pair in input().split(',')])

mandatory_suit = suits_map[mandatory_suit]
values -= {excluded_value}

suits = sorted(suits)
values = sorted(values)

counter = 0

triples = permutations(product(values, suits), 3)
triples = [tuple(sorted(triple)) for triple in list(triples)]
triples = sorted(set(triples))

flag = False
for i, triple in enumerate(triples):
    if flag \
       and (mandatory_suit == triple[0][1]
            or mandatory_suit == triple[1][1]
            or mandatory_suit == triple[2][1]):
        print(
            f'{triple[0][0]} {triple[0][1]}, {triple[1][0]} {triple[1][1]}, {triple[2][0]} {triple[2][1]}')
        break
    if triple == previous_triple:
        flag = True
