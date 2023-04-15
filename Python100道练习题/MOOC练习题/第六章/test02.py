# 已知有一个包含一些同学成绩的字典，计算成绩的最高分、最低分、平均分，
# 并查找所有最高分同学。字典示例：
# scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40}
scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40}
print(max(scores.values()))
print(min(scores.values()))
print(sum(scores.values())/len(scores))
for key,value in scores.items():
    if value==max(scores.values()):
        print(key)
result_name=[key  for key,value in scores.items() if value==max(scores.values())]
print(result_name)
