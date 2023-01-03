使用glove预训练word embedding+LSTM对twitter用户评论进行情感分析，分为中性、积极、消极三类，准确率60%
<!-- 第三次作业
作业要求：本次作业要求使用预训练模型CLIP[1] 进行文本到图片检索 (Image-Text Retrieval)。具体地，本次作业不要求训练模型，只需要利用预训练好的CLIP模型在 Flickr30K 数据集[4] 的测试集划分[5] 上对图片和文本进行编码[3]，并设计 (一种或多种) 相似度函数返回与每条文本 (共 5000 条) 语义相关的图片，报告模型性能 (R@1, R@5, R@10)。
作业分数：本次作业共十分。（R@1:45, R@5: 70, R@10: 80以上即可m满分）
提交要求：提交完成作业后的 Colab 链接或者 ipynb 文件，需保证提交的文件是运行后的，即需要有运行结果显示。提醒：如果提交 Colab 链接的话，需要在 Google Drive 中设置文件访问权限。
其他说明：如果对任务、数据集、评价指标等有疑问的话可以参考下下面列出的参考文献[2]。
参考文献及链接
Radford, Alec, et al. "Learning transferable visual models from natural language supervision." International Conference on Machine Learning. PMLR, 2021.

Rao, Jun, et al. "Where Does the Performance Improvement Come From?-A Reproducibility Concern about Image-Text Retrieval." arXiv preprint arXiv:2203.03853 (2022).

CLIP Code & Tutorial: https://github.com/openai/CLIP ; https://colab.research.google.com/github/openai/clip/blob/master/notebooks/Interacting_with_CLIP.ipynb .

Flickr30K 数据集官方下载链接: http://shannon.cs.illinois.edu/DenotationGraph/data/index.html .

采用 Deep Visual-Semantic Alignments for Generating Image Descriptions, CVPR 2015 的数据集划分方式 (包括每张图片的所对应的 5 条文本数据)，下载链接: https://disk.pku.edu.cn:443/link/457208074C678CF326B32689D8BAC904 . -->