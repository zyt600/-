import torch
from torch import nn




def quadratic_data_generator(data_size):
    # generate an input tensor of size data_size with torch.randn
    x = torch.randn(data_size, 1) - 2
    x = x.to("cpu")
    # calculate y = x^2 + 4x - 3
    y = pow(x,2)+4*4-3
    return x, y

x,y=quadratic_data_generator(12)
print(x)
print(y)
classifier = nn.Sequential(
                        nn.Linear(1,1),
                        nn.ReLU(),
                        )
print(classifier(x))