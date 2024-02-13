import seaborn as sns
import matplotlib.pyplot as plt

(df.select_dtypes(include='number').join(pd.get_dummies(df.select_dtypes(exclude='number')))).corr().pipe((sns.heatmap, 'data'), annot=True, cmap='coolwarm', fmt=".2f") and plt.show()
plt.savefig('correlation_heatmap.png')
