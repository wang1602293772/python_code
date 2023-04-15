#列表使用实例。
matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
col2 = [row[1] for row in matrix]#get a  column from a matrix
print (col2)
col2even = [row[1] for row in matrix if  row[1] % 2 == 0]#filter odd item
print(col2even)