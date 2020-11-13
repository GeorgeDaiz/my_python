import random
import numpy as np
from PIL import Image
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph
from paddle.fluid.dygraph import Linear, Embedding, Conv2D
import pickle
import os
"""==========数据读取与处理=========="""


# 数据读取网络
class MovieLen(object):
    def __init__(self, use_poster: bool):
        self.use_poster = use_poster
        # 声明每个数据文件的路径
        usr_info_path = '.'+os.sep+'work'+os.sep+'ml-1m'+os.sep+'users.dat'
        if use_poster:
            rating_path = '.'+os.sep+'work'+os.sep+'ml-1m'+os.sep+'new_rating.txt'
        else:
            rating_path = '.'+os.sep+'work'+os.sep+'ml-1m'+os.sep+'ratings.dat'

        movie_info_path = '.'+os.sep+'work'+os.sep+'ml-1m'+os.sep+'movies.dat'
        self.poster_path = '.'+os.sep+'work'+os.sep+'ml-1m'+os.sep+'posters'
        # 得到电影数据
        self.movie_info, self.movie_cat, self.movie_title = self.get_movie_info(movie_info_path)
        # 记录电影的最大ID
        self.max_mov_cat = np.max([self.movie_cat[k] for k in self.movie_cat])
        self.max_mov_tit = np.max([self.movie_title[k] for k in self.movie_title])
        self.max_mov_id = np.max(list(map(int, self.movie_info.keys())))
        # 记录用户数据的最大ID
        self.max_usr_id = 0
        self.max_usr_age = 0
        self.max_usr_job = 0
        # 得到用户数据
        self.usr_info = self.get_usr_info(usr_info_path)
        # 得到评分数据
        self.rating_info = self.get_rating_info(rating_path)
        # 构建数据集 
        self.dataset = self.get_dataset(usr_info=self.usr_info,
                                        rating_info=self.rating_info,
                                        movie_info=self.movie_info)
        # 划分数据集，获得数据加载器
        self.train_dataset = self.dataset[:int(len(self.dataset) * 0.9)]
        self.valid_dataset = self.dataset[int(len(self.dataset) * 0.9):]
        print("##Total dataset instances: ", len(self.dataset))
        print("##MovieLens dataset information: \nusr num: {}\n"
              "movies num: {}".format(len(self.usr_info), len(self.movie_info)))

    # 得到电影数据
    def get_movie_info(self, path):
        # 打开文件，编码方式选择ISO-8859-1，读取所有数据到data中 
        with open(path, 'r', encoding="ISO-8859-1") as f:
            data = f.readlines()
        # 建立三个字典，分别用户存放电影所有信息，电影的名字信息、类别信息
        movie_info, movie_titles, movie_cat = {}, {}, {}
        # 对电影名字、类别中不同的单词计数
        t_count, c_count = 1, 1

        # 按行读取数据并处理
        for item in data:
            item = item.strip().split("::")
            v_id = item[0]
            v_title = item[1][:-7]
            cats = item[2].split('|')
            v_year = item[1][-5:-1]

            titles = v_title.split()
            # 统计电影名字的单词，并给每个单词一个序号，放在movie_titles中
            for t in titles:
                if t not in movie_titles:
                    movie_titles[t] = t_count
                    t_count += 1
            # 统计电影类别单词，并给每个单词一个序号，放在movie_cat中
            for cat in cats:
                if cat not in movie_cat:
                    movie_cat[cat] = c_count
                    c_count += 1
            # 补0使电影名称对应的列表长度为15
            v_tit = [movie_titles[k] for k in titles]
            while len(v_tit) < 15:
                v_tit.append(0)
            # 补0使电影种类对应的列表长度为6
            v_cat = [movie_cat[k] for k in cats]
            while len(v_cat) < 6:
                v_cat.append(0)
            # 保存电影数据到movie_info中
            movie_info[v_id] = {'mov_id': int(v_id),
                                'title': v_tit,
                                'category': v_cat,
                                'years': int(v_year)}
        return movie_info, movie_cat, movie_titles

    def get_usr_info(self, path):
        # 性别转换函数，M-0， F-1
        def gender2num(gender):
            return 1 if gender == 'F' else 0

        # 打开文件，读取所有行到data中
        with open(path, 'r') as f:
            data = f.readlines()
        # 建立用户信息的字典
        use_info = {}

        # 按行索引数据
        for item in data:
            # 去除每一行中和数据无关的部分
            item = item.strip().split("::")
            usr_id = item[0]
            # 将字符数据转成数字并保存在字典中
            use_info[usr_id] = {'usr_id': int(usr_id),
                                'gender': gender2num(item[1]),
                                'age': int(item[2]),
                                'job': int(item[3])}
            self.max_usr_id = max(self.max_usr_id, int(usr_id))
            self.max_usr_age = max(self.max_usr_age, int(item[2]))
            self.max_usr_job = max(self.max_usr_job, int(item[3]))
        return use_info

    # 得到评分数据
    def get_rating_info(self, path):
        # 读取文件里的数据
        with open(path, 'r') as f:
            data = f.readlines()
        # 将数据保存在字典中并返回
        rating_info = {}
        for item in data:
            item = item.strip().split("::")
            usr_id, movie_id, score = item[0], item[1], item[2]
            if usr_id not in rating_info.keys():
                rating_info[usr_id] = {movie_id: float(score)}
            else:
                rating_info[usr_id][movie_id] = float(score)
        return rating_info

    # 构建数据集
    def get_dataset(self, usr_info, rating_info, movie_info):
        trainset = []
        for usr_id in rating_info.keys():
            usr_ratings = rating_info[usr_id]
            for movie_id in usr_ratings:
                trainset.append({'usr_info': usr_info[usr_id],
                                 'mov_info': movie_info[movie_id],
                                 'scores': usr_ratings[movie_id]})
        return trainset

    def load_data(self, dataset=None, mode='train'):
        use_poster = False

        # 定义数据迭代Batch大小
        BATCHSIZE = 256

        data_length = len(dataset)
        index_list = list(range(data_length))

        # 定义数据迭代加载器
        def data_generator():
            # 训练模式下，打乱训练数据
            if mode == 'train':
                random.shuffle(index_list)
            # 声明每个特征的列表
            usr_id_list, usr_gender_list, usr_age_list, usr_job_list = [], [], [], []
            mov_id_list, mov_tit_list, mov_cat_list, mov_poster_list = [], [], [], []
            score_list = []
            # 索引遍历输入数据集
            for idx, i in enumerate(index_list):
                # 获得特征数据保存到对应特征列表中
                usr_id_list.append(dataset[i]['usr_info']['usr_id'])
                usr_gender_list.append(dataset[i]['usr_info']['gender'])
                usr_age_list.append(dataset[i]['usr_info']['age'])
                usr_job_list.append(dataset[i]['usr_info']['job'])

                mov_id_list.append(dataset[i]['mov_info']['mov_id'])
                mov_tit_list.append(dataset[i]['mov_info']['title'])
                mov_cat_list.append(dataset[i]['mov_info']['category'])
                mov_id = dataset[i]['mov_info']['mov_id']

                if use_poster:
                    # 不使用图像特征时，不读取图像数据，加快数据读取速度
                    poster = Image.open(self.poster_path + 'mov_id{}.jpg'.format(str(mov_id[0])))
                    poster = poster.resize([64, 64])
                    if len(poster.size) <= 2:
                        poster = poster.convert("RGB")

                    mov_poster_list.append(np.array(poster))

                score_list.append(int(dataset[i]['scores']))
                # 如果读取的数据量达到当前的batch大小，就返回当前批次
                if len(usr_id_list) == BATCHSIZE:
                    # 转换列表数据为数组形式，reshape到固定形状
                    usr_id_arr = np.array(usr_id_list)
                    usr_gender_arr = np.array(usr_gender_list)
                    usr_age_arr = np.array(usr_age_list)
                    usr_job_arr = np.array(usr_job_list)

                    mov_id_arr = np.array(mov_id_list)
                    mov_cat_arr = np.reshape(np.array(mov_cat_list), [BATCHSIZE, 6]).astype(np.int64)
                    mov_tit_arr = np.reshape(np.array(mov_tit_list), [BATCHSIZE, 1, 15]).astype(np.int64)

                    if use_poster:
                        mov_poster_arr = np.reshape(np.array(mov_poster_list) / 127.5 - 1,
                                                    [BATCHSIZE, 3, 64, 64]).astype(np.float32)
                    else:
                        mov_poster_arr = np.array([0.])

                    scores_arr = np.reshape(np.array(score_list), [-1, 1]).astype(np.float32)

                    # 放回当前批次数据
                    yield [usr_id_arr, usr_gender_arr, usr_age_arr, usr_job_arr], \
                          [mov_id_arr, mov_cat_arr, mov_tit_arr, mov_poster_arr], scores_arr

                    # 清空数据
                    usr_id_list, usr_gender_list, usr_age_list, usr_job_list = [], [], [], []
                    mov_id_list, mov_tit_list, mov_cat_list, score_list = [], [], [], []
                    mov_poster_list = []

        return data_generator


