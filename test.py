#task 1

def test(a):
    b = []
    for item in a :
        if item not in b:
            b.append(item)
    return b

print(test([1,1,2,2,3,4,5,5,6,7,8,9,9]))


#task 2

 
a = int(input("Первое число: "))             
b = int(input("Второе число: "))
for i in range(a,b):
    count = 0
    d = 2
    while d < i:
        if i % d == 0:
            count += 1
        d += 1
    if count == 0:
        print(f"{i} простое число")    



#task 3

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


p1_x = int(input("p1.x: "))
p1_y = int(input("p1.y: "))

p2_x = int(input("p2.x: "))
p2_y = int(input("p2.y: "))

p1 = Point(p1_x, p1_y)
p2 = Point(p2_x, p2_y)

print(p1.dist(p2))


# task 4
n = ['aaa', 'bbb', 'ccc', 'dddd', 'dddl', 'yyyyy']

n.sort(key=lambda item: (-len(item), item))


print(n)

b = ['aaa', 'bbb', 'ccc', 'dddd', 'dddl', 'yyyyy']

b.sort(key=lambda item: (+len(item), item))

print(b)

