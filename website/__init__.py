from flask import Flask


app = Flask(__name__)
app._static_folder = r"static/"
app._assets_folder = r"assets/"

import views
