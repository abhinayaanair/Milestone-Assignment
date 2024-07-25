
from flask import Flask, render_template_string, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        return redirect(url_for('success', name=form.name.data))
    return render_template_string('''
        <form method="post">
            {{ form.hidden_tag() }}
            {{ form.name.label }} {{ form.name() }}
            {{ form.submit() }}
        </form>
    ''', form=form)

@app.route('/success/<name>')
def success(name):
    return f"Form submitted with name: {name}"

if __name__ == "__main__":
    app.run(debug=True)