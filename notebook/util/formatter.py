#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:24:11 2020

provides formatting for COVID-19 Notebook

@author: seanlucas
"""

def html_catalog(catalog):
    metadata = catalog.get_metadata()
    dataproduct_rows = ''
    for dataproduct in metadata['dataProducts']:
        dataproduct_rows += f'''
        <tr style="border: 1px solid black">
            <td style="text-align:left; border: 1px solid black">{dataproduct['name']}</td>
            <td style="text-align:left; border: 1px solid black">{dataproduct['id']}</td>
        </tr>
        '''

    return f'''
    <html>
    <body>
    <div>
    <h1>{metadata['name']} ({metadata['id']})</h1>
    <p>{metadata['description']}</p>
    <table style="border: 1px solid black">
        <tr style="border: 1px solid black">
            <td colspan="2" style="text-align:center"><b>Dataproducts</b></td>
        </tr>
            <tr style="border: 1px solid black">
            <td style="text-align:center; border: 1px solid black"><b>Name</b></td>
            <td style="text-align:center; border: 1px solid black"><b>ID</b></td>
        </tr>
        {dataproduct_rows}
    </table>
    </div>
    </body>
    </html>
    '''

def html_variables(dataproduct):
    metadata = dataproduct.get_variable()
    var_rows = ''
    for variable in metadata:
        class_id = ''
        try:
            class_id = variable['classificationId']
        except KeyError:
            pass

        var_rows += f'''
        <tr style="border: 1px solid black">
            <td style="text-align:left; border: 1px solid black">{variable['name']}</td>
            <td style="text-align:left; border: 1px solid black">{variable['id']}</td>
            <td style="text-align:left; border: 1px solid black">{variable['label']}</td>
            <td style="text-align:left; border: 1px solid black">{variable['dataType']}</td>
            <td style="text-align:left; border: 1px solid black">{class_id}</td>
        </tr>
        '''

    return f'''
    <html>
    <body>
    <div>
    <table style="border: 1px solid black">
        <tr style="border: 1px solid black">
            <td colspan="5" style="text-align:center"><b>Variables</b></td>
        </tr>
        <tr style="border: 1px solid black">
            <td style="text-align:center; border: 1px solid black"><b>Name</b></td>
            <td style="text-align:center; border: 1px solid black"><b>ID</b></td>
            <td style="text-align:center; border: 1px solid black"><b>Label</b></td>
            <td style="text-align:center; border: 1px solid black"><b>Data Type</b></td>
            <td style="text-align:center; border: 1px solid black"><b>Classification</b></td>
        </tr>
        {var_rows}
    </table>
    </div>
    </body>
    </html>
    '''

def html_classification(dataproduct, class_id, limit=20):
    metadata = dataproduct.get_classification(class_id)
    code_count = metadata['rootCodeCount']

    codes = dataproduct.get_code(class_id, limit)
    code_rows = ''
    for code in codes:
        code_rows += f'''
        <tr style="border: 1px solid black">
            <td style="text-align:left; border: 1px solid black">{code['codeValue']}</td>
            <td style="text-align:left; border: 1px solid black">{code['name']}</td>
        </tr>
        '''

    return f'''
    <html>
    <body>
    <div>
    <h1>{metadata['id']}</h1>
    <p>Code Count: {code_count}</p>
    <table style="border: 1px solid black">
        <tr style="border: 1px solid black">
            <td colspan="2" style="text-align:center"><b>Codes</b></td>
        </tr>
        <tr style="border: 1px solid black">
            <td style="text-align:center; border: 1px solid black"><b>Value</b></td>
            <td style="text-align:center; border: 1px solid black"><b>Label</b></td>
        </tr>
        {code_rows}
    </table>
    </div>
    </body>
    </html>
    '''