# Import dependencies.
import random
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
from torchvision import datasets, transforms




input = torch.randn(128,10)
tar=torch.randn(128,10)
lossfun=nn.NLLLoss(reduction="sum")
loss1=lossfun(tar,input)
loss2=lossfun(input,tar)
print(loss1)
print(loss2)