import paddle
import paddle.fluid as fluid
from paddle.fluid.dygraph.nn import Linear, Conv2D, Pool2D
import numpy as np
import os
import gzip
import json
import random
import matplotlib.pyplot as plt
from PIL import Image

# 数据集相关参数
IMG_ROWS = 28
IMG_COLS = 28
# 读入数据时用到的批次大小
BATCHSIZE = 100


# 定义数据读取器
def load_data(mode='train'):
    datafile = './data/data17168/mnist.json.gz'
    print('loading mnist dataset from {} ......'.format(datafile))
    data = json.load(gzip.open(datafile))
    print('mnist dataset load done')

    # 区分数据集
    train_set, val_set, eval_set = data
    if mode == 'train':
        # 获得训练数据集
        imgs, labels = train_set[0], train_set[1]
    elif mode == 'valid':
        imgs, labels = val_set[0], val_set[1]
    elif mode == 'eval':
        imgs, labels = eval_set[0], eval_set[1]
    else:
        raise Exception("mode can only be one of ['train', 'valid', 'eval']")
    print('数据集数量： ', len(imgs))

    # 校验数据
    imgs_length = len(imgs)
    assert len(imgs) == len(labels), "length of train_imgs({}) should be the same as train_labels({})".format(
        len(imgs), len(labels)
    )

    # 定义数据集每个数据的序号，根据序号读取数据
    index_list = list(range(imgs_length))

    # 定义数据生成器
    def data_generator():
        if mode == 'train':
            # 训练模式下打乱数据
            random.shuffle(index_list)
        imgs_list = []
        labels_list = []
        for i in index_list:
            # 将数据处理成希望的格式，比如类型为float32，shape为[1, 28, 28]
            img = np.reshape(imgs[i], [1, IMG_ROWS, IMG_COLS]).astype('float32')
            label = np.reshape(labels[i], [1]).astype('int64')
            imgs_list.append(img)
            labels_list.append(label)
            if len(imgs_list) == BATCHSIZE:
                # 获得一个batchsize的数据，并返回
                yield np.array(imgs_list), np.array(labels_list)
                # 清空数据读取列表
                imgs_list = []
                labels_list = []

        # 如果剩余数据的数目小于BATCHSIZE
        # 则剩余数据一起构成一个大小为len(imgs_list)的mini_batch
        if len(imgs_list) > 0:
            yield np.array(imgs_list), np.array(labels_list)

    return data_generator


