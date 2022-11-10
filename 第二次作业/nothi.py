import os
import re
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




inputs = torch.tensor([0 for i in range(50)])
inputs.to("cuda:0")
print(inputs.device)
