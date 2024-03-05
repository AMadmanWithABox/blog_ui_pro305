import dash
import requests
from dash import html, dcc, Input, callback, State, Output
import dash_mantine_components as dmc
from furl import furl
from lib.templates.post_card import create_post_card
from config import cache  # Make sure this import is correct
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()
api_gateway = os.getenv('API_GATEWAY')

dash.register_page(__name__, path_template="/create_blog", name="Create Blog")


layout = dmc.Container(
    children=[
        dmc.TextInput(
            label="Title",
            id="create-blog-title",
            placeholder="Enter the title of your Blog",
            required=True,
        ),
        dmc.Textarea(
            label="Category",
            id="create-blog-category",
            placeholder="Enter the category of your Blog",
            required=True,
        ),
        dmc.Textarea(
            label="Description",
            id="create-blog-description",
            placeholder="Enter the description of your Blog",
            required=True,
        ),
        dmc.Button(
            "Create Blog",
            id="create-blog-button",
            color="blue",
            variant="filled",
            mt=5
        ),
    ],
    style={'width': '100%'}
)


@callback(
    Output("create-blog-button", "loading", allow_duplicate=True),
    Output('url', 'pathname', allow_duplicate=True),
    Input("create-blog-button", "n_clicks"),
    State("create-blog-title", "value"),
    State("create-blog-category", "value"),
    State("create-blog-description", "value"),
    prevent_initial_call=True,
)
def create_blog(n_clicks, title, category, description):
    if n_clicks:
        print(f"Title: {title}, Category: {category}, Description: {description}")
        try:
            # Make a POST request with basic auth
            if cache.get("username") and cache.get("password"):
                response = requests.post(f"{api_gateway}/blog",
                                     json={"title": title, "category":category, "description": description},
                                     auth=HTTPBasicAuth(cache.get("username"), cache.get("password")))
            else:
                return True,
            return False, f"/blogs"
        except Exception as e:
            return False, f"/create_blog"
    return False, f"/create_blog"
