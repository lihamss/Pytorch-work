import torch
# y = (x+w)*(w+2)


# ************retain_graph************
# # 创建叶子结点
# w = torch.tensor([2.], requires_grad=True)
# x = torch.tensor([1.], requires_grad=True)
#
# a = torch.add(x,w)
# b = torch.add(w,2)
# y = torch.mul(a,b)
#
# y.backward(retain_graph=True)
# y.backward()
# print(w.grad)
# torch.autograd.backward(tensors,
#                         grad_tensors=None,
#                         retain_graph=None,
#                         create_graph=False)

# ************grad_tensors************

# w = torch.tensor([2.],requires_grad=True)
# x = torch.tensor([1.],requires_grad=True)
#
# a = torch.add(x,w)
# b = torch.add(w,2)
#
# y0 = torch.mul(a,b) # y0 = (x+w)*(w+2) dy/dw = 7
# y1 = torch.add(a,b) # y1 = (x+w)+(w+2) dy/dw = 2
#
# loss = torch.cat([y0,y1],dim=0)
# grad_tensors = torch.tensor([1.,2.]) # 梯度权重
# loss.backward(gradient=grad_tensors) #将gradient传入torch.autograd.backward()中的grad_tensors
# print(w.grad) #7*1+2*2 = 11

# ************torch.autograd.grad()************
# torch.autograd.grad(outputs,
#                     inputs,
#                     grad_outputs=,
#                     retain_graph=,
#                     create_graph=False)
# flag = True
flag = False
if flag:
    x = torch.tensor([3.],requires_grad=True)
    y = torch.pow(x,2) #y = x**2

    grad_1 = torch.autograd.grad(y,x,create_graph=True)#创建导数的计算图，否则无法进行高阶求导
    print(grad_1)

    grad_2 = torch.autograd.grad(grad_1[0],x)# 注意grad_1是一个tuple，取第一个元素
    print(grad_2)


# flag = True flag = False
if flag:
    w = torch.tensor([2.], requires_grad=True)
    x = torch.tensor([1.], requires_grad=True)
    for i in range(2):

        a = torch.add(x,w)
        b = torch.add(w,2)
        y = torch.mul(a,b)

        y.backward()
        print(w.grad)

        w.grad.zero_()

# flag = True
flag = False
if flag:
    w = torch.tensor([2.], requires_grad=True)
    x = torch.tensor([1.], requires_grad=True)
    a = torch.add(x,w)
    b = torch.add(w,2)
    y = torch.mul(a,b)
    print(a.requires_grad,b.requires_grad,y.requires_grad)

# flag = True
flag = False
if flag:
    w = torch.tensor([2.], requires_grad=True)
    x = torch.tensor([1.], requires_grad=True)
    a = torch.add(x,w)
    b = torch.add(w,2)
    y = torch.mul(a,b)
    w += torch.ones((1,))
    y.backward()
    print(w.grad)

    a = torch.ones((1,))
    print(id(a),a)

    # a = a + torch.ones((1,))
    # print(id(a),a)

    a += torch.ones((1,))
    print(id(a),a)