# 定义模型结构
class MNIST(fluid.dygraph.Layer):
    def __init__(self):
        super(MNIST, self).__init__()

        # 定义卷积层，输出特征通道num_filters设置为20，卷积核的大小filter_size为5，卷积步长stride=1，padding=2
        # 激活函数使用relu
        self.conv1 = Conv2D(num_channels=1, num_filters=20, filter_size=5, stride=1, padding=2, act='relu')
        # 定义池化层，池化核pool_size=2，池化步长为2，选择最大池化方式
        self.pool1 = Pool2D(pool_size=2, pool_stride=2, pool_type='max')
        # 定义卷积层2，输出特征通道num_filters为20，卷积核大小filter_size为5，卷积步长stride=1，padding=2
        self.conv2 = Conv2D(num_channels=20, num_filters=20, filter_size=5, stride=1, padding=2, act='relu')
        # 定义池化层2，池化核pool_size=2，池化步长为2，选择最大池化方式
        self.pool2 = Pool2D(pool_size=2, pool_stride=2, pool_type='max')
        # 定义一层全连接层，输出维度是10
        self.fc = Linear(input_dim=980, output_dim=10, act='softmax')

    def forward(self, inputs, label=None, check_shape=False, check_content=False):
        outputs1 = self.conv1(inputs)
        outputs2 = self.pool1(outputs1)
        outputs3 = self.conv2(outputs2)
        outputs4 = self.pool2(outputs3)
        _outputs4 = fluid.layers.reshape(outputs4, [outputs4.shape[0], -1])
        outputs5 = self.fc(_outputs4)

        # 选择是否打印神经网络每层的参数尺寸和输出尺寸，验证网络结构是否设置正确
        if check_shape:
            # 打印每层网络设置的超参数-卷积核尺寸，卷积步长，卷积padding，池化核尺寸
            print("\n########## print network layer's superparams ##############")
            print("conv1-- kernel_size:{}, padding:{}, stride:{}".format(
                self.conv1.weight.shape, self.conv1._padding, self.conv1._stride
            ))
            print("conv2-- kernel_size:{}, padding:{}, stride:{}".format(
                self.conv2.weight.shape, self.conv2._padding, self.conv2._stride
            ))
            print("pool1-- pool_type:{}, pool_size:{}, pool_stride:{}".format(
                self.pool1._pool_type, self.pool1._pool_size, self.pool1._pool_stride
            ))
            print("pool2-- pool_type:{}, poo2_size:{}, pool_stride:{}".format(
                self.pool2._pool_type, self.pool2._pool_size, self.pool2._pool_stride
            ))
            print("fc-- weight_size:{}, bias_size_{}, activation:{}".format(
                self.fc.weight.shape, self.fc.bias.shape, self.fc._act
            ))

            # 打印每层的输出尺寸
            print("\n########## print shape of features of every layer ###############")
            print("inputs_shape: {}".format(inputs.shape))
            print("outputs1_shape: {}".format(outputs1.shape))
            print("outputs2_shape: {}".format(outputs2.shape))
            print("outputs3_shape: {}".format(outputs3.shape))
            print("outputs4_shape: {}".format(outputs4.shape))
            print("outputs5_shape: {}".format(outputs5.shape))

        # 选择是否打印训练过程中的参数和输出内容，可用于训练过程中的调试
        if check_content:
            # 打印卷积层的参数-卷积核权重，权重参数较多，此处只打印部分参数
            print("\n########## print convolution layer's kernel ###############")
            print("conv1 params -- kernel weights:", self.conv1.weight[0][0])
            print("conv2 params -- kernel weights:", self.conv2.weight[0][0])

            # 创建随机数，随机打印某一个通道的输出值
            idx1 = np.random.randint(0, outputs1.shape[1])
            idx2 = np.random.randint(0, outputs3.shape[1])
            # 打印卷积-池化后的结果，仅打印batch中第一个图像对应的特征
            print("\nThe {}th channel of conv1 layer: ".format(idx1), outputs1[0][idx1])
            print("The {}th channel of conv2 layer: ".format(idx2), outputs3[0][idx2])
            print("The output of last layer:", outputs5[0], '\n')

        # 如果label不是None，则计算分类精度并返回
        if label is not None:
            acc = fluid.layers.accuracy(input=outputs5, label=label)
            return outputs5, acc
        else:
            return outputs5


use_gpu = False
place = fluid.CUDAPlace(0) if use_gpu else fluid.CPUPlace()

