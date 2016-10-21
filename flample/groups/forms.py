from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Optional

__all__ = ["NewGroupForm", "UpdateGroupForm"]


class NewGroupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])


class UpdateGroupForm(FlaskForm):
    name = StringField("Name", validators=[Optional()])
