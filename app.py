from flask import Flask

app = Flask(__name__)

# Register dashboard routes
from dashboard.routes import *  # noqa: F401,F403

if __name__ == "__main__":
    app.run(debug=True)