with fluid.dygraph.guard(place):
    model = MNIST()
    model.train()

    # 调用加载数据的函数，获得MNIST训练数据集
    train_loader = load_data()
    # 四种优化算法
    # optimizer = fluid.optimizer.SGDOptimizer(learning_rate=0.01, parameter_list=model.parameters())
    # optimizer = fluid.optimizer.MomentumOptimizer(learning_rate=0.01, momentum=0.9, parameter_list=model.parameters())
    # optimizer = fluid.optimizer.AdagradOptimizer(learning_rate=0.01, parameter_list=model.parameters())
    optimizer = fluid.optimizer.AdamOptimizer(learning_rate=0.01, parameter_list=model.parameters())

    EPOCH_NUM = 1
    for epoch_id in range(EPOCH_NUM):
        for batch_id, data in enumerate(train_loader()):
            image_data, label_data = data
            image = fluid.dygraph.to_variable(image_data)
            label = fluid.dygraph.to_variable(label_data)

            # 前向计算的过程，同时拿到模型输出值和分类准确率
            if batch_id == 0 and epoch_id == 0:
                # 打印模型参数和每层输出的尺寸
                predict, acc = model(image, label, check_shape=True, check_content=False)
            elif batch_id == 401:
                # 打印模型参数和每层输出的值
                predict, acc = model(image, label, check_shape=False, check_content=True)
            else:
                predict, acc = model(image, label)

            # 计算损失
            loss = fluid.layers.cross_entropy(predict, label)
            avg_loss = fluid.layers.mean(loss)

            # 每训练了200批次的数据，打印下当前Loss的情况
            if batch_id % 200 == 0:
                print("epoch: {}, batch: {}, loss is: {}, acc is {}".format(epoch_id, batch_id, avg_loss.numpy(),
                                                                            acc.numpy()))

            # 后向传播，更新参数的过程
            avg_loss.backward()
            optimizer.minimize(avg_loss)
            model.clear_gradients()

    fluid.save_dygraph(model.state_dict(), 'mnist')
    print("Model has been saved.")


with fluid.dygraph.guard():
    # 加载模型参数
    model = MNIST()
    model_state_dict, _ = fluid.load_dygraph('mnist')
    model.load_dict(model_state_dict)

    model.eval()
    eval_loader = load_data('eval')

    acc_set = []
    avg_loss_set = []
    for batch_id, data in enumerate(eval_loader()):
        x_data, y_data = data
        img = fluid.dygraph.to_variable(x_data)
        label = fluid.dygraph.to_variable(y_data)
        prediction, acc = model(img, label)
        loss = fluid.layers.cross_entropy(input=prediction, label=label)
        avg_loss = fluid.layers.mean(loss)
        acc_set.append(float(acc.numpy()))
        avg_loss_set.append(float(avg_loss.numpy()))

    # 计算多个batch的平均损失和准确率
    acc_val_mean = np.array(acc_set).mean()
    avg_loss_val_mean = np.array(avg_loss_set).mean()
    print('loss={}, acc={}'.format(avg_loss_val_mean, acc_val_mean))


with fluid.dygraph.guard():
    model = MNIST()
    model.train()

    # 各种优化算法都可以加入正则化项，避免过拟合，参数regularization_coeff调节正则化项的权重
    # optimizer = fluid.optimizer.SGDOptimizer(learning_rate=0.01, regularization=fluid.regularizer.L2Decay(regularization_coeff=0.1), parameter_list=model.parameters())
    optimizer = fluid.optimizer.AdamOptimizer(
        learning_rate=0.01,
        regularization=fluid.regularizer.L2Decay(regularization_coeff=0.1),
        parameter_list=model.parameters()
    )

    EPOCH_NUM = 10
    iter = 0
    iters = []
    losses = []
    for epoch_id in range(EPOCH_NUM):
        for batch_id, data in enumerate(train_loader()):
            image_data, label_data = data
            image = fluid.dygraph.to_variable(image_data)
            label = fluid.dygraph.to_variable(label_data)

            predict, acc = model(image, label)
            loss = fluid.layers.cross_entropy(predict, label)
            avg_loss = fluid.layers.mean(loss)

            if batch_id % 100 == 0:
                print("epoch: {}, batch: {}, loss is: {}, acc is {}".format(epoch_id, batch_id, avg_loss.numpy(), acc.numpy()))
                iters.append(iter)
                losses.append(avg_loss.numpy())
                iter = iter + 100
            avg_loss.backward()
            optimizer.minimize(avg_loss)
            model.clear_gradients()

    fluid.save_dygraph(model.state_dict(), 'mnist')


plt.figure()
plt.title("train loss", fontsize=24)
plt.xlabel("iter", fontsize=14)
plt.ylabel("loss", fontsize=14)
plt.plot(iters, losses, color='red', label='train loss')
plt.grid()
plt.show()