# 声明数据读取类
dataset = MovieLen(False)
# 定义数据读取器
train_loader = dataset.load_data(dataset=dataset.train_dataset, mode='train')
# 迭代的读取数据， Batchsize = 256
for idx, data in enumerate(train_loader()):
    usr, mov, score = data
    print("打印用户ID，性别，年龄，职业数据的维度：")
    for v in usr:
        print(v.shape)
    print("打印电影ID，名字，类别数据的维度：")
    for v in mov:
        print(v.shape)

    break

"""==========模型设计=========="""


# 用户特征提取网络
class MovModel(dygraph.layers.Layer):
    def __init__(self, use_poster, use_mov_title, use_mov_cat, use_age_job):
        super(MovModel, self).__init__()

        # 将传入的name信息和bool型参数添加到模型类中
        self.use_mov_poster = use_poster
        self.use_mov_title = use_mov_title
        self.use_age_job = use_age_job
        self.use_mov_cat = use_mov_cat

        # 获取数据集的信息，并构建训练和验证集的数据迭代器
        Dataset = MovieLen(self.use_mov_poster)
        self.Dataset = Dataset
        self.trainset = self.Dataset.train_dataset
        self.valset = self.Dataset.valid_dataset
        self.train_loader = self.Dataset.load_data(dataset=self.trainset, mode='train')
        self.valid_loader = self.Dataset.load_data(dataset=self.valset, mode='valid')

        """define network layer for embedding usr info"""
        USR_ID_NUM = Dataset.max_usr_id + 1
        # 对用户ID做映射，并紧接着一个Linear层
        self.usr_emb = Embedding([USR_ID_NUM, 32], is_sparse=False)
        self.usr_fc = Linear(32, 32)

        # 对用户性别信息做映射
        USR_GENDER_DICT_SIZE = 2
        self.usr_gender_emb = Embedding([USR_GENDER_DICT_SIZE, 16])
        self.usr_gender_fc = Linear(16, 16)

        # 用户年龄
        USR_AGE_DICT_SIZE = Dataset.max_usr_age + 1
        self.usr_age_emb = Embedding([USR_AGE_DICT_SIZE, 16])
        self.usr_age_fc = Linear(16, 16)

        # 用户职业信息
        USR_JOB_DICT_SIZE = Dataset.max_usr_job + 1
        self.usr_job_emb = Embedding([USR_JOB_DICT_SIZE, 16])
        self.usr_job_fc = Linear(16, 16)

        # 新建一个Linear层，整合用户数据信息
        self.usr_combined = Linear(80, 200, act='tanh')

        """define network layer for embedding mov info"""
        # 电影ID信息
        MOV_DICT_SIZE = Dataset.max_mov_id + 1
        self.mov_emb = Embedding([MOV_DICT_SIZE, 32])
        self.mov_fc = Linear(32, 32)

        # 电影类别信息
        CATEGORY_DICT_SIZE = len(Dataset.movie_cat) + 1
        self.mov_cat_emb = Embedding([CATEGORY_DICT_SIZE, 32], is_sparse=False)
        self.mov_cat_fc = Linear(32, 32)

        # 电影名称
        MOV_TITLE_DICT_SIZE = Dataset.max_mov_tit + 1
        self.mov_title_emb = Embedding([MOV_TITLE_DICT_SIZE, 32], is_sparse=False)
        self.mov_title_conv = Conv2D(1, 1, filter_size=(3, 1), stride=(2, 1), padding=0, act='relu')
        self.mov_title_conv2 = Conv2D(1, 1, filter_size=(3, 1), stride=1, padding=0, act='relu')

        # 新建一个FC层，整合电影特征
        self.mov_concat_embed = Linear(96, 200, act='tanh')

    # 定义计算用户特征的前向运算过程
    def get_usr_feat(self, usr_var):
        """get usr feature"""
        usr_id, usr_gender, usr_age, usr_job = usr_var
        # 将用户的ID数据经过embedding和Linear计算，得到的特征保存在feats_collect中
        feats_collect = []
        usr_id = self.usr_emb(usr_id)
        usr_id = self.usr_fc(usr_id)
        usr_id = fluid.layers.relu(usr_id)
        feats_collect.append(usr_id)

        # 计算用户的性别特征，并保存在feats_collect中
        usr_gender = self.usr_gender_emb(usr_gender)
        usr_gender = self.usr_gender_fc(usr_gender)
        usr_gender = fluid.layers.relu(usr_gender)
        feats_collect.append(usr_gender)

        # 选择是否使用用户的年龄-职业特征
        if self.use_age_job:
            usr_age = self.usr_age_emb(usr_age)
            usr_age = self.usr_age_fc(usr_age)
            usr_age = fluid.layers.relu(usr_age)
            feats_collect.append(usr_age)
            usr_job = self.usr_job_emb(usr_job)
            usr_job = self.usr_job_fc(usr_job)
            usr_job = fluid.layers.relu(usr_job)
            feats_collect.append(usr_job)

        # 将用户的特征级联，并通过Linear层得到最终的用户特征
        usr_feat = fluid.layers.concat(feats_collect, axis=1)
        usr_feat = self.usr_combined(usr_feat)
        return usr_feat

    # 定义电影特征的前向计算过程
    def get_mov_feat(self, mov_var):
        """get movie features"""
        # 获得电影数据
        mov_id, mov_cat, mov_title, mov_poster = mov_var
        feats_collect = []
        # 获得batchsize大小
        batch_size = mov_id.shape[0]
        # 计算电影ID的特征，并存在feats_collect中
        mov_id = self.mov_emb(mov_id)
        mov_id = self.mov_fc(mov_id)
        mov_id = fluid.layers.relu(mov_id)
        feats_collect.append(mov_id)

        if self.use_mov_cat:
            # 计算电影种类的特征映射
            mov_cat = self.mov_cat_emb(mov_cat)
            mov_cat = fluid.layers.reduce_sum(mov_cat, dim=1, keep_dim=False)
            mov_cat = self.mov_cat_fc(mov_cat)
            feats_collect.append(mov_cat)

        if self.use_mov_title:
            # 计算电影名字的特征映射
            mov_title = self.mov_title_emb(mov_title)
            mov_title = self.mov_title_conv2(self.mov_title_conv(mov_title))
            mov_title = fluid.layers.reduce_sum(mov_title, dim=2, keep_dim=False)
            mov_title = fluid.layers.relu(mov_title)
            mov_title = fluid.layers.reshape(mov_title, [batch_size, -1])
            feats_collect.append(mov_title)

        # 使用一个全连接层，整合所有电影特征，映射为一个200维的特征向量
        mov_feat = fluid.layers.concat(feats_collect, axis=1)
        mov_feat = self.mov_concat_embed(mov_feat)
        return mov_feat

    # 定义个性化推荐算法的前向计算
    def forward(self, usr_var, mov_var):
        usr_feat = self.get_usr_feat(usr_var)
        mov_feat = self.get_mov_feat(mov_var)
        res = fluid.layers.cos_sim(usr_feat, mov_feat)
        res = fluid.layers.scale(res, scale=5)
        return usr_feat, mov_feat, res


