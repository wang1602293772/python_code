'''
有4个人，他们分别是A、B、C、D。他们中的某些人是朋友，某些人之间是敌人。已知：
A和B是朋友；
C和D是敌人；
A不喜欢D；
B和C是朋友或者敌人。
'''
for A in ['B','C','D']:
    for B in ['A','C','D']:
        for C in ['A','B','D']:
            for D in ['A','B','C']:
                if A!='D' and A=='B' and C!='D' and (B!='C' or B=='C'):
                    print('A',A,'  B',B,'  C',C,'  D',D)
