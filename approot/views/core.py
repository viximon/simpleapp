from flask import render_template
from flask.ext.classy import FlaskView

from approot import app


class Root(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('root.html')


class Snippet(FlaskView):
    def index(self):
        return render_template('snippet.html')


class Foo(FlaskView):
    def blahblah(self):
        a = 1 + 2
        b = 3 + 4
        return c

# URL rules
Root.register(app)
Snippet.register(app)
