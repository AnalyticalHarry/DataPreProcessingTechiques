import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

def unique_values_counts_plot(data, columns):
    num_columns = len(columns)
    num_rows = (num_columns + 2) // 3  
    fig, axes = plt.subplots(nrows=num_rows, ncols=3, figsize=(16, 4 * num_rows))
    axes = axes.flatten()
    for i, column in enumerate(columns):
        if column in data:
            #binary data to string for proper categorical plotting
            processed_data = [str(item) for item in data[column]]
            #count unique values
            counts = {}
            for item in processed_data:
                counts[item] = counts.get(item, 0) + 1
            #sorting the counts in ascending order for plotting
            sorted_counts = sorted(counts.items(), key=lambda x: x[1])
            keys, values = zip(*sorted_counts)
            axes[i].bar(keys, values, color='black', alpha=0.8)
            axes[i].set_title(f'Unique Value Counts for {column}')
            axes[i].set_xlabel('Unique Values')
            axes[i].set_ylabel('Counts')
            axes[i].grid(True, ls='--', alpha=0.3, color='black')
            #tick labels with FixedLocator
            axes[i].xaxis.set_major_locator(FixedLocator(range(len(keys))))
            axes[i].set_xticklabels(keys, rotation=60)
        else:
            print(f"Column '{column}' not found in data.")
            axes[i].set_visible(False)
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)
    plt.tight_layout()
    plt.show()

unique_values_counts_plot(df, ['credit_policy','inq_last_6mths', 'delinq_2yrs', 'pub_rec', 'not_fully_paid'])