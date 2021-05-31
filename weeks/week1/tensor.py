# ************example1************
#通过torch.tensor创建张量
import numpy as np
import torch

# arr = np.ones((4,4))
# print("arr的数据类型：",arr.dtype)
# t = torch.tensor(arr,device="cuda")
# print(t)

# ************example2************
# arr = np.array([[1, 2, 3],[4, 5, 6]])
# t = torch.from_numpy(arr)
# t[0,0]=-2
# print("numpy array:",arr)
# print("tensor:",t)

# ************example3************
# out_t = torch.tensor([1])
# t = torch.zeros((3, 3), out=out_t)
# print(t, "\n",out_t)
# print(id(t),id(out_t),id(t)==id(out_t))

# ************example4************
# t = torch.full((3, 3),5)
# print(t)
# ************example5************
# t = torch.arange(1,10,1)
# print(t)

# ************example6************
# t1 = torch.linspace(2,10,5)
# t2 = torch.linspace(2,10,6)
# print(t1,t2)

# ************example7************
# t = torch.eye(4)
# print(t)
# ************example8************
# #1:mean为张量，std为张量
# mean1 = torch.arange(1,4,dtype=torch.float)
# std1 = torch.arange(1,4,dtype=torch.float)
# t1_normal = torch.normal(mean1,std1)
# print(mean1,std1,t1_normal)
# #2:mean为张量，std为标量
# mean2 = torch.arange(1,4,dtype=torch.float)
# std2 = 1
# t2_normal = torch.normal(mean2,std2)
# print(mean2,std2,t2_normal)
# #3:mean为标量，std为张量
# mean3 = 1
# std3 = torch.arange(1,4,dtype=torch.float)
# t3_normal = torch.normal(mean3,std3)
# print(mean3,std3,t3_normal)
# #4:mean为标量，std为标量
# t4_normal = torch.normal(1,1,size=(3,))
# print(t4_normal)


