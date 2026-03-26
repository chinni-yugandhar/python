def wish(name):
    return f'hello{name}, welcome to python '


wish1 = lambda name: f'hello {name}, welcome to python '

print(wish("chinni"))
print(wish("mouni") )


add1 = lambda a,b,c:(a+b+c)/3

print(add1(1,2,3))
print(add1(6,7,8))

#number even or odd

def iseven(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

iseven = lambda n: "even" if n%2==0 else "odd"
print(iseven(21))
print(iseven(48))
#greaterthan lessthan

def greater(a,b):
    if a>b:
        return a
    else:
        return b

get = lambda a,b : a if a>b else b
print(get(19,9))
print(get(21,48))


#vowels

def isvowel(a):
    if a in vowel:
        return "vowel"
    else:
        return "con"

isvowel = lambda a: "vol"   if a in vol else "con"
vol ='aeiouAEIOU'
print(isvowel('a'))
print(isvowel('k'))


'''l=[10,20,30,40]
res=[20,30,40,50]=map
res1=[20,40]=filter
res2=100=reduce
'''

'''def func(l):
    for i in range(len(l)):
        l[i]+=l[i]*0.18
        return

l = ['anju','prasanna','tarun','manideep','bhuvan']

res = list(map(lambda i:i.title(),l))

print(func(1))
print(res)'''



'''def func(l):
    res=[]
    for i in range(len(l)):
        if l[i]%3==0:
            res.append(l[i])
    return res

l=[20,30,40,50,60,70,80,90,100]
res = list(filter(lambda i:i%3==0,l))
print(func(l))
print(res)
'''



'''l={'laptop':True,
   'iphone':False,
   'mouse':True,
   'tablet':False,
   'charger':True
}
res = list(filter(lambda i:l[i],i))
print(res)
'''

'''l=[91,2,3,4,5,6,7,21,48,47,11,43,40,51]
res = list(filter(lambda i:i!=0,l))
print(res)
'''
'''from functools import reduce

l=[1,2,3,1,4,5,6,7,8,1,9,0,2,3]
res = reduce(lambda a,b:a*b,l)

print(res)
'''
'''from functools import reduce

l=['python','java', 'c','html','react js']
res = reduce(lambda a,b:a+' '+b,1)
print(res)
'''
d = {
    'apple':30,
    'orange':25,
    'pipeapple':60,
    'mango':50,
    'graps':120
}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[l])))

    
     

