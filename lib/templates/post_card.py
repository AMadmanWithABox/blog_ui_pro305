from dash import html
import dash_mantine_components as dmc


def create_post_card(blog):
    return dmc.Card(
        children=[
            dmc.CardSection(
                dmc.Group(
                    children=[
                        dmc.Text(blog['title'], weight=500, size='lg'),
                    ],
                    position="apart",
                    style={'width': '100%'},
                ),
                withBorder=True,
                inheritPadding=True,
                py="xs"
            ),
            dmc.Text(blog['content'], size='sm', mt="sm"),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        w="100%",
        my="xl"
    )
