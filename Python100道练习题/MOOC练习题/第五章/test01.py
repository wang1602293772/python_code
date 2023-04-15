# 1、已知商品列表：
# li = ["手机", "电脑", "鼠标垫", "游艇" ]
# a. 允许用户添加商品
# b. 用户输入序号显示内容
li = ["手机", "电脑", "鼠标垫", "游艇" ]
while 1:
    print('请输入序号选择操作\n1.添加商品\n2.查询商品\n3.退出')
    choice=int(input('请输入序号：'))
    if choice==1:
        goods=input('请输入需要添加的商品名称：')
        li.append(goods)
        print('添加成功')
    elif choice==2:
        index_choice=int(input('请输入商品序号'))
        try:
            print(li[index_choice-1])
        except Exception as e:
            print('商品序号不存在')
    elif choice==3:
        break
    else:
        print('输入有误，请重新输入')