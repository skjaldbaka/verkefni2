n = int(input("Enter the length of the sequence: ")) # Do not change this line
a = 1
b = 2
c = 3
print(a)
print(b)
print(c)

for i in range(4, n+1):
    r = a+b+c
    print(r)
    a = b
    b = c
    c = r