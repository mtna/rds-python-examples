# RDS COVID-19 IPython Notebook
This notebook demonstrates the power and efficiency of our Rich Data Services (RDS) framework through the use of a simple python API library. As the COVID-19 pandemic is of a global concern, this notebook focuses on the COVID-19 data gathered through [John Hopkins University](https://coronavirus.jhu.edu/).

## Software
Python version 3.5 or higher is required for the notebook.

We recommend [Jupyter](https://jupyter.org/) to view the notebook. This is available through [Anaconda](https://www.anaconda.com/)

The [Rich Data Services Python](https://github.com/mtna/rds-python) project is used to query for data from our databases as well as to get any relevant metadata. This can be installed by running:
```bash
pip install mtna-rds
```

The examples used in the notebook create Plotly graphs. To be able to use plotly, you must run the following command:
```bash
pip install plotly
```

To be able to render the Plotly graphs correctly, Jupyterlab must have the correct extension, which can be installed by running the command:
```bash
jupyter labextension install jupyterlab-plotly
```

## About
This notebook is published and maintained by [MTNA](https://www.mtna.us/).

To see what else we are doing to contribute doing the COVID-19 pandemic, visit our site [here](https://covid19.richdataservices.com/).
