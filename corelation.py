import pandas as pd
import os.path
from matplotlib import pyplot as plt
import seaborn as sns


pd.plotting.register_matplotlib_converters()


def corelation(app, sales):
     
     corr_matrix = sales.corr()
     sns.heatmap(corr_matrix,
            xticklabels=corr_matrix.columns,
            yticklabels=corr_matrix.columns)
     plt.title('Corelation between Stats',fontsize=18)
     
     plot_filename = 'corelation.svg'
     plot_filepath = os.path.join(app.config['STATIC_FOLDER'], plot_filename)
     plt.savefig(plot_filepath)