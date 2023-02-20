import numpy as np


def RI(n):
    if n==3: return 0.52
    if n==4: return 0.89
    if n==5: return 1.12
    if n==6: return 1.26
    if n==7: return 1.36
    if n==8: return 1.41
    if n==9: return 1.46
    if n==10: return 1.49


def AHP(*args,matrix):
    matrix=np.asarray(matrix,dtype=float)
    index_list = [*args]
    L_max=max(np.linalg.eig(matrix)[0])
    n=len(index_list)
    CI=(L_max-n)/(n-1)
    CR=CI/RI(n)
    print('CR value={}'.format(CR))
    if CR<0.1:
        print('Weights reasonable')
        for i in range(n):
            sumvalue=sum([matrix[k][i] for k in range(n)])
            for j in range(n):
                temp=matrix[j][i]/sumvalue
                matrix[j][i]=temp
        w_list=[]
        for i in range(n):
            w_list.append(sum(matrix[i]))
        sumvalue = sum(w_list)
        for i in range(len(w_list)):
            w_list[i] = w_list[i] / sumvalue
        print('Weights：',w_list)
        return  w_list
    else:
        print('Weights are not reasonable!')
        for i in range(n):
            sumvalue=sum([matrix[k][i] for k in range(n)])
            for j in range(n):
                temp = matrix[j][i] / sumvalue
                matrix[j][i] = temp
        w_list=[]
        for i in range(n):
            w_list.append(sum(matrix[i]))
        sumvalue=sum(w_list)
        for i in range(len(w_list)):
            w_list[i]=w_list[i]/sumvalue
        print('Weights：',w_list)
        return  w_list




# human activities, extreme weather effect, pollution, salinization
human_activities=[]
extreme_weather=[]
pollution=[]
salinization=[]
matrix=np.array([[1, 5,7,2],
                [1/5,1,1,1/2],
                [1/7,1,1,1/6],
                 [1/2,2,6,1]])
AHP(human_activities,extreme_weather,pollution,matrix=matrix)