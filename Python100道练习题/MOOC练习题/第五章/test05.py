# 开发敏感词语过滤程序，提示用户输入评论内容，如果
# 用户输入的内容中包含特殊的字符：敏感词列表 li = ["你
# 懂的","密码",”法轮功”,”国民党”]，则将用户输入的
# 内容中的敏感词汇替换成***，并添加到一个列表中；如果
# 用户输入的内容没有敏感词汇，则直接添加到上述的列表中
li = ["你懂的","密码","法轮功","国民党"]
filtered_comments = []  # 存放过滤后的评论
while True:
    content=input('请输入评论的内容')
    if content=='':
        print('程序退出！！！')
        break
    else:
        flag=False
        for i in li:
            if i in content:
                content=content.replace(i,'***')
                filtered_comments.append(content)
                flag=True
        if flag==False:
            li.append(content)
    print(filtered_comments)
    print(li)