"""==========模型训练与特征保存=========="""


def train(model):
    # 配置训练参数
    use_gpu = True
    lr = 0.01
    Epoches = 10

    place = fluid.CUDAPlace(0) if use_gpu else fluid.CPUPlace()
    with fluid.dygraph.guard(place):
        # 启动训练
        model.train()
        # 获得数据读取器
        data_loader = model.train_loader
        # 使用adam优化器，学习率使用0.01
        opt = fluid.optimizer.Adam(learning_rate=lr, parameter_list=model.parameters())

        for epoch in range(0, Epoches):
            for idx, data in enumerate(data_loader()):
                # 获得数据，并转为动态图格式
                usr, mov, score = data
                usr_v = [dygraph.to_variable(var) for var in usr]
                mov_v = [dygraph.to_variable(var) for var in mov]
                scores_label = dygraph.to_variable(score)
                # 计算出算法的前向计算结果
                _, _, scores_predict = model(usr_v, mov_v)
                # 计算loss
                loss = fluid.layers.square_error_cost(scores_predict, scores_label)
                avg_loss = fluid.layers.mean(loss)
                if idx % 500 == 0:
                    print("epoch: {}, batch_id: {}, loss is: {}".format(epoch, idx, avg_loss.numpy()))

                # 损失函数下降，并清除梯度
                avg_loss.backward()
                opt.minimize(avg_loss)
                model.clear_gradients()
            # 每个epoch 保存一次模型
            fluid.save_dygraph(model.state_dict(), '.'+os.sep+'checkpoint'+os.sep+'epoch' + str(epoch))


