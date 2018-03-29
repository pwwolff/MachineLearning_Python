import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
path = r"00_Iris\Data\iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pd.read_csv(path, names=names)

# shape
print(df.shape)

# head
print(df.head(20))

# descriptions
print(df.describe())