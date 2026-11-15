# %%
import pandas as pd
import sqlalchemy

import matplotlib.pyplot as plt
from sklearn import cluster

# %%

engine = sqlalchemy.create_engine("sqlite:///../../data/loyalty-system/database.db")

# %%

def import_query(path):
    with open(path) as open_file:
        return open_file.read()

query = import_query("frequencia_valor.sql")
# %%

df = pd.read_sql(query,engine)
df.head()

df = df[df['qtdepontosPos']<4000]

# %%
!pip install matplotlib seaborn

# %%
plt.plot(df['qtdeFrequencia'],df['qtdepontosPos'],'o')
plt.grid(True)
plt.xlabel("Frequencia")
plt.ylabel("Valor")
plt.show()

# %%

!pip install scikit-learn


# %%

from sklearn import preprocessing

minmax = preprocessing.MinMaxScaler()

X = minmax.fit_transform(df[['qtdeFrequencia','qtdepontosPos']])
# ajuste do cluster de forma normalizadda



kmean = cluster.KMeans(n_clusters=5,random_state=42,max_iter=1000)

kmean.fit(X)

df['cluster'] = kmean.labels_

df_X =['cluster'] = kmean.labels_


df.groupby(by='cluster')['IdCliente'].count()

# %%

import seaborn as sns




sns.scatterplot(data=df,
                x="qtdeFrequencia",
                y="qtdepontosPos", hue="cluster")

plt.grid()



# %%



# %%



# %%



# %%



# %%



# %%


