# def checksort(l):
#     sl=sorted(l)
#     if sl==l:
#         return True
#     else:
#         return False
    
# l=[10,20,30,5,40]
# print("Given list is",l)
# if checksort(l):
#     print("The given list is sorted")
# else:
#     print("The given list is not sorted")

#efficient way
def issorted(l,n):
    n=len(l)
    inc=True
    Dec=True
    for i in range(1,n):
        if l[i]<l[i-1]:
            inc=False
        if l[i-1]<l[i]:
            Dec=False
    if inc or Dec:
        return True
    return False
l=[10,9,8,7,6,5,4,3]
print("Given list is",l)
if issorted(l,len(l)):
    print("The given list is sorted")
else:
    print("The given list is not sorted")

l1=[10,20,30,40]
print("\nGiven list 1 is",l1)
if issorted(l1,len(l1)):
    print("List 1 is also sorted.")
else:
    print("List 1 is not sorted.")