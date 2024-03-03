import dash_auth

from lib.templates.appshell import create_appshell
from dash import Dash, html, dcc
import dash_mantine_components as dmc

VALID_USERNAME_PASSWORD_PAIRS = {
    'connor1': 'abc123',
    'carter1': 'abc123',
    'cantera1': 'abc123'
}

app = Dash(
    __name__,
    use_pages=True,
    update_title=None,
)

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = dmc.MantineProvider(children=[dcc.Location(id='url'), create_appshell()])
server = app.server

if __name__ == '__main__':
    app.run(debug=True)
