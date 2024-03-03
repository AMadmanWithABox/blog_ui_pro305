import dash
import dash_mantine_components as dmc

from lib.templates.blog_card import create_blog_card

dash.register_page(__name__, path='/blogs', name='Blogs')


def create_blogs_page():
    # TODO: get all the blogs from the database and store in the unfiltered_blogs variable
    unfiltered_blogs = [{"title": f"Blog {i}", "category": f"Category {i}", "description": f"Description {i}"} for i in range(1, 6)]
    filtered_blogs = [create_blog_card(blog) for blog in unfiltered_blogs]
    return filtered_blogs


layout = dmc.Container(children=create_blogs_page())
