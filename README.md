References: https://www.youtube.com/watch?v=YUVhYhx75qw

To start flask app:
set FLASK_APP="name of app"
flask run

To enable debug mode:
set FLASK_ENV=1
flask run

if there is an app.py, flask will recognize this as the default

render_template function facilitated by Jinja, a full-featured template engine for Python

{{ varname }} in html file allows us to pass variables from jinja/flask to html

In general {{}} syntax is jinja code

session is used to take advantage of cookies