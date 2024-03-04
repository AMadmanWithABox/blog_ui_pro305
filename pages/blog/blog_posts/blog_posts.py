import dash
import requests
from dash import html, dcc, Input, callback, State, Output
import dash_mantine_components as dmc

import app
from lib.templates.post_card import create_post_card

from config import cache  # Make sure this import is correct
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()
api_gateway = os.getenv('API_GATEWAY')

dash.register_page(__name__, path_template="/blog/<blog_id>", name="Blog Posts")


def layout(blog_id=None):
    if blog_id is None:
        return html.Div("No blog id provided.")
    logged_user = cache.get("username")

    blog_response = requests.get(f"{api_gateway}/blog/posts/{blog_id}", auth=HTTPBasicAuth(cache.get("username"),
                                                                                           cache.get(
                                                                                               "password"))).json()
    user_response = requests.get(f"{api_gateway}/user/id/{logged_user}", auth=HTTPBasicAuth(cache.get("username"),
                                                                                            cache.get(
                                                                                                "password"))).json()

    blog = requests.get(f"{api_gateway}/blog/id/{blog_id}", auth=HTTPBasicAuth(cache.get("username"),
                                                                               cache.get("password"))).json()
    blog_posts = blog_response.json()

    posts = []

    for post in blog_posts:
        post = {
            "blog_id": post["blog_id"],
            "Id": post["Id"],
            "title": post["title"],
            "content": post["content"]
        }
        posts.append(post)

    print(posts)

    #  Get blog posts by blog id unfiltered_posts = [{"title": f"title {i}", "content": (f"content {i}" for j in
    #  range(1, 1000))} for i in range(5)]
    filtered_posts = [create_post_card(post, blog_id) for post in posts]

    return html.Div(
        children=[dmc.Button(id="new-post-button"),
                  html.Div(hidden=True, id="page-context", children=[user_response["Id"], blog_response["author"]]),
                  filtered_posts])


# @callback(
#     Output("url", "pathname", allow_duplicate=True),
#     Output("new-post-button", "disabled", allow_duplicate=True),
#     Input("new-post-button", "n_clicks"),
#     Input("dummy", "dummy"),
#     State("url", "pathname"),
#     State("page-context", "children"),
#     config_prevent_initial_callbacks=True
# )
# def new_post(n_clicks, pathname, page_context):
#     if page_context[0] != page_context[1]:
#         return pathname, True
#     if n_clicks:
#         return "/blog/new-post", True
#     return pathname, False
