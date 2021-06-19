# f=open('test.txt','r')
# print(f.name)
# print(f.mode)
# f.close()
#use context manager

with open('test.txt', 'r') as f:
    f_contents=f.readline()
    print(f_contents)


print(f.closed)
