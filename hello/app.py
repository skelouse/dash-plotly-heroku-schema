# https://sql-viewer.herokuapp.com/

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd
import flask

import plotly
import plotly.graph_objs as go
import plotly.offline as pyo 

server = flask.Flask(__name__)

app = dash.Dash(__name__, server=server)

app.layout = html.Div(id='main-div', children=[

    html.H1(id='main_header', className='main_header', children="This is a test title 2")
])


if __name__ == "__main__":
    app.run_server(debug=True, threaded=True)