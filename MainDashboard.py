import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import os

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

tabs = []

for filename in os.listdir():
    if filename.endswith(".py") and filename != "MainDashboard.py":
        tabs.append(
            dcc.Tab(label=filename.replace(".py", ""), value=filename)
        )

app.layout = html.Div(
    children=[
        dcc.Tabs(
            id="tabs",
            value="script1.py",
            children=tabs,
        ),
        html.Div(id="content"),
    ],
)

@app.callback(
    Output("content", "children"),
    [Input("tabs", "value")]
)
def render_content(tab):
    try:
        with open(tab, "r") as f:
            code = f.read()
        return html.Pre(code, style={"white-space": "pre-wrap"})
    except FileNotFoundError:
        return html.Div("File not found")

if __name__ == "__main__":
    app.run_server(debug=True)