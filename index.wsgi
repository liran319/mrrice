import sae
from website import app

application = sae.create_wsgi_app(app)

