import csv

# f = open('sample.csv', 'w', encoding='utf-8', newline='')
# wr = csv.writer(f)
# wr.writerows([[1,2,3],[4,5,6],[7,8,9]])
# f.close()


f = open('sample.csv', 'r', encoding='utf-8')
rd = csv.reader(f)
#print(rd)
for i in rd:
    print(i)
    print(type(i))
f.close