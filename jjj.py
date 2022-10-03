import torch
from time import perf_counter
# outt = torch.full((13, 13), 1)
# row2 = torch.full((1, 13), 2)
# col2 = torch.full((13, 1), 2)
# outt[[1, 6, 11]] = row2
# outt[:, [1, 6, 11]] = col2
# outt[[3, 3, 4, 4], [3, 4, 3, 4]] = 3
# outt[[8, 8, 9, 9], [8, 9, 8, 9]] = 3
# outt[[3, 3, 4, 4], [8, 9, 8, 9]] = 3
# outt[[8, 8, 9, 9], [3, 4, 3, 4]] = 3


# print(type(outt.size()))
# print(perf_counter())
# X = torch.randn(100,2)
# print(X)
x=3
y=x^3
# y = x ^ 3 + 4 * (x ^ 2) - 3
print(y)