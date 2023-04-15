#找到年龄最大的人，并输出。请找出程序中有什么问题。
person = {"li":18,"wang":50,"zhang":20,"sun":22}
#方法1
# values=list(person.values())
# keys=list(person.keys())
# max_age=max(values)
# max_person=keys[values.index(max_age)]
# print(max_person)
# 方法2
max_person='li'
for i in person:
    if person[i]>person[max_person]:
        max_person=i
print(max_person)