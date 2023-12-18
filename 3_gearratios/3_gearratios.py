container = list(open('3_gearratios.in.txt'))
symbol = {}

# hard coding in range because we're working with n x n matrix as file input
for r in range(10):
    for c in range(10):
        if container[r][c] not in '0123456789.':
            symbol[(r, c)] = []


print(symbol)
print(container)