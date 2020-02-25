import main
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'ghkjgfgdflgjldfkghldry'

class enter(FlaskForm):
    login = StringField('Enter Twitter Account', validators=[DataRequired()])
    button = SubmitField('Generate Map')

@app.route('/', methods= ['GET', 'POST'])

def login():
    """
    This is my flask application
    """
    form = enter()
    if request.method == 'POST':
        return main.friend_location(request.form.get('login'))
    else:
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(port = 3000)
