# RDS Google Mobility IPython Notebook
## WARNING: THIS PROJECT IS IN EARLY DEVELOPMENT STAGE. CONTENT OR CODE SHOULD ONLY BE USED FOR TESTING OR EVALUATION PURPOSES.
This notebook provides interactive viewing of the data provided by the [Google Mobility Reports](https://www.google.com/covid19/mobility/) utilizing Rich Data Services (RDS)

## Software
Python version 3.5 or higher is required for the notebook.

We recommend [Jupyter](https://jupyter.org/) to view the notebook. This is available through [Anaconda](https://www.anaconda.com/)

The [Rich Data Services Python](https://github.com/mtna/rds-python) project is used to query for data from our databases as well as to get any relevant metadata. This can be installed by running:
```bash
pip install mtna-rds
```

To be able to render the the widgets correctly, Jupyterlab must have the correct extension, which can be installed by running the command:
```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

## About
This notebook is published and maintained by [MTNA](https://www.mtna.us/).
