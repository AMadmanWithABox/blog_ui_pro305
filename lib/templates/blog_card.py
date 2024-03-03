from dash import html
import dash_mantine_components as dmc


def create_blog_card(blog):
    return dmc.Card(
        children=[
            dmc.CardSection(
                dmc.Group(
                    children=[
                        dmc.Text(blog['title'], weight=500, size='lg'),
                        dmc.Badge(blog['category'], color='blue', variant='light')
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
    )
