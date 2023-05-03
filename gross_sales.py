import pandas as pd
import os.path
from matplotlib import pyplot as plt
import seaborn as sns


pd.plotting.register_matplotlib_converters()

# calculating gross sales of each product type
def gross_sales(app, sales):

    # grouping each product type and calculating the gross sales of each product type
    grouped_sales = sales.groupby('product_type').sum().sort_values('gross_sales', ascending=False).reset_index()
    
    #plotting bar graph comparing gross sales and product type
    plt.figure(figsize=(10, 5))
    sns.barplot(x=grouped_sales['gross_sales'],y=grouped_sales['product_type'])
    plt.title('Gross Sales by Product Type', fontsize=18)
    plt.xlabel('Gross Sales', fontsize=14)
    plt.ylabel('Product Type', fontsize=14)
    plt.grid(axis='x')

    # saving the plot in a folder
    plot_filename = 'gross_sales.png'
    plot_filepath = os.path.join(app.config['STATIC_FOLDER'], plot_filename)
    plt.savefig(plot_filepath)
    
    
    return {
                'title': 'Which product types have the highest gross sales?',
                'filename': plot_filename,
                'data': ['From the above chart we can conclude that '+grouped_sales['product_type'].iloc[0]+' has highest sales while '+grouped_sales['product_type'].iloc[-1]+' had lowest gross sales']
            }

