import requests
from dash import html
import dash_mantine_components as dmc
from requests.auth import HTTPBasicAuth
import os
from config import cache  # Make sure this import is correct
from dotenv import load_dotenv

load_dotenv()
api_gateway = os.getenv('API_GATEWAY')


def create_blog_card(blog):
    response = requests.get(f"{api_gateway}/user/id/{blog['author']}",
                            auth=HTTPBasicAuth(cache.get("username"), cache.get("password")))

    author = response.json()['username']

    return dmc.Anchor(
        dmc.Card(
            children=[
                dmc.CardSection(
                    dmc.Group(
                        children=[
                            dmc.Text(blog['title'], weight=500, size='lg'),
                            dmc.Group(
                                spacing="sm",
                                position="right",
                                children=[
                                dmc.Badge(author, color='teal', variant='light'),
                                dmc.Badge(blog['category'], color='blue', variant='light')
                                ],
                            )
                        ],
                        position="apart",
                        style={'width': '100%'},
                    ),
                    withBorder=True,
                    inheritPadding=True,
                    py="xs"
                ),
                dmc.Text(blog['description'], size='sm', mt="sm"),
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            w="100%",
            my="xl"
        ),
        href=f'/blog/{blog["Id"]}',
        underline=False,
        inherit=True
    )
