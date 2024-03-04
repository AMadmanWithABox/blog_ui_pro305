import dash
from dash import html, Output, Input, callback, page_container, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

GITHUB_LINK = "https://github.com/AMadmanWithABox/blog_ui_pro305"
APP_NAME = "Blog App"
APP_ABBR = "B"


def get_icon(icon):
    return DashIconify(icon=icon, height=16)


def create_home_link(label):
    """
    Creates a hyperlink for the home page
    :param label: The text to display
    :return: A hyperlink using the dmc Anchor component
    """
    return dmc.Anchor(
        label,
        href="/",
        underline=False,
        className="link",
        inherit=True
    )


def create_header_link(icon, href, size=22, color="indigo"):
    return dmc.Anchor(
        dmc.ThemeIcon(
            DashIconify(
                icon=icon,
                width=size,
            ),
            variant="outline",
            radius=30,
            size=36,
            color=color,
        ),
        href=href,
        target="_blank",
    )


def create_header_grid_group_content():
    return [
        dmc.Burger(opened=False, id="burger-button", style={"z-index": 900000}),
        dmc.Title(
            children=[
                dmc.MediaQuery(
                    create_home_link(APP_NAME),
                    smallerThan="lg",
                    styles={"display": "none"},
                ),
                dmc.MediaQuery(
                    create_home_link(APP_ABBR),
                    largerThan="lg",
                    styles={"display": "none"},
                )
            ],
            order=1,
            weight=100,
            inline=1,
            align='center'
        )]


def create_header_grid_content():
    return [
        dmc.Col(
            span="auto",
            display="flex",
            children=[
                dmc.Group(
                    align="center",
                    style={"width": "100%"},
                    children=create_header_grid_group_content()),
            ],
            pt=12
        ),
        dmc.Col(
            span="auto",
            display="center",
            children=[
                dmc.Title(
                    id="header-page-name",
                    children="",
                    order=1,
                    inline=1,
                    align='center',
                    weight=400,
                    style={"width": "100%", "text-align": "center"}
                ),
            ],
            pt=12
        ),
        dmc.Col(
            span="auto",
            display="center",
            style={"width": "100%"},
            children=dmc.Group(
                position="right",
                align="center",
                style={"width": "100%"},
                children=[
                    create_header_link(
                        "radix-icons:github-logo",
                        GITHUB_LINK,
                    ),
                ]),
            pt="12"
        )]


def create_header_content():
    return [
        dcc.Location(id="current-location", refresh=True),
        dmc.Stack(
            justify="center",
            style={"height": 70},
            children=dmc.Grid(
                align="center",
                children=create_header_grid_content()
            )
        )]


def create_header():
    return dmc.Header(
        height=70,
        fixed=True,
        px=25,
        children=create_header_content()
    )


def create_sidebar():
    pages = dash.page_registry.values()

    return html.Div(
        children=[
            dmc.Drawer(
                size=300,
                withCloseButton=False,
                closeOnClickOutside=False,
                closeOnEscape=False,
                id="sidebar-drawer",
                withOverlay=False,
                children=[
                    dmc.NavLink(label="Home", href="/", icon=DashIconify(icon="bi:house-door-fill"))
                ].__add__([
                    dmc.NavLink(
                        label=page.get('name'),
                        href=page.get('path'),
                    ) for page in pages if page.get('name') != "Blog Posts"
                ])
            ),
        ])


def create_appshell():
    return dmc.MantineProvider(
        dmc.MantineProvider(
            inherit=True,
            children=[
                dmc.NotificationsProvider(
                    [
                        create_header(),
                        create_sidebar(),
                        html.Div(
                            dmc.Container(size="80%", pt=90, children=page_container),
                            id="wrapper",
                        ),
                    ]
                )
            ]
        ),

        theme={
            "black": "#2d4b81",
            "primaryColor": 'blue',
            "styles": {"mantineProvider": {
                "backgroundColor": "blue",
            }},
            "backgroundColor": "blue",
            # add your colors
            "colors": {
                "deepBlue": [
                    "#eef3ff",
                    "#dce4f5",
                    "#b9c7e2",
                    "#94a8d0",
                    "#748dc1",
                    "#5f7cb8",
                    "#5474b4",
                    "#44639f",
                    "#39588f",
                    "#2d4b81"
                ],  # 10 color elements
            },
            "shadows": {
                # other shadows (xs, sm, lg) will be merged from default theme
                "md": "1px 1px 3px rgba(0,0,0,.25)",
                "xl": "5px 5px 3px rgba(0,0,0,.25)",
            },
            "headings": {
                "fontFamily": "Roboto, sans-serif",
                "sizes": {
                    "h1": {"fontSize": 30},
                },
            },
        },
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )


@callback(
    Output("header-page-name", "children"),
    Input("url", "pathname"),
)
def update_header(pathname):
    pages = dash.page_registry.values()
    for page in pages:
        if page["path"] == pathname:
            return page["name"]
    return ""


@callback(
    Output("sidebar-drawer", "opened"),
    Input("burger-button", "opened"),
    config_prevent_initial_callbacks=True,
)
def open_sb(opened):
    return opened
