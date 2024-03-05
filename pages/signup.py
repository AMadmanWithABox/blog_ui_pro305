import dash
from dash import html, dcc, Input, callback, State, Output
import dash_mantine_components as dmc
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
import base64

from config import cache

load_dotenv()
api_gateway = os.getenv('API_GATEWAY')

dash.register_page(__name__, path='/signup', name='Signup')


layout = html.Div(
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
                dmc.PasswordInput(
                    label="Verify Password",
                    id="v-password",
                    placeholder="Enter your password",
                    required=True,
                ),
                dmc.Button(
                    "Signup",
                    id="signup-button",
                    color="blue",
                    variant="filled",
                    mt=5
                ),
            ]
        ),
    ]
)


@callback(
    Output("signup-button", "loading"),
    Output('url', 'pathname', allow_duplicate=True),
    Input("signup-button", "n_clicks"),
    State("username", "value"),
    State("password", "value"),
    State("v-password", "value"),
    prevent_initial_call=True,
)
def signup_submit(n_clicks, username, password, v_password):
    if n_clicks:
        print(f"Username: {username}, Password: {password}")


        try:
            if password != v_password:
                raise Exception('passwords are not the same')
            # Make a GET request with basic auth
            response = requests.post(f"{api_gateway}/user", json={'username': username, 'password': password})
            print(response.json())
            # Check if the response is successful (HTTP status code 200)
            if response.ok:
                print("Authentication successful.")
                cache.set("username", username)
                cache.set("password", password)

                return True, '/'
            else:
                print("Authentication failed.")
                return False, None
        except Exception as e:
            print(f"An error occurred: {e}")
            return False, None
    return False, None

