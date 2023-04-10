"""
https://blog.csdn.net/Richard_Kim/article/details/121432007?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-4-121432007-blog-104562798.235^v28^pc_relevant_default_base1&spm=1001.2101.3001.4242.3&utm_relevant_index=7
"""

import os
from torch.utils.data import Dataset, DataLoader
import torch
import torch.nn as nn
from sklearn.metrics import f1_score
from tqdm import trange
from tqdm import tqdm


# 构建数据集
def build_corpus(split, data_dir):
    """
    :param split: 分割类型，是训练集，验证集or测试集
    :param data_dir: 数据路径
    :return:  word_lists(原始数据), tag_lists(标签数据), word2index, tag2index
    """
    assert split in ['train', 'dev', 'test']
    word_lists = []
    tag_lists = []
    with open(data_dir, 'r', encoding='utf-8') as f:
        word_list = []
        tag_list = []
        for line in f:
            if line != '\n':
                word, tag = line.strip('\n').split()
                # print("word=", word)
                # print("tag=", tag)
                word_list.append(word)
                tag_list.append(tag)
            else:
                word_lists.append(word_list)
                tag_lists.append(tag_list)
                word_list = []
                tag_list = []

    # 进行排序
    sorted_word_lists = sorted(word_lists, key=lambda x: len(x), reverse=False)
    sorted_tag_lists = sorted(tag_lists, key=lambda x: len(x), reverse=False)
    # 返回word2index tag2index
    word2index = build_map(sorted_word_lists)
    tag2index = build_map(sorted_tag_lists)
    # print("word2index=", word2index)
    # print("tag2index=", tag2index)
    word2index['<UNK>'] = len(word2index)
    word2index['<PAD>'] = len(word2index)
    tag2index['<PAD>'] = len(tag2index)
    return word_lists, tag_lists, word2index, tag2index


# 构建word2index和tag2index字典
def build_map(lists):
    """
    :param lists:
    :return: 返回一个字典
    """
    maps = {}
    for list in lists:
        for element in list:
            if element not in maps:
                maps[element] = len(maps)
    return maps


word_lists, tag_lists, word2index, tag2index = build_corpus('train', 'data/train.txt')


# print(word2index)
# print(tag2index)


# 定义数据集对象
class MyDataset(Dataset):
    # 初始化对象元素
    def __init__(self, datas, tags, word_2_index, tag_2_index):
        self.datas = datas
        self.tags = tags
        self.word_2_index = word_2_index
        self.tag_2_index = tag_2_index

    def __getitem__(self, index):
        data = self.datas[index]
        tag = self.tags[index]
        #
        data_index = [self.word_2_index[i] for i in data]
        tag_index = [self.tag_2_index[i] for i in tag]
        return data_index, tag_index

    def __len__(self):
        # 每句话的长度肯定和标签的长度一样
        assert len(self.datas) == len(self.tags)
        return len(self.tags)

    # 这里是对每个batch做数据处理,进行数据的拼接
    # 这batch_datas长度是batch_size中规定的那个维度
    # 里面包含了data和tag

    def pro_batch_data(self, batch_datas):
        global device
        datas = []
        tags = []
        batch_lens = []
        for data, tag in batch_datas:
            datas.append(data)
            tags.append(tag)
            batch_lens.append(len(data))
        # print("batch_datas=", batch_datas)
        # print("datas=", datas)
        # print("tags=", tags)

        batch_max_len = max(batch_lens)
        datas = [i + [self.word_2_index["<PAD>"]] * (batch_max_len - len(i)) for i in datas]
        tags = [i + [self.tag_2_index["<PAD>"]] * (batch_max_len - len(i)) for i in tags]
        return torch.tensor(datas, dtype=torch.int64, device=device), torch.tensor(tags, dtype=torch.long,
                                                                                   device=device)


