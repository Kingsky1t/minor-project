from flask import Flask, request, render_template
import pandas as pd
from gross_sales import gross_sales
from sales_vs_returns import sales_vs_returns
from corelation import corelation
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'


@app.route('/', methods=['GET', 'POST'])
def home():
    result=[]
    if request.method == 'GET':
        return render_template('home.html')
    else:
        file = request.files['file']
        #reading the file and renaming the columns for efficiency
        sales = pd.read_csv(file)
        sales=sales.dropna()
        sales.columns = ['product_type', 'net_quantity','gross_sales', 'discounts', 'returns', 'total_net_sales']
        
        result.append(gross_sales(app, sales))
        result.append(sales_vs_returns(app, sales))
        result.append(corelation(app,sales))
        # sales_vs_returns(app,sales)
        # corelation(app,sales)
        
        # result = [
        #     {
        #         'title': 'Which product types have the highest gross sales?',
        #         'filename': 'gross_sales.svg',
        #         'data': 'From the above chart we can conclude that '+most+' has highest sales while '+least+' had lowest gross sales'
        #     },
        #     {   
        #         'title':'hi',
        #         'filename':'sales_vs_returns.svg',
        #         'data':'hello world'
        #     },
        #     {   
        #         'title':'hi',
        #         'filename':'corelation.svg',
        #         'data':'hello world'
        #     }
        # ]

        return render_template('home.html', result=result)
