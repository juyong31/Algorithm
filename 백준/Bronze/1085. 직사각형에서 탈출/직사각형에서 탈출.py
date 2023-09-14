x, y, w, h = map(int, input().split())

list1 = []
x1 = x - 0
x2 = w - x
y1 = y - 0
y2 = h - y

list1.append(x1)
list1.append(x2)
list1.append(y1)
list1.append(y2)

print(min(list1))