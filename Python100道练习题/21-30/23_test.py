#先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。
'''
  *
 ***
*****
 ***
  *
'''
n=3
for i in range(n):
    for j in range(n-1-i):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()
for i in range(n-2,-1,-1):
    for j in range(n-1-i):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()
