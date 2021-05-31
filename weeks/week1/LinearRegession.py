import torch
import matplotlib.pyplot as plt
torch.manual_seed(10) #设置一个随机种子，以便重复实验结果
lr = 0.05 #设置学习率为0.05

#创建训练数据i
x = torch.rand(20, 1) * 10 #创建一个（20,1）的张量，其中每一个数据都是一个x

y = 2*x + (5 + torch.randn(20, 1)) #加入高斯白噪音

#构建线性回归参数，初始化w,b
w = torch.randn((1), requires_grad=True)
b = torch.zeros((1), requires_grad=True)

for item in range(1000):

    #前向传播
    wx = torch.mul(w, x)

    y_pred = torch.add(wx, b)

    #计算MSE loss
    loss = (0.5 * (y - y_pred) ** 2).mean()#系数0.5是为消掉求导过程中的系数2，不加也没没什么关系

    #反向传播
    loss.backward()

    #更新参数
    w.data.sub_(lr * w.grad)  #w = w - lr*w.grad
    b.data.sub_(lr * b.grad)  # b = b - lr*b.grad

    # 清零张量的梯度   20191015增加
    w.grad.zero_()
    b.grad.zero_()

    #绘图
    if item % 20 == 0:

        plt.cla() #清楚之前的曲线，防止重叠
        plt.scatter(x.data.numpy(), y.data.numpy())#绘制散点图
        plt.plot(x.data.numpy(), y_pred.data.numpy(),'r-',lw = 5)
        plt.text(2,20,'Loss = %.4f' % loss.data.numpy(),fontdict={'size':20,'color': 'red'})
        plt.xlim=(1.5, 10)
        plt.ylim = (8, 28)
        plt.title("item: {}\nw: {} b: {}".format(item,w.data.numpy(),b.data.numpy()))
        plt.pause(0.5)


        if loss.data.numpy() < 1:
            break
    plt.show()