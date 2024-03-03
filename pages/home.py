from dash import html

import dash

dash.register_page(__name__, path='/', name='Home')


def create_home():
    return html.Div(
        children=[
            html.H1("Home"),
            html.P("Welcome to the home page!"),
        ]
    )

layout = create_home()
