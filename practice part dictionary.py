# Dictionaries

# Q1
sentence = "python is fun and python is powerful"
d = {}
for word in sentence.split():
    d[word] = d.get(word,0) + 1
print(d)

# Q2
d = {'a':1,'b':2,'c':3}
inv = {v:k for k,v in d.items()}
print(inv)

# Q3
d1 = {'a':1,'b':2}
d2 = {'b':5,'c':3}
result = {**d1, **d2}
print(result)

# Q4
words = ["apple","banana","apricot","berry"]
d = {}
for word in words:
    first_letter=word[0]
    d.setdefault(word[0], []).append(word)
    print(d)

# Q5
d = {'a':40,'b':60,'c':80}
result = {k:v for k,v in d.items() if v > 50}
print(result)

# Q6
data = {"user":{"profile":{"name":"Ali"}}}
name = data.get("user",{}).get("profile",{}).get("name")
print(name)

# Q7
cubes = {x:x**3 for x in range(1,11)}
print(cubes)

# Q8
d = {'a':10,'b':50,'c':30}
key = max(d, key=d.get)
print(key)

# Q9
keys = ['a','b','c']
values = [1,2,3]
d = dict(zip(keys, values))
print(d)

# Q10
d = {'a':1,'b':None,'c':3}
result = {k:v for k,v in d.items() if v is not None}
print(result)