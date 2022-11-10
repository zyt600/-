import torch
import os
import collections
from torch import nn, optim
from torch.utils.data import TensorDataset, DataLoader, Dataset
import torch.nn.functional as F
from torch.utils.data.dataset import T_co
# from tqdm import tqdm
import math
import random
import numpy as np
# Example of target with class indices

loss = nn.CrossEntropyLoss()
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
output = loss(input, target)
print(output)
output.backward()
# Example of target with class probabilities
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5).softmax(dim=1)
output = loss(input, target)
output.backward()
print(output)
