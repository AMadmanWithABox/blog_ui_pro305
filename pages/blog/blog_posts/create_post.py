import dash
import requests
from dash import html, dcc, Input, callback, State, Output
import dash_mantine_components as dmc
from lib.templates.post_card import create_post_card

from config import cache  # Make sure this import is correct
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()
api_gateway = os.getenv('API_GATEWAY')

dash.register_page(__name__, path_template="/blog/<blog_id>", name="Blog Posts", redirect_from=["/blogs"])


def create_blog_page(blog_id):
    db_response = requests.get(api_gateway + f"/blog/{blog_id}", auth=HTTPBasicAuth(cache.get("username"), cache.get("password")))
    blog = db_response.json()
    posts = blog['posts']
    post_cards = [create_post_card(post) for post in posts]
    return html.Div(post_cards)


layout = html.Div(create_blog_page(blog_id))

