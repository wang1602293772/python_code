#编写input()和output()函数输入，输出5个学生的数据记录。
def stu_input():
   name_list=[]
   score_list=[]
   for i in range(5):
      name = input(f'请输入第{i+1}个学生姓名：')
      score = int(input(f'请输入第{i+1}个学生成绩：'))
      name_list.append(name)
      score_list.append(score)
   return name_list,score_list
def stu_print(name_list,score_list):
   for i in range(len(name_list)):
      print(f'学生{name_list[i]}的成绩为{score_list[i]}')
name_list,score_list=stu_input()
stu_print(name_list,score_list)

