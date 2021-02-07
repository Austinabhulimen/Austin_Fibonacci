#fibonacci sequence
empty_list=[0,1]
new_list=[]
n = int(input("sample input: "))
empty_list = [0,1]
nextnum = []
x = (n+1) -n
new_list=[]
r = []

while n >len(new_list):
    for i in empty_list:
        nextnum = sum(empty_list)
        empty_list.append(nextnum)
        r = empty_list.pop(0)
        new_list.append(r)
    x+=1

lastnum=new_list[-1]
result = tuple(new_list)

print(f"Sample output:{lastnum}{result}")












