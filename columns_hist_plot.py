import matplotlib.pyplot as plt


def columns_hist_plot(data, columns):
    num_cols = len(columns)
    num_rows = (num_cols + 3) // 4  
    fig, axes = plt.subplots(num_rows, 4, figsize=(15, 4 * num_rows))  
    #array to handle both single-row and multi-row cases
    axes = axes.flatten()
    for i, column in enumerate(columns):
        ax = axes[i]
        ax.hist(data[column], bins=30, edgecolor='grey', color='black', alpha=1)
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        ax.set_title(f'Distribution of {column}')
        ax.grid(True, ls='--', alpha=0.3, color='black')
        #labels to 90 degrees
        ax.tick_params(axis='x', labelrotation=90)
    for i in range(num_cols, num_rows * 4):
        fig.delaxes(axes[i])
    plt.tight_layout()
    plt.show()

columns_hist_plot(df, df.columns)