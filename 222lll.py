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












m = nn.LogSoftmax(dim=0)
input = torch.randn(2, 3)
print(input)
output = m(input)
print(output)

