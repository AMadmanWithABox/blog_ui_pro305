from lib.templates.appshell import create_appshell
from dash import Dash

app = Dash(
    __name__,
    use_pages=True,
    update_title=None,
)

app.layout = create_appshell()
server = app.server

if __name__ == '__main__':
    app.run(debug=True)
