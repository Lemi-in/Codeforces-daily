def num_lattice_points(r):
    return 4 * (r ** 2)

t = int(input())
for _ in range(t):
    r = int(input())
    print(num_lattice_points(r) - num_lattice_points(r - 1))