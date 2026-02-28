s1 = {1, 45, 67, 4, 99, 23}
s2 = {4, 45, 23, 67, 73, 13}

print(s1.union(s2))
print(s1.intersection(s2))

print({1,45}.issubset(s1))
print(s2.issuperset({67, 73}))

