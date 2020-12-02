"""
My site: https://sql-viewer.herokuapp.com/

To run this file, cd into this directory and run the commands

>>> pip install -r requirements.txt
>>> gunicorn app:server --reload

Follow this tutorial to get it hosted on heroku:
https://devcenter.heroku.com/articles/getting-started-with-python
"""

import os
import dash
# import dash_core_components as dcc
import dash_html_components as html
# import dash_table
import flask
from flask import send_from_directory
# import plotly
# import plotly.graph_objs as go
# import plotly.offline as pyo

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
app.layout = html.Div(id='main-div', children=[
    html.H1(
        id='main_header',
        className='main_header',
        children="This is a test header")  # comma here to add more children
])

with open('./assets/app.css', 'r') as f:
    var = str(f.read())
    styles = (
            """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>This is the title</title>
    <meta name="image" property="og:image"
          content="https://image/url.png">
    <meta name="description" property="og:description"
          content="This is an example description">
    <meta name="author" content="Samuel Stoltenberg">
</head>
    <style>
           """ + var +
            """
    </style>

<body>
    {%app_entry%}
    <footer>
        {%config%}
        {%scripts%}
        {%renderer%}
    </footer>
</body>
</html>
""")


@server.route('/favicon.ico')
def favicon():
    """
    Function for routing the favicon.ico, simply swap the image in assets
    to make it your own favicon https://www.favicon.cc/
    Quick note,  if you run gunicorn before updating the favicon
    it will still be the alien in your cache try running
    on a different port
    >>> gunicorn app:server -b 127.0.0.1:8001
    """
    return send_from_directory(os.path.join(server.root_path, 'assets'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


app.index_string = styles


if __name__ == "__main__":
    app.run_server(debug=True)
