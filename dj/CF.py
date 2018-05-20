# coding:utf-8
import pandas as pd
import numpy as np
import scipy.spatial.distance as ssd


# 加载借阅数据
def LoadLead(filepath):
    return pd.read_excel(filepath)


# 加载图书和图书编号信息
def LoadBkIfmtion(filepath):
    return pd.read_excel(filepath)


# 加载学生和学生编号信息
def LoadStIfmtion(filepath):
    return pd.read_excel(filepath)


# 分离读者和借阅信息并且除去重复项
def separation(data):
    n = data.drop_duplicates([u'marc_id'])
    marc_id = n[u'marc_id']
    marc_id = pd.Series(marc_id.values)

    n = data.drop_duplicates([u'st_id'])
    st_id = n[u'st_id']
    st_id = pd.Series(st_id.values)
    return marc_id, st_id


# 创建借书矩阵
def creatlendM(data, st_id, book_id):
    lendM = pd.DataFrame([0])
    lendM = pd.DataFrame(lendM, index=st_id.values)
    lendM = lendM.reindex(columns=marc_id.values, fill_value=0)

    i = 0
    while (i < len(data.index)):
        lendM[data.ix[i][u'marc_id']][data.ix[i][u'st_id']] = lendM[data.ix[i][u'marc_id']][data.ix[i][u'st_id']] + 1
        i = i + 1
    return lendM


# 创建相似度矩阵
def creatsimM(lendM, marc_id):
    simM = pd.DataFrame([0.0])
    simM = pd.DataFrame(simM, index=marc_id.values)
    simM = simM.reindex(columns=marc_id.values, fill_value=0.0)
    i = 0
    b5 = 0
    # print b5
    while (i < len(marc_id)):
        j = i + 1
        while (j < len(marc_id)):
            # 如果重叠项目少于5，就直接写相似度为0.1
            t1 = lendM[lendM[marc_id[i]] > 0].index
            t2 = lendM[lendM[marc_id[j]] > 0].index
            t1 = t1.values
            t2 = t2.values
            c = 0
            for k1 in t1:
                for k2 in t2:
                    if (k1 == k2):
                        c = c + 1
            if (c <= 1):
                k = 0
                simM[marc_id[i]][marc_id[j]] = 0.001
                simM[marc_id[j]][marc_id[i]] = 0.001
            else:
                # print marc_id[i]
                # print marc_id[j]
                b5 = b5 + 1
                simM[marc_id[i]][marc_id[j]] = 1.0 - ssd.cosine(lendM[marc_id[i]].values, lendM[marc_id[j]].values)
                simM[marc_id[j]][marc_id[i]] = 1.0 - ssd.cosine(lendM[marc_id[i]].values, lendM[marc_id[j]].values)
            j = j + 1
        i = i + 1
    return simM


# 推荐图书
def recommend(st_name, book_id, simM):
    st_id = st_name
    result_id = list()
    for i in book_id:
        # print(simM[i].max())
        result_id.append(simM[i][simM[i] == simM[i].max()].index.values)

    result = list()
    for line in result_id:
        if len(line) < 10:
            result.append(line[0])

    return result


"""
book_id = list()
book_id.append(199)
book_id.append(640)
book_id.append(750)
book_id.append(839)
book_id.append(943)
book_id.append(946)
book_id.append(988)
book_id.append(1242)
book_id.append(1252)
st_id = 716
bid = recommend(st_id, book_id, simM)
print(bid)
"""