# 启动训练
with dygraph.guard():
    use_poster, use_mov_title, use_mov_cat, use_age_job = False, True, True, True
    model = MovModel(use_poster, use_mov_title, use_mov_cat, use_age_job)
    train(model)


# 评估指标
def evaluation(model, params_file_path):
    use_gpu = False
    place = fluid.CUDAPlace(0) if use_gpu else fluid.CPUPlace()

    with fluid.dygraph.guard(place):
        model_state_dict, _ = fluid.load_dygraph(params_file_path)
        model.load_dict(model_state_dict)
        model.eval()

        acc_set = []
        avg_loss_set = []
        for idx, data in enumerate(model.valid_loader()):
            usr, mov, score_label = data
            usr_v = [dygraph.to_variable(var) for var in usr]
            mov_v = [dygraph.to_variable(var) for var in mov]

            _, _, scores_predict = model(usr_v, mov_v)

            pred_scores = scores_predict.numpy()

            avg_loss_set.append(np.mean(np.abs(pred_scores - score_label)))

            diff = np.abs(pred_scores - score_label)
            diff[diff > 0.5] = 1
            acc = 1 - np.mean(diff)
            acc_set.append(acc)
        return np.mean(acc_set), np.mean(avg_loss_set)


param_path = '.'+os.sep+'checkpoint'+os.sep+'epoch'
for i in range(10):
    acc, mae = evaluation(model, param_path+str(i))
    print("ACC:", acc, "MAE:", mae)


