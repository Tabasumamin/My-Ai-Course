# Sets

# Q1
a = {1,2,3,4}
b = {3,4,5}
print(a-b)

# Q2
a = {1,2,3}
b = {2,3,4}
c = {3,5,2}
print(a & b & c)

# Q3
sentence = "Python is a powerful language"
words = set(sentence.lower().split())
print(words)

# Q4
lst = [4,1,2,2,3,1]
result = sorted(set(lst))
print(result)

# Q5
a = {1,2}
b = {1,2,3}
print(a<b)

# Q6
result = {x*x for x in range(1,16) if x % 3 == 0}
print(result)

# Q7
lst = [1,2,2,3,4,4,5]
duplicates = len(lst) - len(set(lst))
print(duplicates)

# Q8
vowels = {'a','e','i','o','u'}
text = "Malik Waqas"
result = ''.join([y for y in text if y not in vowels])
print(result)

# Q9
a = {1,2,3}
b = {3,4,5}
print(a^b)

# Q10
a = "listen"
b = "silent"
print(set(a) == set(b))