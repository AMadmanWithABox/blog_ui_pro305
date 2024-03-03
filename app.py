import dash_auth

from lib.templates.appshell import create_appshell
from dash import Dash, html, dcc
import dash_mantine_components as dmc

app = Dash(
    __name__,
    use_pages=True,
    update_title=None,
)

app.layout = dmc.MantineProvider(children=[dcc.Store(id='session-store', storage_type='session'), dcc.Location(id='url'), create_appshell()])
server = app.server

if __name__ == '__main__':
    app.run(debug=True)
