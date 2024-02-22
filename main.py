import copy
from collections import deque
from heapq import heappush, heappop

def build_array(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    array_2d = []
    for line in lines:
        row = []
        i = 0
        line = line.rstrip('\n')

        while i < len(line):
            if line[i] == 'w':
                row.append('w')
                i += 1
            elif line[i] == 'z':
                row.append('z')
                i += 1
            elif line[i] == 'S':
                row.append('S')
                i += 1
            elif line[i] == 'A':
                row.append('A')
                i += 1
            elif line[i] == '|':
                row.append(1)
                i += 1
            elif line[i] == '+':
                row.append(1)
                i += 1
            elif line[i:i + 3] == '---':
                row.append(1)
                i += 3
            elif line[i:i + 3] == '   ':
                row.append(0)
                i += 3
                if i < len(line) and line[i] == ' ':
                    row.append(0)
                    i += 1
            elif line[i:i + 3] == ' w ':
                row.append('w')
                i += 3
                if i < len(line) and line[i] == ' ':
                    row.append(0)
                    i += 1
            elif line[i:i + 3] == ' S ':
                row.append('S')
                i += 3
                if i < len(line) and line[i] == ' ':
                    row.append(0)
                    i += 1
            elif line[i:i + 3] == ' Z ':
                row.append('z')
                i += 3
                if i < len(line) and line[i] == ' ':
                    row.append(0)
                    i += 1
            elif line[i:i + 3] == ' A ':
                row.append('A')
                i += 3
                if i < len(line) and line[i] == ' ':
                    row.append(0)
                    i += 1
            else:
                print("None of the conditions matched at index", i)
                i += 1

        array_2d.append(row)
    return array_2d

def generate_moves_dictionary(arr):
    moves_dict = {}
    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            valid_moves = []

            # Check left
            if j > 0 and arr[i][j-1] in [0, 'S', 'z', 'w', 'A']:
                valid_moves.append((i, j-1))
            # Check right
            if j < cols - 1 and arr[i][j+1] in [0, 'S', 'z', 'w', 'A']:
                valid_moves.append((i, j+1))
            # Check up
            if i > 0 and arr[i-1][j] in [0, 'S', 'z', 'w', 'A']:
                valid_moves.append((i-1, j))
            # Check down
            if i < rows - 1 and arr[i+1][j] in [0, 'S', 'z', 'w', 'A']:
                valid_moves.append((i+1, j))

            moves_dict[(i, j)] = valid_moves

    return moves_dict

def get_anato_position(state):
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell == 'A':
                return i, j
    return -1, -1

def swap(state, pos1, pos2):
    state[pos1[0]][pos1[1]], state[pos2[0]][pos2[1]] = state[pos2[0]][pos2[1]], state[pos1[0]][pos1[1]]
    return state


def dfs(initialState, moves_dictionary):
    print("DFS Started")
    visited = set()
    stack = deque([(initialState, [], 0)])  # Counter for weapons

    while stack:
        current_state, path, weapons = stack.pop()
        current_state_tuple = tuple(map(tuple, current_state))
        visited.add(current_state_tuple)

        i, j = get_anato_position(current_state)

        for move in moves_dictionary[(i, j)]:
            k, m = move
            if current_state[k][m] == 'S':
                path.append(current_state)
                print("Congratulations, Anato reached a Safe House")
                return path  # Found the destination

            if current_state[k][m] == 'z' and weapons > 0:
                new_state = swap(copy.deepcopy(current_state), (i, j), (k, m))
                if tuple(map(tuple, new_state)) not in visited:
                    path.append(current_state)
                    stack.append((new_state, path, weapons - 1))
            elif current_state[k][m] == 'w':
                new_state = swap(copy.deepcopy(current_state), (i, j), (k, m))
                if tuple(map(tuple, new_state)) not in visited:
                    path.append(current_state)
                    stack.append((new_state, path, weapons + 1))
            elif current_state[k][m] == 0:
                new_state = swap(copy.deepcopy(current_state), (i, j), (k, m))
                if tuple(map(tuple, new_state)) not in visited:
                    path.append(current_state)
                    stack.append((new_state, path, weapons))
            elif current_state[k][m] == 'z' and weapons <= 0:
                # No weapons, cannot proceed
                continue

    return "“Oh, no. Anato is doomed and going to die in suspense without watching the Final episode.”"
#######################################################################################################
def bfs(initialState, moves_dictionary):
    print("BFS Started")
    visited = set()
    queue = deque([(initialState, [], 0)])  # Counter for weapons

    while queue:
        current_state, path, weapons = queue.pop()
        current_state_tuple = tuple(map(tuple, current_state))
        visited.add(current_state_tuple)

        i, j = get_anato_position(current_state)

        for move in moves_dictionary[(i, j)]:
            k, m = move
            if current_state[k][m] == 'S':
                path.append(current_state)
                print("Congratulations, Anato reached a Safe House")
                return path  # Found the destination

            if current_state[k][m] == 'z' and weapons > 0:
                new_state = swap(copy.deepcopy(current_state), (i, j), (k, m))
                if tuple(map(tuple, new_state)) not in visited:
                    path.append(current_state)
                    queue.append((new_state, path, weapons - 1))
            elif current_state[k][m] == 'w':
                new_state = swap(copy.deepcopy(current_state), (i, j), (k, m))
                if tuple(map(tuple, new_state)) not in visited:
                    path.append(current_state)
                    queue.append((new_state, path, weapons + 1))
            elif current_state[k][m] == 0:
                new_state = swap(copy.deepcopy(current_state), (i, j), (k, m))
                if tuple(map(tuple, new_state)) not in visited:
                    path.append(current_state)
                    queue.append((new_state, path, weapons))
            elif current_state[k][m] == 'z' and weapons <= 0:
                # No weapons, cannot proceed
                continue

    return "“Oh, no. Anato is doomed and going to die in suspense without watching the Final episode.”"
#######################################################################################################

# Main code

array_2D = build_array("sample.txt")
# for row in array_2D:
#     print("length: ", len(row))
#     print(row)
moves = generate_moves_dictionary(array_2D)
# for key, value in moves.items():
#     print(f"{key}: {value}")

initial_state = array_2D  # Assuming the initial state is the grid read from the file
result = dfs(initial_state, moves)
if isinstance(result, list):
    print("Path found:")
    for state in result:
        for row in state:
            print(''.join(map(str, row)))  # Converting integers to strings before joining
        print()  # Empty line between states
else:
    print(result)
