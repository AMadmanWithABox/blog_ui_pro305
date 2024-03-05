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

dash.register_page(__name__, path_template="/update_post/<blog_id>/<post_id>", name="Update Post")


layout = dmc.Container(
        children=[
            dmc.TextInput(
                label="Title",
                id="title",
                placeholder="Enter the title of your post",
                required=True,
            ),
            dmc.Textarea(
                label="Content",
                id="content",
                placeholder="Enter the content of your post",
                required=True,
            ),
            dmc.Button(
                "Update Post",
                id="update-post-button",
                color="blue",
                variant="filled",
                mt=5
            ),
        ],
        style={'width': '100%'}
    )


@callback(
    Output("title", "value"),
    Output("content", "value"),
    Input('url', 'pathname'),
    State("title", "value"),
    State("content", "value")
)
def initial_fill(url, title, content):
    if title != "":
        return title, content
    f = furl(url)
    # print(f)
    blog_id = f.path.segments[1]
    post_id = f.path.segments[2]
    post = requests.get(f"{api_gateway}/post/id/{post_id}", auth=HTTPBasicAuth(cache.get("username"),
                                                                                   cache.get("password"))).json()
    print(post)
    return post['title'], post['content']


@callback(
    Output("update-post-button", "loading"),
    Output('url', 'pathname', allow_duplicate=True),
    Input("update-post-button", "n_clicks"),
    Input("title", "value"),
    Input("content", "value"),
    State('url', 'pathname'),
    prevent_initial_call=True,
)
def create_post(n_clicks, title, content, url):
    f = furl(url)
    # print(f)
    blog_id = f.path.segments[1]
    post_id = f.path.segments[2]
    if n_clicks:
        print(f"Title: {title}, Content: {content}")
        try:
            # Make a POST request with basic auth
            if cache.get("username") and cache.get("password"):
                response = requests.put(f"{api_gateway}/post",
                                         json={"post_id": post_id, "title": title, "content": content},
                                         auth=HTTPBasicAuth(cache.get("username"), cache.get("password")))
            else:
                return True,
            return False, f"/blog/{blog_id}"
        except Exception as e:
            return False, f'/update_post/{blog_id}/{post_id}'
    return False, f'/update_post/{blog_id}/{post_id}'
