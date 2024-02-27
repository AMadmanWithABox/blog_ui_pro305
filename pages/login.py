import dash
from dash import html, dcc

dash.register_page(__name__, path='/login', name='Login')


def create_login():
    return html.Div(
        children=[
            html.H1("Login"),
            html.Div(
                children=[
                    html.Label("Username"),
                    dcc.Input(id="username-input", type="text"),
                    html.Label("Password"),
                    dcc.Input(id="password-input", type="password"),
                    html.Button("Login", id="login-button"),
                ]
            ),
        ]
    )


layout = create_login()