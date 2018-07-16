"""A microservice app to provide current unix time."""

import os
import time

from flask import Flask


app = Flask(__name__)


@app.route('/')
def get_unit_time():
    return str(time.time()).split('.')[0]


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
