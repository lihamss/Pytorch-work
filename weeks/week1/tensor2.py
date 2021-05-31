import torch
import numpy as np
# ************example1***********
# t = torch.ones((2,3))
# t_0 = torch.cat([t,t],dim=0)
# t_1 = torch.cat([t,t],dim=1)
# print("t_0:{} shape:{}\nt_1:{} shape:{}".format(t_0, t_0.shape,t_1,t_1.shape))

# ************example2***********
# t = torch.ones((2,3))
# t_stack = torch.stack([t,t],dim=0)
# print("t_stack:{}\nshape:{}".format(t_stack,t_stack.shape))

# ************example3***********
# a = torch.ones((2,3))
# list_of_tensors = torch.chunk(a, dim=1, chunks=3)
# for idx,t in enumerate(list_of_tensors):
#     print("第{}个张量:{},shape is {}".format(idx+1,t, t.shape))

# ************example4***********
# t = torch.ones((2,5))
# list_of_tensors = torch.split(t, [1,2,1,1],dim=1)
# for idx,t in enumerate(list_of_tensors):
#     print("第{}个张量:{},shape is {}".format(idx+1,t, t.shape))

# ************example5***********
# t = torch.randint(0,9,size=(3,3))
# idx = torch.tensor([0,2],dtype=torch.long)
# t_select = torch.index_select(t,dim=0,index=idx)
# print("t:\n{}\nt_select:\n{}".format(t,t_select))

# ************example6***********
# t = torch.randint(0,9,size=(3,3))
# mask = t.ge(5)
# t_select = torch.masked_select(t,mask) #ge表示大于等于
# print("t:\n{}\nmask:\n{}\nt_select:\n{}".format(t,mask,t_select))

# ************example7***********
# t = torch.randperm(8)
# t_reshape = torch.reshape(t,(2,4))
# print("t:\n{}\nt_reshape:\n{}".format(t,t_reshape))
#
# t[1] = 1119
# print("t:\n{}\nt_reshape:\n{}".format(t,t_reshape))
# print("t.data 内存地址：{}".format(id(t.data)))
# print("t_reshape.data 内存地址：{}".format(id(t_reshape.data)))

# ************example8***********
# t = torch.rand((2,2,4))
# t_transpose = torch.transpose(t,dim0=1,dim1=2)
# print("t:{} \nt_transpose:{}".format(t,t_transpose))

# ************example9***********
# t = torch.rand((2,5))
# t_t = torch.t(t)
# print("t:{} \nt_transpose:{}".format(t,t_t))

# ************example10***********
# t = torch.rand((1,1,3,4))
# t_sq = torch.squeeze(t)
# t_unsq = torch.unsqueeze(t_sq,dim=1)
# t_0 = torch.squeeze(t,dim=0)
# t_1 = torch.squeeze(t,dim=1)
# t_2 = torch.squeeze(t,dim=2)
# t_3 = torch.squeeze(t,dim=3)
#
# print(t.shape,
#       t_sq.shape,
#       t_unsq.shape,
#       t_0.shape,
#       t_1.shape,
#       t_2.shape,
#       t_3.shape)

torch.manual_seed(3)
t = torch.rand(5,1)
w = torch.randn((1))
b = torch.rand((1))
print("t:{}\nw:{}\nb:{}\n".format(t,w,b))
