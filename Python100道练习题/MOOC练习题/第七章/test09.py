side_length=int(input('请输入正方形边长'))
for i in range(side_length):
    if side_length>1:
        if i==0 or i ==side_length-1:
            print('*'*side_length)
        else:
            print('*',end='')
            print(' '*(side_length-2),end='')
            print('*', end='')
            print()
