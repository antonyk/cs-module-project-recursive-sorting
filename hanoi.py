
a = [5, 4, 3, 2, 1]
b = []
c = []

def hanoi(n, source, target, spare):
    if n > 0:
        hanoi(n-1, source, spare, target)
        target.append(source.pop())
        hanoi(n-1, spare, target, source)

hanoi(len(a), a, c, b)

print(c)