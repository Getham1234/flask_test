from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    #return("Hello World!")
    
    a = "My name is Geetham"
    return """
    <html>
        <head>
            <title> Home </title>
        </head>
        <body>
            <div><a href ="/about"> About </a></div>
            <div><a href ="/test"> Test Page <a></div>
            <div><a href ="/test2"> Test2 Page <a></div>""" 
    a
    """

    </body>
</html>
 
"""

@app.route('/about')
def about():
    return("About")

@app.route('/test')
def test():
    user = {'username': 'Geetham'}
    age = 12
    return render_template('test.html', user = user, age = age)

@app.route('/test2')
def test2():
    user = {'username': 'RandoRobo'}
    sample_data = [
    {
    'author': {'username': 'RandoRobo'},
    'body': 'Hello!'
    },
    {
    'author': {'username': 'Geetham'},
     'body': 'Welcome to Flask!'
    }
    ]
    return render_template('test2.html', user=user, sample_data=sample_data)