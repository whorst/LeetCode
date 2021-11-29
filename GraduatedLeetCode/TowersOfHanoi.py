# tutorialspoint.com/data_structures_algorithms/tower_of_hanoi.htm

def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        # print("Move disk 1 from source", source, "to destination", destination)
        x = source.pop(0)
        destination.insert(0, x)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    x = source.pop(0)
    destination.insert(0, x)
    TowerOfHanoi(n - 1, auxiliary, destination, source)

s = [1,2,3]
d = []
a = []
print(TowerOfHanoi(3, s,d,a))

print(s, d, a)
    # s  a  d
    # a  d  s