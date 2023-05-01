import pandas as pd
import os.path
from matplotlib import pyplot as plt
import seaborn as sns


pd.plotting.register_matplotlib_converters()


def gross_sales(app, sales):

    grouped_sales = sales.groupby('product_type').sum().sort_values('gross_sales', ascending=False).reset_index()
    plt.figure(figsize=(10, 5))
    sns.barplot(x=grouped_sales.sort_values('gross_sales', ascending=False)['gross_sales'],y=grouped_sales.sort_values('gross_sales', ascending=False)['product_type'])
    plt.title('Gross Sales by Product Type', fontsize=18)
    plt.xlabel('Gross Sales', fontsize=14)
    plt.ylabel('Product Type', fontsize=14)
    plt.grid(axis='x')

    plot_filename = 'gross_sales.svg'
    plot_filepath = os.path.join(app.config['STATIC_FOLDER'], plot_filename)
    plt.savefig(plot_filepath)
    return grouped_sales['product_type'].iloc[0], grouped_sales['product_type'].iloc[-1]
