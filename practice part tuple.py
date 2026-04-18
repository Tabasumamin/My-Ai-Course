Tuple

# Q1
lst = [1,2,3,4]
t = tuple(lst)

a,b,c,d = t
print(a,b,c,d)

# Q2
t = (('a',1),('b',2),('c',3))
result = [x[1] for x in t]
print(result)

Q3
def calculation(nums):
    return sum(nums), min(nums), max(nums)

sum,max,min = calculation([2,5,1,8])
print(sum,max,min)

# Q4
t1 = (1,2,3)
t2 = (4,5)

result = list(t1 + t2)
print(result)

# Q5
t = (1,2,3,3,3,4)
freq = max(set(t), key=t.count)
print(freq) 

# Q6
t1 = (1,2,3)
t2 = (3,2,1)
print(sorted(t1) == sorted(t2))

# Q7
t = (1,2,3,4,5,6)
print(t[-3:])

# Q8
t = (1,2)
print(t * 3)

# Q9
t = ((1,2),(3,4))
flat = tuple(x for sub in t for x in sub)
print(flat)

# Q10
p1 = (2,3)
p2 = (5,7)

distance = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
print(distance)