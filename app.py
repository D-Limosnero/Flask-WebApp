from flask import Flask, render_template, request, redirect, url_for, flash, abort
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Allows messages to be securely transmitted between host and client
app.secret_key = '5ad867d8sh6ts68578hgss6g67'

@app.route('/')
def home():
    return render_template('home.html')

# By default, flask enables only GET requests
@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method== 'POST':
        urls = {}
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] in urls.keys():
            flash('Shortened URL already taken. Please select another name')
            return redirect(url_for('home'))
        
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url':request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename) # workzeug utils to prevent bad filename
            f.save('C:/Users/dean/Documents/GitHub/Flask-WebApp/static/user_files/' + full_name)
            urls[request.form['code']] = {'file':full_name}

        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))
    
@app.route('/<string:code>') # look for after the first slash on the website any string and put it in a variable "code"
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file'])) # look in static
    return abort(404) # import abort for this functionality: use error handler to customize page

@app.errorhandler(404)
def page_not_fount(error):
    return render_template('page_not_found.html'), 404

