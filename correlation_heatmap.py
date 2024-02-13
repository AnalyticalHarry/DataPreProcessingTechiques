import seaborn as sns
import matplotlib.pyplot as plt

#plot heat map even value is categorical 
(df.select_dtypes(include='number').join(pd.get_dummies(df.select_dtypes(exclude='number')))).corr().pipe((sns.heatmap, 'data'), annot=True, cmap='coolwarm', fmt=".2f") and plt.show()
