

def unique_values_counts_table(data, columns):
    tables = []

    for column in columns:
        if column in data:
            #counting unique values
            counts = {}
            for item in data[column]:
                counts[item] = counts.get(item, 0) + 1

            #sorting the counts in ascending order
            sorted_counts = sorted(counts.items(), key=lambda x: x[1])
            max_key_length = max(len(str(key)) for key, _ in sorted_counts)
            max_value_length = max(len(str(value)) for _, value in sorted_counts)
            header = f"{column.center(max_key_length)} | {'Count'.center(max_value_length)}"
            separator = '-' * (max_key_length + max_value_length + 3)
            table_rows = [f"{str(key).rjust(max_key_length)} | {str(value).rjust(max_value_length)}" 
                          for key, value in sorted_counts]
            table = header + "\n" + separator + "\n" + "\n".join(table_rows)
            tables.append(table)
        else:
            tables.append(f"Column '{column}' not found in data.")

    return '\n\n'.join(tables)

# print(unique_values_counts_table(df, ['credit_policy', 'inq_last_6mths', 'delinq_2yrs', 'pub_rec', 'not_fully_paid']))