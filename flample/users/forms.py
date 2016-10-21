from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms import (
    Form as WTForm,
    PasswordField,
    BooleanField,
    FieldList,
    HiddenField,
    FormField,
)
from wtforms.validators import DataRequired, Length, Optional
from flample.models import Admin, Group
from wtforms_sqlalchemy.fields import QuerySelectField

__all__ = ["LoginForm", "NewPersonForm", "UpdatePersonForm"]


def get_groups():
    return Group.query.all()


class LoginForm(FlaskForm):
    email = StringField("", validators=[DataRequired("Email is mandatory.")])
    password = PasswordField(
        "",
        validators=[
            DataRequired("Password is mandatory."),
            Length(min=6, message="Password length " "must be >5."),
        ],
    )
    remember = BooleanField("Remember Me")

    def validate(self):
        self.flash = False
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        query = Admin.query.filter(Admin.email.ilike(self.email.data))
        user = query.first()
        if user is None:
            self.flash = True
            return False

        if not user.match_password(self.password.data):
            self.flash = True
            return False

        self.user = user
        return True


class AddressForm(WTForm):
    address_id = HiddenField()
    name = StringField()


class EmailForm(WTForm):
    email_id = HiddenField()
    name = StringField()


class PhoneForm(WTForm):
    phone_id = HiddenField()
    name = StringField()


class GroupForm(WTForm):
    group_id = HiddenField()
    name = QuerySelectField(query_factory=get_groups, blank_text="")


class NewPersonForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])

    addresses = FieldList(FormField(AddressForm), min_entries=1)
    emails = FieldList(FormField(EmailForm), min_entries=1)
    phones = FieldList(FormField(PhoneForm), min_entries=1)
    groups = FieldList(FormField(GroupForm), min_entries=1)


class UpdatePersonForm(FlaskForm):
    name = StringField("Name", validators=[Optional()])
    address = StringField("Address", validators=[Optional()])
    city = StringField("City", validators=[Optional()])
    state = StringField("State", validators=[Optional()])
    zip_code = StringField("Zip Code", validators=[Optional()])
