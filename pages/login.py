import dash
from dash import html, dcc, Input, callback, State, Output
import dash_mantine_components as dmc
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
import base64

load_dotenv()
api_gateway = os.getenv('API_GATEWAY')

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
    [Output("login-button", "loading"), Output('session-store', 'data'), Output('url', 'pathname')],
    [Input("login-button", "n_clicks")],
    [State("username", "value"), State("password", "value")],
    prevent_initial_call=True
)
def login_submit(n_clicks, username, password):
    if n_clicks:
        print(f"Username: {username}, Password: {password}")
        try:
            # Make a GET request with basic auth
            response = requests.get(api_gateway + "/user/username/" + username, auth=HTTPBasicAuth(username, password))

            # Check if the response is successful (HTTP status code 200)
            if response.ok:
                print("Authentication successful.")
                # Encode username and password to store in session storage
                encoded_credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
                return True, {'username': username, 'password': password}, '/'
            else:
                print("Authentication failed.")
                return False, {}
        except Exception as e:
            print(f"An error occurred: {e}")
            return False, {}
    return False, None


layout = create_login()
