# -*- coding: utf-8 -*-
from flask.ext.scss import Scss
from website import app

if __name__ == '__main__':
    app.debug = True
    Scss(app, static_dir='static', asset_dir='assets')
    app.run(port=4001, debug=True)
