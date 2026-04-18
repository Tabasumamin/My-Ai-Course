List

Q1
a=20
list=[a**2 for a in range(21) if a%2==0]
print(list)

Q2
nums=[3,1,4,1,5]
sorted_nums=sorted(nums)
print(sorted_nums)
print(nums)

Q3
lst = [1,2,2,3,4,3,5]
result = []
for x in lst:
    if x not in result:
        result.append(x)
print(result)

Q4
nested = [[1,2],[3,4],[5]]
flat = [x for sub in nested for x in sub]
print(flat)

Q5
names = ['alice','Bob','charlie','DAVID']
sorted_names = sorted(names, key=str.lower)
print(sorted_names)

Q6
a = [10,20,30,40,50,60]
a[2:5] = [100,200]
print(a)

Q7
lst = [7,2,7,4,7,6]
indices = [i for i,x in enumerate(lst) if x == 7]
print(indices)


Q8
lst = [1,2,2,3,4,4,5]
unique = [x for x in lst if lst.count(x) == 1]
print(unique)

Q9
lst = [1,2,3,4]
rotated = lst[-1:] + lst[:-1]
print(rotated)

Q10
lst = [1,2,3,4,5,6]
even = [x for x in lst if x % 2 == 0]
odd = [x for x in lst if x % 2 != 0]
print(even)
print(odd)