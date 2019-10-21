##l=[]
##b=[]
##if __name__ == '__main__':
##    for i in range(int(input())):
##        name = input()
##        score = float(input())
##        b.append(score)
##        a = [name , score]
##        l.append(a)
##        
##
##b.sort()
##
##from statistics import mean 
##if __name__ == '__main__':
##    n = int(input())
##    student_marks = {}
##    for _ in range(n):
##        name, *line = input().split()
##        scores = list(map(float, line))
##        student_marks[name] = scores
##    query_name = input()
##    a=mean(student_marks.get(query_name))
##    print(round(a,2))


##def solve(s):
##    sen = ''.join(s.split())
##    if sen.isalnum():
##        a=s.split()
##        for i in range(len(a)):
##            if a[i].isalpha():
##                return a[i].capitalize()
##    else:
##        return s.title()

##from itertools import product
##a =[int(x) for x in input().split()]
##b =[int(x) for x in input().split()]
##
##print(list(product(a,b)).split(','))



##n , m = map(int,input().split())
##arr = input().split('')
##a =set(input().split(''))
##b =set(input().split(''))
##happiness = 0
##
##for i in arr:
##    if i in  a:
##        happiness+=1
##    else:
##        happiness-=1
##
##print(happiness)




##n = int(input())
##a = list(map(int,input().split(' ')))
##a = a.sort()
##for i in range(a):
##    if a[i] == a[i+1]:
##        pass
##    else:
##        print(a[i])



##
##import re
##
##name_check = re.compile(r"[^A-Za-zs.]")
##
##name = input("Please, enter your name: ")
##
##while name_check.search(name):
##    print("Please enter your name correctly!")
##    name = input("Please, enter your name: ")




def fibonacci(n):
    # return a list of fibonacci numbers
    if n==1 :
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))
