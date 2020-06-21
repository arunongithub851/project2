def my_func(a):
    list1=a.split(',')
    list1[0]=int(list1[0].replace('[',''))
    list1[-1]=int(list1[-1].replace(']',''))
    for i in range(list1.index(list1[-1])):
        list1[i]=int(list1[i])
    return list1

def func2(list1):
    b=[]
    for i in range(list1.index(list1[-1])+1):
        if list1[i] >= 0:
            b.append(list1[i])
    print(b)

a=input('list1:')
list1=my_func(a)
func2(list1)

a=input('list2:')
list1=my_func(a)
func2(list1)
