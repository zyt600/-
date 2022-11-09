import torch
import os
import collections
from torch import nn
from torch.utils.data import TensorDataset, DataLoader, Dataset
import torch.nn.functional as F
from torch.utils.data.dataset import T_co
# from tqdm import tqdm
import math
import random
import numpy as np

ebd = torch.nn.Embedding(2, 5)
input = torch.tensor([1])
print(input)
ebdout = ebd(input)
print(ebdout, ebdout.size())
# print(ebdout.view(1,1,-1))
embed_size = 5
num_hiddens = 8
lstm = nn.LSTM(embed_size, hidden_size=num_hiddens)
zeroH = torch.zeros(8).view(1, 1, -1)
zeroC = zeroH[:]
print(zeroC)
outlstm = lstm(ebdout.view(1, 1, -1), zeroH, zeroC)
print()
print()
for itm in outlstm:
    print(itm)
