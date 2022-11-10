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

vocab, embeddings = [], []
with open('glove.6B.50d.txt', 'rt', encoding="utf-8") as fi:
    full_content = fi.read().strip().split('\n')
for i in range(len(full_content)):
    i_word = full_content[i].split(' ')[0]
    i_embeddings = [float(val) for val in full_content[i].split(' ')[1:]]
    vocab.append(i_word)
    embeddings.append(i_embeddings)

vocab_npa = np.array(vocab)
embs_npa = np.array(embeddings)


vocab_npa = np.insert(vocab_npa, 0, '<pad>')
vocab_npa = np.insert(vocab_npa, 1, '<unk>')
print(vocab_npa[:10])


pad_emb_npa = np.zeros((1,embs_npa.shape[1]))   #embedding for '<pad>' token.
unk_emb_npa = np.mean(embs_npa,axis=0,keepdims=True)    #embedding for '<unk>' token.


embs_npa = np.vstack((pad_emb_npa,unk_emb_npa,embs_npa))
print(embs_npa.shape)

my_embedding_layer = torch.nn.Embedding.from_pretrained(torch.from_numpy(embs_npa).float())

assert my_embedding_layer.weight.shape == embs_npa.shape
print(my_embedding_layer.weight.shape)






device="cuda:0"










inputs=torch.tensor([0 for i in range(50)])
inputs.to(device)
print(inputs.device)
myembedding = nn.Embedding.from_pretrained(
    torch.tensor(my_embedding_layer.weight.clone().detach(), dtype=torch.float).clone().detach(), freeze=True).to(device)
embeddingOut=myembedding(inputs)