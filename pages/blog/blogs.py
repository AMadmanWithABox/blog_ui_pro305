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

# Define a container to hold the dynamic content
layout = html.Div(id='blogs-content')

# Use a callback to populate the container
@callback(
    Output('blogs-content', 'children'),
          [Input('url', 'pathname')]
)
def update_blogs_content(pathname):
    if cache.get('username'):
        response = requests.get(api_gateway + "/blog", auth=HTTPBasicAuth(cache.get("username"), cache.get("password")))
        # response_dict = {item['Id']: item for item in response.json()}

        # Perform your cache-dependent logic here
        # unfiltered_blogs = [{"title": f"Blog {i}", "category": f"Category {i}", "description": f"Description {i}"} for i in range(1, 6)]
        filtered_blogs = [create_blog_card(blog) for blog in response.json()]
    else:
        # Handle the case where cache data is not available
        filtered_blogs = [html.P("No blogs available or user not logged in.")]

    return dmc.Container(children=filtered_blogs)
