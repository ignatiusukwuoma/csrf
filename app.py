import uuid
import logging
from flask import Flask, session, request, abort, render_template

logging.basicConfig(filename="app.log")

app = Flask(__name__)
# should be kept secret
app.secret_key = b'64ruhr7y4ic/fe>egu]'


@app.before_request
def protect_against_csrf():
    if request.method == 'POST':
        csrf_token = session.pop('csrf_token', None)
        if not csrf_token or csrf_token != request.form.get('csrftoken'):
            logging.warning("Attempt to send a request with incorrect token")
            abort(403)


@app.route('/', methods=['POST', 'GET'])
def index():
    username = None
    if request.method == 'POST':
        form_details = validate(request.form)
        username = form_details.get('username')
        return render_template('home.html', app_name="CSRF Protection", username=username)
    return render_template('home.html', app_name="CSRF Protection", username=username)


def validate(form_details):
    # carry out validation and sanitization of input
    return form_details


def generate_csrf_token():
    if 'csrf_token' not in session:
        random_string = str(uuid.uuid4)
        session['csrf_token'] = random_string
    return session['csrf_token']


app.jinja_env.globals['csrf_token'] = generate_csrf_token
