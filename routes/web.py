"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    Get('/polls', 'PollsController@show').name('polls'),
]

from masonite.auth import Auth
ROUTES += Auth.routes()
