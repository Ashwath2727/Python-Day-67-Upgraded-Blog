from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField
from wtforms.validators import DataRequired


class AddPostForm(FlaskForm):

    title = StringField("Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    img_url = URLField("Image URL", validators=[DataRequired()])

    body = CKEditorField("Blog Content", validators=[DataRequired()])

    submit = SubmitField("Submit Post")