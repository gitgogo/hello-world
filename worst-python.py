#coding=utf-8
#错误示例
# def use_mutable_default_param(idx=0, ids=[]):
#     ids.append(idx)
#     print(idx)
#     print(ids)

#正确
def use_mutable_default_param(idx=0,ids=None):
	if ids==None:
		ids=[]
	ids.append(idx)
	print idx,ids
use_mutable_default_param(idx=1)
use_mutable_default_param(idx=2)
# list去重
list1 =[1,2,3,4,4,3,2,1]
print reduce(lambda x,y: x if y in x else x+[y],[[]]+list1)
#dict冗余
from collection import defaultdict

i have a trouble,i wnat to back last day