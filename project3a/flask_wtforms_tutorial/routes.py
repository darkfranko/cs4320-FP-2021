from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from .forms import StockForm
from .charts import *


@app.route("/", methods=['GET', 'POST'])
@app.route("/stocks", methods=['GET', 'POST'])
def stocks():
    
    form = StockForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Get the form data to query the api
            symbols = request.form['symbol']
            chart_type = request.form['chart_type']
            time_series = request.form['time_series']
            start_date = convert_date(request.form['start_date'])
            end_date = convert_date(request.form['end_date'])
            check = True
        while check:
                if end_date <= start_date:
                    #Generate error message as pass to the page
                    err = "ERROR: This End date cannot be earlier than Start date."
                    chart = None
                else:
                    #query the api using the form data
                    err = None
                    
                    #THIS IS WHERE YOU WILL CALL THE METHODS FROM THE CHARTS.PY FILE AND IMPLEMENT YOUR CODE
                    apikey = 'HZ259IH50LQMRCXN'
                    one = "TIME_SERIES_INTRADAY"
                    two = "TIME_SERIES_DAILY"
                    three = "TIME_SERIES_WEEKLY"
                    four = "TIME_SERIES_MONTHLY"
                    #Had major troulbe figuring out why Assertion failure was raising errors...
                    #This chart variable is what is passed to the stock.html page to render the chart returned from the api
                    if symbols == "IBM":
                        #Line
                        if chart_type == "1":
                            if time_series == "1":
                                url = 'https://www.alphavantage.co/query?function={one}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                                r = requests.get(url)
                                data = r.json()
                                ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                                data, meta_data = ts.get_intraday(symbol=symbols,interval='1min', outputsize='full')
                                data['4. close'].plot()
                                plt.title('Intraday Times Series for the stock (1 min)')
                                chart = plt.show()
                                print(chart)
                                check = False
                            elif time_series == "2":
                                url = 'https://www.alphavantage.co/query?function={two}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                                r = requests.get(url)
                                data = r.json()
                                ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                                x = ["Open", "High", "Low", "Close"]
                                y = [data['4. open','color': 'red'].plot(), data['4. high', 'color': 'blue'].plot(), data['4. low', 'color': 'green'].plot(), data['4. close', 'color': 'yellow'].plot()]
                                plt.barh(x, y)
                                for index, value in enumerate(y):
                                    plt.text(value, index,
                                    str(value))
                                    chart = plt.show()
                                    print(chart)
                                    check = False
                            elif time_series == 3:
                                url = 'https://www.alphavantage.co/query?function={three}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                                r = requests.get(url)
                                data = r.json()
                                ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                                x = ["Open", "High", "Low", "Close"]
                                y = [data['4. open','color': 'red'].plot(), data['4. high', 'color': 'blue'].plot(), data['4. low', 'color': 'green'].plot(), data['4. close', 'color': 'yellow'].plot()]
                                plt.barh(x, y)
                                for index, value in enumerate(y):
                                    plt.text(value, index,
                                    str(value))
                                    chart = plt.show()
                                    print(chart)
                                check = False
                            elif time_series == 4:
                                url = 'https://www.alphavantage.co/query?function={four}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                                r = requests.get(url)
                                data = r.json()
                                ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                                x = ["Open", "High", "Low", "Close"]
                                y = [data['4. open','color': 'red'].plot(), data['4. high', 'color': 'blue'].plot(), data['4. low', 'color': 'green'].plot(), data['4. close', 'color': 'yellow'].plot()]
                                plt.barh(x, y)
                                for index, value in enumerate(y):
                                    plt.text(value, index,
                                    str(value))
                                    chart = plt.show()
                                    print(chart)
                                    check = False         
                        else:
                            if time_series == "1":
                                ts = TimeSeries(key=apikey, output_format='pandas')
                                data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
                                data['4. close'].plot()
                                plt.title('Intraday Times Series for the MSFT stock (1 min)')
                                chart = plt.show()
                    else:
                        if chart_type == "1":
                            if time_series == "1":
                                chart = one
                                ts = TimeSeries(key=apikey, output_format='pandas')
                                data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
                                data[chart].plot()
                                plt.title('Intraday Times Series for the MSFT stock (1 min)')
                                chart = plt.show()
                        #Bar
                        else:
                            if time_series == "1":
                                chart = two
                                ts = TimeSeries(key=apikey, output_format='pandas')
                                data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
                                data[chart].plot()
                                plt.title('Intraday Times Series for the MSFT stock (1 min)')
                                chart = plt.show()
                    
        return render_template("stock.html", form=form, template="form-template", err = err, chart = chart)
    
    return render_template("stock.html", form=form, template="form-template")
