import torch
# t = torch.rand(3,3)
# print("t:",t)
# m = t.ge(0.1).float().squeeze()
# print("m:",m)
sample_nums= 100
mean_value = 1.8
bias = 1
n_data = torch.ones(sample_nums, 2)

x0 = torch.normal(mean_value * n_data, 1)+bias #类别0 数据 shape=(100, 2)

x1 = torch.normal(-mean_value * n_data, 1)+bias #类别1 数据 shape=(100, 2)
# print("x0:{}\nx1:{}".format(x0,x1))
# print(x0.size(),x1.size())

