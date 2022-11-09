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

input = torch.tensor([[1], [1]])
print("input", input)

ebdout = ebd(input)
print("ebdout")
print(ebdout)
print("ebdout.size()")
print(ebdout.size())

embed_size = 5
num_hiddens = 8

print("ebdout.view(1, 2, -1)")
print(ebdout.view(1, 2, -1))

lstm = nn.LSTM(embed_size, hidden_size=num_hiddens)
# zeroH = torch.zeros(8).view(1, 1, -1)
# zeroC = zeroH[:]
# print(zeroC)
#
# outlstm, rubish = lstm(ebdout.view(1, 1, -1), (zeroH, zeroC))
outlstm, rubish = lstm(ebdout.view(1, 2, -1))
print()
print(outlstm)
