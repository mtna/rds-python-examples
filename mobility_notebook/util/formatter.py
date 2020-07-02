from IPython.core.display import display, HTML
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io
import datetime

def header(country):
    return display(HTML(f'''
    <p style="font-size:50px">{country}</p>
    '''))

def line_plot(results, figsize=None):   
    df = pd.DataFrame(results.records, columns = results.columns)
    ax = df.plot(figsize=figsize, legend=False)
    ax.set_ylim(-100,100)
    trend_name = results.metadata[1]['name']
    ax.fill_between(df["Datestamp"], df[trend_name].tolist(), color='#eeefff')

    ax.margins(0)
    ax.xaxis.set_major_locator(plt.LinearLocator(3))
    y_tick_labels = []
    for y in ax.get_yticks():
        if str(y) == "0.0":
            y_tick_labels.append("baseline")
        else:
            y_tick_labels.append(str(y)[:-2] + "%")
    ax.set_yticklabels(y_tick_labels)
    
    plt.close()
    return ax
    
def code_values(codes):
    code_rows = ''
    for code in codes:
        code_rows += f'''
        <tr style="border: 1px solid black">
            <td style="text-align:left; border: 1px solid black">{code['codeValue']}</td>
            <td style="text-align:left; border: 1px solid black">{code['name']}</td>
        </tr>
        '''

    return display(HTML(f'''
    <html>
    <body>
    <div>
    <h1>Country Codes</h1>
    <table style="border: 1px solid black">
        <tr style="border: 1px solid black">
            <td style="text-align:center; border: 1px solid black"><b>Value</b></td>
            <td style="text-align:center; border: 1px solid black"><b>Label</b></td>
        </tr>
        {code_rows}
    </table>
    </div>
    </body>
    </html>
    '''))

def variable_metadata(variables):
    var_rows = ''
    for var in variables:
        var_rows += f'''
        <tr style="border: 1px solid black">
            <td style="text-align:left; border: 1px solid black">{var['id']}</td>
            <td style="text-align:left; border: 1px solid black">{var['label']}</td>
            <td style="text-align:left; border: 1px solid black">{var['description']}</td>
        </tr>
        '''

    return display(HTML(f'''
    <html>
    <body>
    <div>
    <h1>Country Codes</h1>
    <table style="border: 1px solid black">
        <tr style="border: 1px solid black">
            <td style="text-align:center; border: 1px solid black"><b>ID</b></td>
            <td style="text-align:center; border: 1px solid black"><b>Label</b></td>
            <td style="text-align:center; border: 1px solid black"><b>Description</b></td>
        </tr>
        {var_rows}
    </table>
    </div>
    </body>
    </html>
    '''))

def baseline_chart(trend_name, baseline_value, sB64Img):
    display(HTML(get_style() + (
        '<div class="floating-text">'+ 
        f'<h3 style="text-align:center">{trend_name}</h3>'+
        f'<p style="font-size:80px;padding-bottom:10px;margin-bottom:10px;text-align:center">{baseline_value}%<p>'+
        f'<p style="font-size:10px;text-align:center">compared to baseline<p>'+
        '</div>'
        '<div class="floating-box">'+ 
        '<img src="data:image/png;base64,{}\n">'.format(sB64Img)+
        '</div>')))

def get_style():
    return """
    <style>
    .floating-box {
    display: inline-block;
    margin: 10px;
    background-color: white;
    }
    .floating-text {
    width: 350px;
    display: inline-block;
    margin: 10px;
    vertical-align: 45px;
    }
    </style>
    """

def format_datatime(datetime):
    datetime_formatted = str(datetime.year) + "-" + str(datetime.month) + "-" + str(datetime.day)
    return datetime_formatted