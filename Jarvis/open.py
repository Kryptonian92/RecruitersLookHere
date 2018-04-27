i = 1
for item in ['a', 'b','c']:
    print(i, item, sep='. ')
    i += 1

for item in enumerate(['a','b','c'],1):
    print(item)
    print(item[0], item[1], sep='. ')

f = open('test.txt')
for line in f:
    print(line)
f.close()

with open("test.txt") as f:
    for line in f:
        print(line)
