roll = [int(x) for x in input("enter rollof 2 students").split()]
name = [x for x in input("enter name 2 students").split()]

d={}
d={roll[i]:name[i] for i in range(2)}
print(d)

