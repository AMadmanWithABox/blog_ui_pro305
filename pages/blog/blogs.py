from random import random

import dash
from dash import html, dcc, Input, callback, State, Output
import dash_mantine_components as dmc
import requests
from dotenv import load_dotenv
import os
from config import cache  # Make sure this import is correct
from requests.auth import HTTPBasicAuth

from lib.templates.blog_card import create_blog_card

dash.register_page(__name__, path='/blogs', name='Blogs')

load_dotenv()
api_gateway = os.getenv('API_GATEWAY')


def create_blogs_content():
    if cache.get('username'):
        db_response = requests.get(api_gateway + "/blog",
                                   auth=HTTPBasicAuth(cache.get("username"), cache.get("password")))
        blogs = db_response.json()

        # Perform your cache-dependent logic here
        filtered_blogs = [create_blog_card(blog) for blog in blogs]
    else:
        # Handle the case where cache data is not available
        filtered_blogs = [html.P(f"No blogs available or user not logged in.")]

    return dmc.Container(id='blogs-content', children=filtered_blogs)


layout = create_blogs_content()
