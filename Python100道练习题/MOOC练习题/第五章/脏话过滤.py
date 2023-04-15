# 开发敏感词语过滤程序，提示用户输入评论内容，如果
# 用户输入的内容中包含特殊的字符：敏感词列表 li = ["你
# 懂的","密码",”法轮功”,”国民党”]，则将用户输入的
# 内容中的敏感词汇替换成***，并添加到一个列表中；如果
# 用户输入的内容没有敏感词汇，则直接添加到上述的列表中
violations_comments_list = []
li = ["你懂的", "密码", "法轮功", "国民党"]
comments = input('输入评论内容')
flag = True
for word in li:
    if word in comments:
        comments = comments.replace(word, '***')
        violations_comments_list.append(comments)
        flag = False
if flag:
    li.append(comments)
print('violations_comments_list=', violations_comments_list)
print('li=', li)
print(comments)
