from itertools import combinations

NodesEmbedding = [
    0b100000000000000100,   # 0
    0b110000000000010000,   # 1
    0b000100000000000110,   # 2
    0b111000100000100000,   # 3
    0b000110100000011000,   # 4
    0b000001100000000111,   # 5
    0b011000010000000000,   # 6
    0b000110011000100000,   # 7
    0b000001011000011000,   # 8
    0b000000001000000011,   # 9
    0b001000000100000000,   # 10
    0b000010000110000000,   # 11
    0b000001000111100000,   # 12
    0b000000000011001000,   # 13
    0b000000000001000001    # 14
]

NodesOccupied = []
NodesUnoccupied = list(range(15))
safe_stack = []
solution = []

def isSameRow(n1, n2, n3):
    return bool(NodesEmbedding[n1] & NodesEmbedding[n2] & NodesEmbedding[n3])

def getRoads(n):
    options_all = list(combinations(NodesUnoccupied, 2))
    options = []
    for option in options_all:
        if isSameRow(n, option[0], option[1]) is True\
                and ((n < option[0] and n < option[1]) or (n > option[0] and n > option[1])):
            options.append(option)
    return options

def action(n, n1, n2):
    global NodesOccupied
    global NodesUnoccupied
    global solution

    NodesOccupied += [n1, n2]
    NodesOccupied.remove(n)
    NodesUnoccupied.append(n)
    NodesUnoccupied.remove(n1)
    NodesUnoccupied.remove(n2)

    temp_unoccupied = NodesUnoccupied[:]
    solution.append([[n, n1, n2], temp_unoccupied])

def get_back():
    global layer_num
    global NodesOccupied
    global NodesUnoccupied
    global solution

    NodesOccupied = safe_stack[-1][0][:]
    NodesUnoccupied = []
    for i in range(15):
        if i not in NodesOccupied:
            NodesUnoccupied.append(i)

    solution.pop()
    # print(safe_stack)

def main():
    global NodesOccupied
    global NodesUnoccupied
    global safe_stack

    startPoints = [0, 1, 3, 4]
    # for startPoint in startPoints:
    startPoint = startPoints[0]
    NodesOccupied.append(startPoint)
    NodesUnoccupied.remove(startPoint)

    isAction = 1

    while len(NodesUnoccupied) > 1:

        if isAction:
            temp_Occupied = NodesOccupied[:]
            safe_stack.append([temp_Occupied, []])
            for node in temp_Occupied:
                options = getRoads(node)
                for option in options:
                    safe_stack[-1][1].append([node] + list(option))

        if len(safe_stack[-1][1]):
            action(safe_stack[-1][1][0][0], safe_stack[-1][1][0][1], safe_stack[-1][1][0][2])
            isAction = 1
        else:
            if len(safe_stack) > 1:
                safe_stack.pop()
                safe_stack[-1][1].pop(0)
                get_back()
                isAction = 0
            else:
                print('没有找到安全序列。')
                break

    print('Success.\n')
    for each in solution:
        print(f'remove {each[0][0]}, append {each[0][1:]}, NodesUnoccupied: {each[1]}')

if __name__ == '__main__':
    main()
