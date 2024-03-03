from lib.templates.appshell import create_appshell
from dash import Dash
import dash_core_components as dcc

app = Dash(
    __name__,
    use_pages=True,
    update_title=None,
)

app.layout = [dcc.Location('url'), create_appshell()]
server = app.server

if __name__ == '__main__':
    app.run(debug=True)
