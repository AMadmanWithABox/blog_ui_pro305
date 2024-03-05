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

dash.register_page(__name__, path_template="/blog/<blog_id>/create_post", name="Create Post")


def load_layout():
    print("Loading layout")
    return dmc.Container(
        children=[
            dmc.TextInput(
                label="Title",
                id="title",
                placeholder="Enter the title of your post",
                required=True,
            ),
            dmc.TextInput(
                label="Category",
                id="category",
                placeholder="Enter the category of your post",
                required=True,
            ),
            dmc.Textarea(
                label="Content",
                id="content",
                placeholder="Enter the content of your post",
                required=True,
            ),
            dmc.Button(
                "Create Post",
                id="create-post-button",
                color="blue",
                variant="filled",
                mt=5
            ),
        ],
        style={'width': '100%'}
    )


layout = load_layout


@callback(
    Output("create-post-button", "loading"),
    Output('url', 'pathname', allow_duplicate=True),
    Input("create-post-button", "n_clicks"),
    State("title", "value"),
    State("category", "value"),
    State("content", "value"),
    State('url', 'pathname'),
    prevent_initial_call=True,
)
def create_post(n_clicks, title, category, content, url):
    f = furl(url)
    # print(f)
    blog_id = f.args['blog_id']

    if n_clicks:
        print(f"Title: {title}, Category: {category}, Content: {content}")
        try:
            # Make a POST request with basic auth
            response = requests.post(f"{api_gateway}/post",
                                     json={"blog_id": blog_id, "title": title, "content": content},
                                     auth=HTTPBasicAuth(cache.get("username"), cache.get("password")))
            print(response.json())
            return False, f"/blog/{blog_id}"
        except Exception as e:
            print(e)
            return False, f"/blog/{blog_id}/create_post"
    return False, f"/blog/{blog_id}/create_post"