def get_usr_mov_features(model, params_file_path, poster_path=None):
    use_gpu = False
    place = fluid.CUDAPlace(0) if use_gpu else fluid.CPUPlace()
    usr_pkl = {}
    mov_pkl = {}

    # 定义将list中每个元素转为variable的函数
    def list2variable(inputs, shape):
        inputs = np.reshape(np.array(inputs).astype(np.int64), shape)
        return fluid.dygraph.to_variable(inputs)

    with fluid.dygraph.guard(place):
        # 加载模型参数到模型中，设置为验证模式eval()
        model_state_dict, _ = fluid.load_dygraph(params_file_path)
        model.load_dict(model_state_dict)
        model.eval()
        # 获得整个数据集的数据
        dataset = model.Dataset.dataset

        for i in range(len(dataset)):
            # 获得用户数据、电影数据、评分数据
            # 本案例只转换所有在样本中出现过的user和movie，实际中可以使用业务系统中的全量数据
            usr_info, mov_info, score = dataset[i]['usr_info'], dataset[i]['mov_info'], dataset[i]['scores']
            usrid = str(usr_info['usr_id'])
            movid = str(mov_info['mov_id'])

            # 获得用户数据，计算得到用户特征，保存在usr_pkl字典中
            if usrid not in usr_pkl.keys():
                usr_id_v = list2variable(usr_info['usr_id'], [1])
                usr_age_v = list2variable(usr_info['age'], [1])
                usr_gender_v = list2variable(usr_info['gender'], [1])
                usr_job_v = list2variable(usr_info['job'], [1])

                usr_in = [usr_id_v, usr_gender_v, usr_age_v, usr_job_v]
                usr_feat = model.get_usr_feat(usr_in)

                usr_pkl[usrid] = usr_feat.numpy()

            # 获得电影数据，计算得到电影特征，保存在mov_pkl字典中
            if movid not in mov_pkl.keys():
                mov_id_v = list2variable(mov_info['mov_id'], [1])
                mov_cat_v = list2variable(mov_info['category'], [1, 6])
                mov_tit_v = list2variable(mov_info['title'], [1, 1, 15])
                mov_in = [mov_id_v, mov_cat_v, mov_tit_v, None]
                mov_feat = model.get_mov_feat(mov_in)
                mov_pkl[movid] = mov_feat.numpy()

    print(len(mov_pkl.keys()))
    # 保存特征到本地
    pickle.dump(usr_pkl, open('.'+os.sep+'usr_feat.pkl', 'wb'))
    pickle.dump(mov_pkl, open('.'+os.sep+'mov_feat.pkl', 'wb'))
    print('usr and mov features has been saved')


