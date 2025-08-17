def digit_sum(n):
    return sum(int(d) for d in str(n))


def is_accessible(x, y):
    return digit_sum(x) + digit_sum(y) <= 25


def count_accessible_cells(start_x, start_y):
    queue = [(start_x, start_y)]
    visited = set()
    visited.add((start_x, start_y))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.pop(0)

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in visited and is_accessible(new_x, new_y):
                visited.add((new_x, new_y))
                queue.append((new_x, new_y))

    return len(visited)


if __name__ == "__main__":
    start_x, start_y = 1000, 1000
    result = count_accessible_cells(start_x, start_y)
    print(result)
