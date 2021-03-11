from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField


class FibonacciSequenceForm(FlaskForm):
    """Fibonacci Forms"""

    number = IntegerField("Insert Number")
    submit = SubmitField("Submit")
