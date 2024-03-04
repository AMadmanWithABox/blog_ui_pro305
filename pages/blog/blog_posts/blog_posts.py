import dash
from dash import clientside_callback

from lib.templates.post_card import create_post_card

dash.register_page(__name__, path_template="/blog/<blog_id>", name="Blog Posts", redirect_from=["/blogs"])


def layout(blog_id):
    # TODO: Get blog by id
    blog = {
        "title": f"Blog {blog_id}",
        "category": f"Category {blog_id}",
        "description": f"Description {blog_id}",
        "id": blog_id
    }
    # TODO: Get blog posts by blog id
    unfiltered_posts = [{"title": f"title {i}", "content": (f"content {i}" for j in range(1, 1000))} for i in range(5)]
    filtered_posts = [create_post_card(post) for post in unfiltered_posts]