param_path = '.'+os.sep+'checkpoint'+os.sep+'epoch7'
# poster_path = '.'+os.sep+'work'+os.sep+'ml-1m'+os.sep+'posters'
get_usr_mov_features(model, param_path)


"""==========电影推荐=========="""
mov_feat_dir = 'mov_feat.pkl'
usr_feat_dir = 'usr_feat.pkl'

usr_feats = pickle.load(open(usr_feat_dir, 'rb'))
mov_feats = pickle.load(open(mov_feat_dir, 'rb'))
usr_id = 2
usr_feat = usr_feats[str(usr_id)]

mov_id = 1
# 通过电影ID索引到电影特征
mov_feat = mov_feats[str(mov_id)]

movie_data_path = '.'+os.sep+'work'+os.sep+'ml-1m'+os.sep+'movies.dat'
mov_info = {}
# 打开电影数据文件，根据电影ID索引到电影信息
with open(movie_data_path, 'r', encoding='ISO-8859-1') as f:
    data = f.readlines()
    for item in data:
        item = item.strip().split('::')
        mov_info[str(item[0])] = item

usr_file = '.'+os.sep+'work'+os.sep+'ml-1m'+os.sep+'users.dat'
usr_info = {}
with open(usr_file, 'r') as f:
    data = f.readlines()
    for item in data:
        item = item.strip().split('::')
        usr_info[str(item[0])] = item

print("当前的用户是：")
print("usr_id:", usr_id, usr_info[str(usr_id)])
print("对应的特征是：", usr_feats[str(usr_id)])

print("\n当前电影是：")
print("mov_id:", mov_id, mov_info[str(mov_id)])
print("对应的特征是：")
print(mov_feat)


# 定义根据用户兴趣推荐电影
def recommend_mov_for_usr(usr_id, top_k, pick_num, usr_feat_dir, mov_feat_dir, mov_info_path):
    assert pick_num <= top_k
    # 读取电影和用户特征
    usr_feats = pickle.load(open(usr_feat_dir, 'rb'))
    mov_feats = pickle.load(open(mov_feat_dir, 'rb'))
    usr_feat = usr_feats[str(usr_id)]

    cos_sims = []
    with dygraph.guard():
        # 索引电影特征，计算和输入用户ID的特征的相似度
        for idx, key in enumerate(mov_feats.keys()):
            mov_feat = mov_feats[key]
            usr_feat = dygraph.to_variable(usr_feat)
            mov_feat = dygraph.to_variable(mov_feat)
            sim = fluid.layers.cos_sim(usr_feat, mov_feat)
            cos_sims.append(sim.numpy()[0][0])
    # 对相似度排序
    index = np.argsort(cos_sims)[-top_k:]

    mov_info = {}
    # 读取电影文件里的数据，根据电影ID索引到电影信息
    with open(mov_info_path, 'r', encoding='ISO-8859-1') as f:
        data = f.readlines()
        for item in data:
            item = item.strip().split('::')
            mov_info[str(item[0])] = item

    print("当前的用户是：")
    print("usr_id:", usr_id)
    print("推荐可能喜欢的电影是：")
    res = []

    # 加入随机选择因素，确保每次推荐的都不一样
    while len(res) < pick_num:
        val = np.random.choice(len(index), 1)[0]
        idx = index[val]
        mov_id = list(mov_feats.keys())[idx]
        if mov_id not in res:
            res.append(mov_id)

    for id in res:
        print('mov_id: ', id, mov_info[str(id)])


