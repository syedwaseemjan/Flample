from flask import Blueprint, request

from flample.api import route
from flample.exceptions import FlampleError, FlampleFormError
from flample.forms import NewPersonForm, UpdatePersonForm
from flample.services import _persons

bp = Blueprint("person", __name__, url_prefix="/persons")


@route(bp, "/")
def list():
    """Returns a list of user instances."""
    return _persons.all()


@route(bp, "/", methods=["POST"])
def new():
    """Creates a new person. Returns the new person instance."""
    form = NewPersonForm()
    if form.validate_on_submit():
        return _persons.create_person(form)
    raise FlampleFormError(form.errors)


@route(bp, "/<person_id>")
def show(person_id):
    """Returns a person instance."""
    person = _persons.get_or_404(person_id)
    return _persons._serialize(person)


@route(bp, "/<person_id>/update", methods=["POST"])
def update(person_id):
    """Updates a person. Returns the updated person instance."""
    form = UpdatePersonForm()
    if form.validate_on_submit():
        return _persons.update(_persons.get_or_404(person_id), **request.json)
    raise FlampleFormError(form.errors)


@route(bp, "/<person_id>/delete")
def delete(person_id):
    """Deletes a person. Returns a 204 response."""
    _persons.delete(_persons.get_or_404(person_id))
    return None, 204


@route(bp, "/<int:person_id>/groups")
def groups(person_id):
    return {}


@route(bp, "/search", methods=["POST"])
def search():
    """Returns a person instance."""
    text = request.form.get("text")
    person = _persons.search(text)
    if not person:
        raise FlampleError("No Result Found")
    return _persons._serialize(person)
