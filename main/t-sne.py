import pandas as pd
from sklearn.manifold import TSNE
from sklearn import preprocessing
import matplotlib as plt
import seaborn as sns
tsne = TSNE(random_state=12, n_components=2, perplexity=40, learning_rate=100)
file = r"C:\Users\T440p\Downloads\iris (1).csv"
file2 = r"C:\Users\T440p\Downloads\iris_tsne.csv"
col = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Length']
df = pd.read_csv(file, delimiter=',', usecols=col)
# print df

min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df)
df_normalized = pd.DataFrame(np_scaled)
# print df_normalized

digits = tsne.fit_transform(df)
# error = tsne.
# print digits.kl_divergence_
df_tsne = pd.DataFrame(digits, columns=['x', 'y'])
df_tsne.to_csv(file2)
# sns.lmplot('x', 'y', data=df_tsne, fit_reg=False)
# sns.plt.show()
# print digits

# normalizacja
# for v in data_set:
#     # print v
#     _d = v.split(",")
#     # print _d, 'split'
#     data.append([float(i) for i in _d])
#
# col_max = []
# # print len(data[0])
# for i in range(len(data[0])):
#     col = []
#     for j in data:
#         col.append(j[i])
#     col_max.append(max(col))
# # print col_max, 'col max'
# data_normalized = []
# for row in data:
#     _d = []
#     for i, item in enumerate(row):
#         _d.append(str(item/ col_max[i]))
#     data_normalized.append(_d)