import dash
import requests
import dash_mantine_components as dmc
from dash import html, dcc, Input, callback, State, Output
from furl import furl

from lib.templates.post_card import create_post_card

from config import cache  # Make sure this import is correct
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()
api_gateway = os.getenv('API_GATEWAY')

dash.register_page(__name__, path_template="/blog/<blog_id>/post/<post_id>", name="Blog Post")


layout = dmc.Stack(
    # children=[
    #     dmc.Text(post['title'], weight=500, size='xl'),
    #     dmc.Text(post['content'], size='lg'),
    # ],
    children=[
        dmc.Text(id="blog-title", weight=500, size='xl'),
        dmc.Text(id="blog-content", size='lg'),
        dmc.Group(children=[
            dmc.Button("Delete Post", id="delete-button"),
            dmc.Button("update", id="update-button")
        ])
    ],
    style={'width': '100%'}
)


@callback(
    Output("blog-title", "children"),
    Output("blog-content", "children"),
    Output('update-button', 'children'),
    Input("url", "pathname")
)
def get_post(url):
    f = furl(url)
    blog_id = f.path.segments[1]
    post_id = f.path.segments[3]
    post = requests.get(f"{api_gateway}/post/id/{post_id}", auth=HTTPBasicAuth(cache.get("username"),
                                                                               cache.get("password"))).json()
    update_children = dmc.Anchor("Update", href=f'/update_post/{blog_id}/{post_id}')
    return post["title"], post["content"], update_children


@callback(
    Output("delete-button", "loading"),
    Output('url', 'pathname', allow_duplicate=True),
    Input("delete-button", "n_clicks"),
    State('url', 'pathname'),
    prevent_initial_call=True,
    suppress_callback_exceptions=True
)
def delete_post(n_clicks, url):
    f = furl(url)
    # print(f)
    blog_id = f.path.segments[1]
    post_id = f.path.segments[3]
    print("in delete_post")
    if n_clicks:
        try:
            # Make a POST request with basic auth
            if cache.get("username") and cache.get("password"):
                response = requests.delete(f"{api_gateway}/post/id/{post_id}",
                                           auth=HTTPBasicAuth(cache.get("username"), cache.get("password")))
            else:
                return True, f"/blog/{blog_id}"
            return False, f"/blog/{blog_id}"
        except Exception as e:
            print(e)
            return False, f"/blog/{blog_id}/post/{post_id}"
    return False, f"/blog/{blog_id}/post/{post_id}"



