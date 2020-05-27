cp={
    'c':1,
    'd':3,
    's':4
}
print(set(cp.values()))
set2=set(cp.values())
set2.update([11, 12])

print(set2)