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

dash.register_page(__name__, path_template="/blog/<blog_id>", name="Blog Posts", redirect_from=["/blogs"])


@callback(

)
def layout(blog_id):
    # TODO: Get blog by id
    blog_response = requests.get(f"{api_gateway}/blog/posts/{blog_id}", auth=HTTPBasicAuth(cache.get("username"),
                                                                                           cache.get("password")))
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

    # TODO: Get blog posts by blog id
    unfiltered_posts = [{"title": f"title {i}", "content": (f"content {i}" for j in range(1, 1000))} for i in range(5)]
    filtered_posts = [create_post_card(post) for post in unfiltered_posts]
