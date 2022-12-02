#import function which is required to create a form
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateTimeField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired

#class where the form takes the values
class create_form (FlaskForm):
    id_field = HiddenField()
    title = StringField('title', validators=[DataRequired()],render_kw={"placeholder": "Title"})
    module_code = StringField('module_code', validators=[DataRequired()],render_kw={"placeholder": "Module Code"})
    deadline = DateTimeField('deadline',format = '%m-%d-%y',render_kw={"placeholder": " Deadline (DD-MM-YYY)"})
    description = TextAreaField('description',render_kw={"placeholder": "Description"})

    


