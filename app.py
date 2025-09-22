from os import path
from robyn import Robyn

app = Robyn(__file__)

# @app.get("/")
# def index():
#     return serve_html("index.html")

app.serve_directory(
    route="/",
    directory_path=path.join(path.dirname(__file__), "public"),
    index_file="index.html",
)


if __name__ == "__main__":
    app.start()
