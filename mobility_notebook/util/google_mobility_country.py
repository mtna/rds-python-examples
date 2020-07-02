from rds import Server
from . import formatter
import ipywidgets as widgets
from ipywidgets import interact
import datetime
import io
import base64
from IPython.core.display import display, HTML

server = Server("https://covid19.richdataservices.com/rds")
catalog = server.get_catalog("int")
dataproduct = catalog.get_dataproduct("google_mobility_country")

country_codes = dataproduct.get_code("iso3166_1", limit=1000)

trend_variables = []
trend_variables.append(dataproduct.get_variable(variable="retail_recreation_pct"))
trend_variables.append(dataproduct.get_variable(variable="grocery_pharmacy_pct"))
trend_variables.append(dataproduct.get_variable(variable="parks_pct"))
trend_variables.append(dataproduct.get_variable(variable="transit_station_pct"))
trend_variables.append(dataproduct.get_variable(variable="workplace_pct"))
trend_variables.append(dataproduct.get_variable(variable="residential_pct"))

def interactive():
    code_values = []
    global country_codes
    for code in country_codes:
        code_values.append(code['name'])

    country = widgets.Dropdown(
        options=code_values,
        value=code_values[0],
        description='Country:',
        disabled=False,
    )

    start = widgets.DatePicker(
        value=datetime.datetime(2020,1,1),
        description='Start Date:',
        disabled=False
    )

    end = widgets.DatePicker(
        value=datetime.datetime(2020,12,31),
        description='End Date:',
        disabled=False
    )

    interact(get_data, country=country, date_start=start, date_end=end)
    
def get_data(country, date_start, date_end):
    global country_codes
    for code in country_codes:
        if code['name'] == country:
            code_value = code['codeValue']
    
    formatter.header(country)
    
    global trend_variables
    for trend_variable in trend_variables:
        trend = trend_variable['label']
        trend_value = trend_variable['id']
        
        trend_avg = trend + ":avg("+trend_value+")"
        where = ["iso3166_1=" + code_value+" AND date_stamp>=" + formatter.format_datatime(date_start) + " AND date_stamp<=" + formatter.format_datatime(date_end)]

        results = dataproduct.select(cols=["date_stamp", trend_avg], orderby=["date_stamp"], groupby=["date_stamp"], where=where, inject=True)
        if results.records == None or len(results.records) == 0:
            return display(HTML(f'''<h3>{"No trend data available for " + trend + " in " + country + "."}</h3>'''))

        plot = formatter.line_plot(results)

        Bio=io.BytesIO()
        fig = plot.get_figure()
        fig.canvas.print_png(Bio)

        baseline_value = int(results.records[-1][1])

        sB64Img = base64.b64encode(Bio.getvalue()).decode()
        formatter.baseline_chart(results.metadata[1]["name"], baseline_value, sB64Img)
