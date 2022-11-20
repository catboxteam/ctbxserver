from . import routes

@routes.route('/users')
def users():
    return "test"