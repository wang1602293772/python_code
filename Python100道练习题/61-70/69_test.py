#有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
person_number=int(input('请输入人数：'))  #键盘录入围成圈的人数
person_list=[i for i in range(1,person_number+1)] #按人数生成人数序号列表
stay_deal_list=person_list.copy() #浅拷贝一个一样的列表实施处理
count=1 #通过计数器来判断序号是否为3的倍数
while len(stay_deal_list)!=1:
    stay_remove_list = []  # 将需要删除的列表全部放进待删除的列表中，一次性更新事实处理的列表
    for j in stay_deal_list:
        if count%3==0:
            stay_remove_list.append(j)
        count+=1
    for k in stay_remove_list:
        stay_deal_list.remove(k)
print(stay_deal_list)