# 模型
class BiLSTM_CRF(nn.Module):
    def __init__(self, corpus_num, embedding_num, hidden_num, class_num, biFlag=True):
        """
        :param corpus_num: 训练语料长度
        :param embedding_num: 词嵌入的维度
        :param hidden_num:  隐藏层维度
        :param class_num:  分类的种类多少
        :param BiFlag:   是否为双向LSTM，默认为双向，这样的话全连接层就要有2倍的输入
        """
        super().__init__()
        self.embedding = nn.Embedding(corpus_num, embedding_num)
        self.lstm = nn.LSTM(embedding_num, hidden_num, batch_first=True, bidirectional=biFlag)
        # 损失函数
        self.cross_loss = nn.CrossEntropyLoss()
        if biFlag:
            self.linear = nn.Linear(hidden_num * 2, class_num)
        else:
            self.linear = nn.Linear(hidden_num, class_num)

    def forward(self, batch_data, batch_tag=None):
        embedding = self.embedding(batch_data)
        out, _ = self.lstm(embedding)
        pre = self.linear(out)
        # 预测集合中最大的那一个就是预测值
        self.pre = torch.argmax(pre, dim=-1).reshape(-1)
        if batch_tag is not None:
            preReshape = pre.reshape(-1, pre.shape[-1])
            batch_tag_reshape = batch_tag.reshape(-1)
            print("preShape‘s shape", preReshape.shape)
            print("batchTagReshape", batch_tag_reshape.shape)
            loss = self.cross_loss(preReshape, batch_tag_reshape)
            return loss
        else:
            return self.pre


# 测试函数，用户输入文字，看看模型运行结果
def usage():
    global word_2_index, model, index_2_tag, device
    while True:
        text = input("输入：")
        # text = "张定宇是金银潭医院的一名教授"
        text_index = [[word_2_index[i] for i in text]]
        print("text_index=", text_index)
        text_index = torch.tensor(text_index, dtype=torch.int64, device=device)
        model.forward(text_index)
        pre = [index_2_tag[i] for i in model.pre]
        print([f'{w}_{s}' for w, s in zip(text, pre)])


if __name__ == "__main__":
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    train_data, train_tag, word_2_index, tag_2_index = build_corpus("train", "data/train.txt")
    dev_data, dev_tag, _, none_ = build_corpus("dev", "data/test_Demo.txt")
    index_2_tag = [i for i in tag_2_index]

    corpus_num = len(word_2_index)
    """
        这里为什么分类的类别是tag2index的长度呢，因为命名实体识别的本质就是对每个字分类
        和文本分类有思想上的相同性，所以就是标签类型的长度
    """
    class_num = len(tag_2_index)
    # 超参数
    epoch = 5
    train_batch_size = 5
    dev_batch_size = 5
    embedding_num = 101
    hidden_num = 107
    bi = True
    lr = 0.001

    # 搞到训练数据
    train_dataset = MyDataset(train_data, train_tag, word_2_index, tag_2_index)
    train_dataloader = DataLoader(train_dataset, train_batch_size, shuffle=False,
                                  collate_fn=train_dataset.pro_batch_data)
    # 验证数据
    dev_dataset = MyDataset(dev_data, dev_tag, word_2_index, tag_2_index)
    dev_dataloader = DataLoader(dev_dataset, dev_batch_size, shuffle=False, collate_fn=train_dataset.pro_batch_data)

    # 定义模型
    model = BiLSTM_CRF(corpus_num, embedding_num, hidden_num, class_num, bi)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    model = model.to(device)
    # 定义交叉熵损失函数
    cross_loss = nn.CrossEntropyLoss()

    for e in trange(epoch):
        model.train()
        for batch_data, batch_tag in tqdm(train_dataloader):
            train_loss = model.forward(batch_data, batch_tag)
            train_loss.backward()  # 反向传播
            # 更新参数
            opt.step()
            opt.zero_grad()
        # 开始测试
        model.eval()
        # 保存模型
        torch.save(model, "Model")
        all_pre = []
        all_tag = []
        for dev_batch_data, dev_batch_tag in train_dataloader:
            dev_loss = model.forward(dev_batch_data, dev_batch_tag)
            all_pre.extend(model.pre.detach().cpu().numpy().tolist())
            all_tag.extend(dev_batch_tag.detach().cpu().numpy().reshape(-1).tolist())
        score = f1_score(all_tag, all_pre, average="micro")
        print(f"{e},f1_score:{score:.3f},dev_loss:{dev_loss:.3f},train_loss:{train_loss:.3f}")
    # 调用测试函数
    usage()
