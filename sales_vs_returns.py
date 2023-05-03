import pandas as pd
import os.path
from matplotlib import pyplot as plt
import seaborn as sns


pd.plotting.register_matplotlib_converters()


def sales_vs_returns(app, sales):
     
     gross_sales = sales.loc[:, ['product_type', 'gross_sales']].groupby('product_type').sum()
     gross_sales.rename(columns = {'gross_sales': 'sales'}, inplace = True)
     gross_sales['sale_type'] = 'gross_sale'

     returns = sales.loc[:, ['product_type', 'returns']].groupby('product_type').sum()
     returns.rename(columns = {'returns': 'sales'}, inplace = True)
     returns['sale_type'] = 'return'

     combined_sales_returns = pd.concat([gross_sales, returns]).reset_index()

     # Create barplot comparing gross sales vs returns
     plt.figure(figsize = (10, 5))
     sns.barplot(x = 'sales', 
               y = 'product_type',
               hue = 'sale_type',
               data = combined_sales_returns.sort_values(['sales', 'sale_type'], ascending = [False, False]))
     plt.title('Gross Sales vs Returns by Product Type')
     plt.xlabel('Sales')
     plt.ylabel('Product Type')
     plt.grid(axis='x')  
     
     # saving the plot in a folder
     plot_filename = 'sales_vs_returns.png'
     plot_filepath = os.path.join(app.config['STATIC_FOLDER'], plot_filename)
     plt.savefig(plot_filepath)
     
     
     return {   
               'title':'Gross sales and returns for each product.',
               'filename':plot_filename,
               'data':''
            }