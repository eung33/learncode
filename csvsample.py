import csv




f = open('sample.csv', 'r', encoding='utf-8')
rd = csv.reader(f)
lines = []
array = []

#print(rd)
for line in rd:
    print(line[0])
#    print(type(rd))
    lines.append(line[0][12])

print(lines)

# for i in range(0,4):
#     a = lines[0][i]
#     print(a)

# print(a)

# print(type(lines))
# print(lines[0][1])
# a = lines[0][1]
# print(type(a))


# for i in range(lines[0])
#     print(lines[i][0])

f = open('sample2.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerows(lines)
f.close()