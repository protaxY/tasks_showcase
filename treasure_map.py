def find_treasure(coords: list):
    coord_dict = {}
    for i in range(len(coords)):
        # Делим Х и У на 10, так как для верного пути могут различаться только единицы
        ind = (coords[i][0] // 10, coords[i][1] // 10)
        # При наличии совпадения координаты в словаре - увеличиваем количество кладов рядом с совпавшей точкой
        if ind in coord_dict:
            coord_dict[ind] += 1
        # При отсутствии - создаем новую точку в словаре, от которой будет идти отсчет
        else:
            coord_dict[ind] = 1
    # Ответ - самое большое количество кладов рядом с одной из точек
    print(max(coord_dict.values()))


def main():
    n = int(input())
    coords = []
    # Создаем список кортежей типа (int, int) для каждой введенной строки, разбитой на отдельные координаты
    for _ in range(n):
        coords.append(tuple(map(int, input().split())))
    find_treasure(coords)


if __name__ == "__main__":
    main()
