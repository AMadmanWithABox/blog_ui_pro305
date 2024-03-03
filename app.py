import dash_auth
from dash import Dash, html, dcc
import dash_mantine_components as dmc

from lib.templates.appshell import create_appshell
from config import cache  # Import the cache

app = Dash(
    __name__,
    use_pages=True,
    update_title=None,
)

# Initialize the cache with the app's server
cache.init_app(app.server)

app.layout = dmc.MantineProvider(children=[dcc.Location(id='url'), create_appshell()])
server = app.server

if __name__ == '__main__':
    app.run(debug=True)
