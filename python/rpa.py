import requests
def get_code(url):
	r=requests.get(url)
	return r.status_code

def del_shuzu(data,x):
    data.pop(x)
    return data

#  把data2中的数据按顺序插入到data1的空值项中

def merge_shuzu_0(data1, data2):
    number=0
    for i in range(len(data1)-1):
        if data1[i]=='':
            # data1.pop(i)
            data1[i] = data2[number]
            number = number + 1
    return data1
# 判断该数组内是否所有元素均为空,全为空则返回true
def is_allnull (data):
    for i in data:
        print (i)
        if i.strip()!='':
            return 'false'


    return 'true'


#

# data=[' ',' -',' ']
# print (is_allnull(data))
def merge_shuzu_1(data1, data2):
    number = 0
    for i in range(len(data1)):
        print (i)
        if i<len(data1):
            if data1[i]!='' and data1[i+1] != '':
                pass
            else:
                data1[i] = data2[number]
                number = number + 1
            # elif data1[i]=='' and data1[i+1] == '':
            #     print (i)
            #     data1[i] = data2[number]
            #     number = number + 1
            # elif data1[i]=='' and data1[i+1] != '':
            #     data1[i] = data2[number]
            #     number = number +1
            # print (data1)
    return data1

def merge_shuzu_4(data1, data2):
    num = 0
    data=[]
    for k in range(len(data1)):
        if data1[k] =='':
            if k==0:
                pass
            else:
                data1[k]=data1[k-1]
                if data1[k]!='':
                    data.append(k)
        print (data)
    for i in data:
        data1[i]=data1[i]+data2[num]
        num+=1
    return (data1)
    # for i in range(len(data1)):
    #     print (i)
    #     if i<len(data1):
    #         if data1[i]!='' and data1[i+1] != '':
    #             data.append(data1[i])
    #         elif data1[i]!='' and data1[i+1] == '':
    #             sign_num = sign_num + 1
    #             sign = data1[i]
    #             if sign_num>sign_allnum:
    #                 sign=''
    #             data.append(sign+data2[number])
    #             number = number + 1
    #         elif data1[i]=='' and data1[i+1] == '':
    #             data.append(sign+data2[number])
    #             number = number + 1
    #         elif data1[i]=='' and data1[i+1] != '':
    #             sign=''
    #             data.append(data2[number])
    #             number = number +1

    #         print (data)
    # return data

def merge_shuzu_2(data1, data2):
    number = 0
    sign=''
    for i in range(len(data1)):
        # print (i)
        if i<len(data1):
            if data1[i]!='' and data1[i+1] != '':
                pass
            else:
                if data1[i]!='':
                    sign=data1[i]
                data1[i] = sign+data2[number]
                number = number + 1
            # print (data1)
    return data1
def merge_shuzu_3(data1, data2):
    number = 0
    sign=''
    for i in range(len(data1)):
        if i<len(data1):
            if data1[i]!='' and data1[i+1] != '':
                pass
            else:
                if data1[i]!='':
                    sign=data1[i]
                else:
                    sign=''
                data1[i] = sign+data2[number]
                number = number + 1
            # print (data1)
    return data1


def merge_shuzu_5(data1, data2):
    num=0
    sign=''
    for i in range(len(data1)-1):
        if data1[i]!='' and data1[i+1]=='':
            sign=data1[i]
            data1[i]=sign+data2[num]
            num+=1
        if data1[i]=='' and data1[i+1]=='':
            data1[i] = sign+data2[num]

    print (data1)



# data = ['a', 'b', 'c']

#
# data1=["序号",
# "法院（含管辖）",
# "首次执行案件",
# "",
# "",
# "",
# "",
# "",
# "",
# "",
# "",
# "",
# "",
# "",
# "恢复执行案件",
# "",
# "",
# "其他",
# "",
# "",
# ""
#
# ]
# data2=["实结占结案数比例（%）",
# "实际执结率（%）",
# "终本占结案数比例（%）",
# "终本率（%）",
# "未结率（%）",
# "实际执行到位率（%）",
# "执行完毕率（%）",
# "终结率（%）",
# "法定期限内结案率（%）",
# "结案平均用时（天/件）",
# "执行完毕案件结案平均用时(天/件）",
# "关键节点平均超期数",
# "执行完毕率（执恢）（%）",
# "终本案件恢复执行平均用时（天/件）",
# "实际执行到位率（执恢）（%）",
# "保全率（%）",
# "终本合格率（%）",
# "终本案件合格率（不含执恢）（%）",
# "（%）"
#        ]
# print (data1+data2)
# print (range(len(data1)))
# print (len(data1))
# print(del_shuzu(data,1))
# print (merge_shuzu_3(data1,data2))
