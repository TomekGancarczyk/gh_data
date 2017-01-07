import pandas as pd
from sklearn.manifold import TSNE
tsne = TSNE(random_state=42, n_components=3)
file = r"C:\Users\T440p\Downloads\iris_norm.csv"
file2 = r"C:\Users\T440p\Downloads\iris_tsne.csv"
df = pd.read_csv(file, delimiter=';')
digits = tsne.fit_transform(df)
df_tsne = pd.DataFrame(digits)
df_tsne.to_csv(file2)

print digits

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