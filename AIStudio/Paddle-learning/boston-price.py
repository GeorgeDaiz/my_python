import numpy as np
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph


max_values = []
min_values = []
avg_values = []


def load_data():
    # 导入数据
    datafile = './data/housing.data'
    data = np.fromfile(datafile, sep=' ')
    feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
                     'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    feature_num = len(feature_names)

    # 将原始数据reshape，变成[N, 14]
    data = data.reshape([data.shape[0] // feature_num, feature_num])

    # 将原始数据集拆分成训练集和测试集
    # 80%做训练，20%做测试，训练和测试必须是没有交集的
    ratio = 0.8
    offset = int(data.shape[0] * ratio)
    training_data = data[:offset]

    # 计算训练集的最大、最小、平均值
    maximums, minimums, avgs = training_data.max(axis=0), training_data.min(axis=0), \
                               training_data.sum(axis=0) / training_data.shape[0]

    # 记录数据的归一化参数，在预测时对数据做归一化
    global max_values
    global min_values
    global avg_values
    max_values = maximums
    min_values = minimums
    avg_values = avgs

    # 对数据进行归一化处理
    for i in range(feature_num):
        data[:, i] = (data[:, i] - avgs[i]) / (maximums[i] - minimums[i])

    # 训练集和测试集的划分比例
    training_data = data[: offset]
    test_data = data[offset:]
    return training_data, test_data


class Network:
    def __init__(self, num_of_weights):
        # 产生随机的w初始值
        # 为了保持程序运行结果一致性，设置随机数种子
        self.w = np.random.randn(num_of_weights, 1)
        self.b = 0.

    def forward(self, x):
        z = np.dot(x, self.w) + self.b
        return z

    def loss(self, z, y):
        error = z - y
        num_samples = error.shape[0]
        cost = error * error
        cost = np.sum(cost) / num_samples
        return cost

    def gradient(self, x, y):
        z = self.forward(x)
        N = x.shape[0]
        gradient_w = 1. / N * np.sum((z - y) * x, axis=0)
        gradient_w = gradient_w[:, np.newaxis]
        gradient_b = 1. / N * np.sum(z - y)
        return gradient_w, gradient_b

    def update(self, gradient_w, gradient_b, eta=0.01):
        self.w = self.w - eta * gradient_w
        self.b = self.b - eta * gradient_b

    def train(self, training_data, num_epoches, batch_size=10, eta=0.01):
        n = len(training_data)
        losses = []
        for epoch_id in range(num_epoches):
            # 迭代前打乱训练数据顺序
            np.random.shuffle(training_data)
            mini_batches = [training_data[k: k + batch_size] for k in range(0, n, batch_size)]
            for iter_id, mini_batch in enumerate(mini_batches):
                x = mini_batch[:, : -1]
                y = mini_batch[:, -1:]
                a = self.forward(x)
                loss = self.loss(a, y)
                gradient_w, gradient_b = self.gradient(x, y)
                self.update(gradient_w, gradient_b, eta)
                losses.append(loss)
                print('Epoch {:3d} / iter {:3d}, loss = {:.4f}'.
                      format(epoch_id, iter_id, loss))
        return losses


def test1():
    # 获取数据
    train_data, test_data = load_data()

    # 创建网络
    net = Network(13)
    # 启动训练
    losses = net.train(train_data, num_epoches=50, batch_size=100, eta=0.1)

    # 画出损失函数的变化趋势
    plot_x = np.arange(len(losses))
    plot_y = np.array(losses)
    plt.plot(plot_x, plot_y)
    plt.show()


class Regressor(fluid.dygraph.Layer):
    def __init__(self):
        super(Regressor, self).__init__()

        # 定义一层全连接层，输出维度是1，激活函数为None
        self.fc = dygraph.Linear(input_dim=13, output_dim=1, act=None)

    def forward(self, inputs):
        x = self.fc(inputs)
        return x


# 定义paddle动态图工作环境
with fluid.dygraph.guard():
    # 声明定义好的线性回归模型
    model = Regressor()
    model.train()
    # 加载数据
    training_data, test_data = load_data()
    # 定义优化算法
    opt = fluid.optimizer.SGD(learning_rate=0.01, parameter_list=model.parameters())

with dygraph.guard(fluid.CPUPlace()):
    EPOCH_NUM = 10
    BATCH_SIZE = 10

    # 外层循环
    for epoch_id in range(EPOCH_NUM):
        np.random.shuffle(training_data)
        mini_batches = [training_data[k: k + BATCH_SIZE] for k in range(0, len(training_data), BATCH_SIZE)]
        # 内层循环
        for iter_id, mini_batch in enumerate(mini_batches):
            x = np.array(mini_batch[:, : -1]).astype('float32')
            y = np.array(mini_batch[:, -1:]).astype('float32')

            # 将numpy数据转为paddle动态图variable
            house_features = dygraph.to_variable(x)
            prices = dygraph.to_variable(y)

            # 前向计算
            predicts = model(house_features)

            loss = fluid.layers.square_error_cost(predicts, label=prices)
            avg_loss = fluid.layers.mean(loss)
            if iter_id % 20 == 0:
                print("epoch: {}, iter: {}, loss is: {}".format(epoch_id, iter_id, avg_loss.numpy()))

            # 反向传播
            avg_loss.backward()
            opt.minimize(avg_loss)
            model.clear_gradients()
    # 保存模型
    fluid.save_dygraph(model.state_dict(), 'LR_model')


def load_one_example(data_dir):
    f = open(data_dir, 'r')
    datas = f.readlines()

    tmp = datas[-10]
    tmp = tmp.strip().split()
    one_data = [float(v) for v in tmp]

    # 归一化处理
    for i in range(len(one_data) - 1):
        one_data[i] = (one_data[i] - avg_values[i] / max_values[i] - min_values[i])

    data = np.reshape(np.array(one_data[: -1]), [1, -1]).astype(np.float32)
    label = one_data[-1]
    return data, label


with dygraph.guard():
    # 参数为保存模型参数的文件地址
    model_dict, _ = fluid.load_dygraph('LR_model')
    model.load_dict(model_dict)
    model.eval()

    test_data, label = load_one_example('./data/data16317/housing.data')
    test_data = dygraph.to_variable(test_data)
    results = model(test_data)

    # 对结果做反归一化处理
    results = results * (max_values[-1] - min_values[-1]) + avg_values[-1]
    print("Inference result is {}, the corresponding label is {}".format(results.numpy(), label))