top_k, pick_num = 10, 6
usr_id = 2
recommend_mov_for_usr(usr_id, top_k, pick_num, 'usr_feat.pkl', 'mov_feat.pkl', movie_data_path)


# 给定一个用户ID，找到评分最高的topk个电影
usr_a = 2
topk = 10
rating_path = '.'+os.sep+'work'+os.sep+'ml-1m'+os.sep+'ratings.dat'
with open(rating_path, 'r') as f:
    ratings_data = f.readlines()

usr_rating_info = {}
for item in ratings_data:
    item = item.strip().split('::')
    usr_id, mov_id, score = item[0], item[1], item[2]
    if usr_id == str(usr_a):
        usr_rating_info[mov_id] = float(score)

# 获得评分过的电影ID
movie_ids = list(usr_rating_info.keys())
print("ID为 {} 的用户，评分过的电影数量是: ".format(usr_a), len(movie_ids))

# 选出ID为usr_a评分最高的前topk个电影
ratings_topk = sorted(usr_rating_info.items(), key=lambda item: item[1])[-topk:]
movie_info_path = '.'+os.sep+'work'+os.sep+'ml-1m'+os.sep+'movies.dat'
with open(movie_info_path, 'r', encoding='ISO-8859-1') as f:
    data = f.readlines()

movie_info = {}
for item in data:
    item = item.strip().split('::')
    # 获得电影的ID信息
    v_id = item[0]
    movie_info[v_id] = item

for k, score in ratings_topk:
    print('电影ID：{}， 评分是：{}， 电影信息：{}'.format(k, score, movie_info[k]))


# 根据相似用户推荐电影
def recommend_mov_by_usr_base(usr_id, top_k, pick_num, usr_feat_dir, mov_feat_dir, mov_info_path):
    assert pick_num < top_k
    # 读取电影和用户特征
    usr_feats = pickle.load(open(usr_feat_dir, 'rb'))
    mov_feats = pickle.load(open(mov_feat_dir, 'rb'))
    usr_feat = usr_feats[str(usr_id)]

    cos_sims = []
    with dygraph.guard():
        # 索引用户特征，计算和输入用户ID的特征的相似度
        for idx, key in enumerate(usr_feats.keys()):
            idx_feat = usr_feats[key]
            usr_feat = dygraph.to_variable(usr_feat)
            idx_feat = dygraph.to_variable(idx_feat)
            sim = fluid.layers.cos_sim(usr_feat, idx_feat)
            cos_sims.append(sim.numpy()[0][0])

    index = np.argsort(cos_sims)[-top_k:]
    mov_info = {}
    with open(mov_info_path, 'r', encoding='ISO-8859-1') as f:
        data = f.readlines()
        for item in data:
            item = item.strip().split("::")
            mov_info[str(item[0])] = item

    print('当前用户是：')
    print("usr_id:", usr_id)
    print("推荐可能喜欢的电影是：")
    res = []

    usr_b = np.random.choice(len(index), 1)[0]
    idx = index[usr_b]

    with open(rating_path, 'r') as f:
        ratings_data = f.readlines()

    usr_rating_info = {}
    for item in ratings_data:
        item = item.strip().split("::")
        # 处理每行数据，分别得到用户ID，电影ID，和评分
        usr_id, movie_id, score = item[0], item[1], item[2]
        if usr_id == str(usr_b):
            usr_rating_info[movie_id] = float(score)

    res = usr_rating_info
    for id in res:
        print('mov_id:', id, mov_info[str(id)])


