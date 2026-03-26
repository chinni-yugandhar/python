a = []
for i in range(1,100):
    if i%2==0:
        a.append(i)
print(a)


l=[i for i in range(1,100) if i%2==0]
print(l)

print("=========================================================================================")


l=[ i for i in range(1,100) if i%3==0]
print(l)
print("================================================================================================")



s='python programming'
vol='aeiouAEIOU'

l=[i for i in s if i in vol]
print(l)

print("==================================================================================================")

l=[7,3,2,5,6,4,1,2,8,5,6,7,3,8]
r1=[0 if i%2==0 else  i for i in l]
print(r1)
print("====================================================================================================")

def reels():
    r=['1..100','101..200','201..300','301..400','401..500','501..600']
    for i in r:
        yield i

scroll = reels()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print("=======================================================================================================")



def display():
    yield "pfs-41"
    yield "pfs-31"
    yield "pfs-30"
    yield "pfs-22"
    yield "pfs-50"
    yield "pfs-22"
    yield "pfs-15"
leave = display()
for i in range(7):
    print(next(leave))
    
