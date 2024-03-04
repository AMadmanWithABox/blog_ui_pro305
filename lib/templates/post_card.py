from dash import html
import dash_mantine_components as dmc


def create_post_card(post, blog_id):
    return dmc.Anchor(href=f'/blog/{blog_id}/post/{post['Id']}', children=[
        dmc.Card(
            children=[
                dmc.CardSection(
                    dmc.Group(
                        children=[
                            dmc.Text(post['title'], weight=500, size='lg'),
                        ],
                        position="apart",
                        style={'width': '100%'},
                    ),
                    withBorder=True,
                    inheritPadding=True,
                    py="xs"
                ),
                dmc.Text(post['content'], size='sm', mt="sm"),
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            w="100%",
            my="xl"
        )]
                      )
