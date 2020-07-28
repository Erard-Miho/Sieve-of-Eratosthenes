
print('Add your range with a integer')
one= int(input())
a1=[] # All numbers from 2 - 50
for i in range(2,one):
    a1.append(i)

a2=a1 # polymorphism with a1[]

r=0

for j in a2: # iterrate through numbers

    for i in range(2, one):   # 

        e = j**2 + r * j  # formula of P
        r += 1
        
        if e in a1: # if 
            a1.remove(e)
a1.pop(-1)
print(a1)



