import torch
from torch import nn

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

a=[1,2,3]
a=torch.tensor([1,2])
b=[]
b.append(a.clone().detach())
b.append(a)
a[0]=999
print(b)