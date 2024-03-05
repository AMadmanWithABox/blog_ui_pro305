import dash
import requests
from dash import html, dcc, Input, callback, State, Output
import dash_mantine_components as dmc
from lib.templates.post_card import create_post_card

from config import cache  # Make sure this import is correct
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
from furl import furl


load_dotenv()
api_gateway = os.getenv('API_GATEWAY')

dash.register_page(__name__, path_template="/blog/<blog_id>", name="Blog Posts", redirect_from=["/blogs"])


def layout(blog_id=None):
    if blog_id is None:
        return dmc.Button("Create Post", id="create-post", color="blue", disabled=True)
    # TODO: Get blog by id
    blog_response = requests.get(f"{api_gateway}/blog/posts/{blog_id}", auth=HTTPBasicAuth(cache.get("username"),
                                                                                           cache.get("password")))

    blog = requests.get(f"{api_gateway}/blog/id/{blog_id}", auth=HTTPBasicAuth(cache.get("username"),
                                                                               cache.get("password"))).json()
    print("Blog:", blog)
    try:
        print("Blog Author:", blog['Items'][0]['author'])
    except:
        return html.Div(children=[])

    response = requests.get(f"{api_gateway}/user/username/{cache.get("username")}",
                            auth=HTTPBasicAuth(cache.get("username"), cache.get("password")))

    # print(response.json())

    author = response.json()['user_id']
    print("Current User:", author)
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

    filtered_posts = []
    if blog['Items'][0]['author'] == author:
        filtered_posts.append(dmc.Button(dmc.Anchor("Create Post", href=f"/create_post/{blog_id}", inherit=True)))

    #  Get blog posts by blog id unfiltered_posts = [{"title": f"title {i}", "content": (f"content {i}" for j in
    for i in range(len(posts)):
        filtered_posts.append(create_post_card(posts[i], blog_id))

    return html.Div(children=filtered_posts)

# @callback(
#     Output('url', 'pathname', allow_duplicate=True),
#     Input('create-post', 'n_clicks'),
#     State('url', 'pathname'),
#     prevent_initial_call=True
# )
# def create_post(n_clicks, pathname):
#     f = furl(pathname)
#     print(f'furl {f}')
#     blog_id = f.path.segments[1]
#     print(f'blog_id {blog_id}')
#     if n_clicks:
#         return f"/blog/create_post/{blog_id}"
#     return pathname
