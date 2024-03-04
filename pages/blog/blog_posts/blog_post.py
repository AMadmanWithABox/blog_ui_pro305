import dash
import requests
from dash import html, dcc, Input, callback, State, Output

from lib.templates.post_card import create_post_card

from config import cache  # Make sure this import is correct
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()
api_gateway = os.getenv('API_GATEWAY')

dash.register_page(__name__, path_template="/blog/<blog_id>/post/<post_id>", name="Blog Posts", redirect_from=["/blogs"])


def layout(blog_id=None, post_id=None):
    if blog_id is None:
        return html.Div("No blog id provided.")
    if post_id is None:
        return html.Div("No post id provided.")

    post = requests.get(f"{api_gateway}/blog/posts/{blog_id}/{post_id}", auth=HTTPBasicAuth(cache.get("username"),
                                                                                             cache.get("password"))).json()

    return post

