import pandas as pd
import os.path
from matplotlib import pyplot as plt
import seaborn as sns


pd.plotting.register_matplotlib_converters()


def corelation(app, sales):
       
       corr_matrix = sales.corr()
       
       plt.figure(figsize=(10, 5))
       sns.heatmap(corr_matrix,
              xticklabels=corr_matrix.columns,
              yticklabels=corr_matrix.columns,
              annot=True)
       plt.title('Corelation between Stats',fontsize=18)
       # plt.grid(axis='x')
              
       plot_filename = 'corelation.png'
       plot_filepath = os.path.join(app.config['STATIC_FOLDER'], plot_filename)
       plt.savefig(plot_filepath)
       
       res_text=[]
       length=len(sales.columns)-1
       for i in range(0,length):
              for j in range(0,i):
                     if corr_matrix.iloc[i][j]>=0.5 and i!=j:
                            str=f"{sales.columns[i]} and {sales.columns[j]} are highly and positively correlated"
                            res_text.append(str)
                     elif corr_matrix.iloc[i][j]<=-0.5 and i!=j:
                            str=f"{sales.columns[i]} and {sales.columns[j]} are highly and negatively correlated"
                            res_text.append(str)
       res_text.append('Rest are less correlated')

       return {   
              'title':'Correlation Analysis',
              'filename':plot_filename,
              'data':res_text
              }