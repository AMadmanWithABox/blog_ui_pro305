import dash
from dash import html, dcc, Input, callback, State, Output
import dash_mantine_components as dmc

dash.register_page(__name__, path='/login', name='Login')


def create_login():
    return html.Div(
        children=[
            html.H1("Login"),
            html.Div(
                children=[
                    dmc.TextInput(
                        label="Username",
                        id="username",
                        placeholder="Enter your username",
                        required=True,
                    ),
                    dmc.PasswordInput(
                        label="Password",
                        id="password",
                        placeholder="Enter your password",
                        required=True,
                    ),
                    dmc.Button(
                        "Login",
                        id="login-button",
                        color="blue",
                        variant="filled",
                        mt=5
                    ),
                ]
            ),
        ]
    )


@callback(
    Output("login-button", "loading"),
    Input("login-button", "n_clicks"),
    State("username", "value"),
    State("password", "value"),
    prevent_initial_call=True
)
def login_submit(n_clicks, username, password):
    if n_clicks:
        print(f"Username: {username}, Password: {password}")
        return True
    return False


layout = create_login()
