#direct methods(slicing)
# l=[10,20,30,40]
# l=l[1:]+l[0:1]
# print(l);
# #pop and append
# l1=[10,20,30,50]
# l1.append(l1.pop(0))
# print(l1)

def rotatebyleft(l):
    n = len(l)
    start=l[0]
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=start
    return l
l=[10,20,30,40]
print(rotatebyleft(l))