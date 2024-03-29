from flample.extensions import db
from flample.utils import JsonSerializer

users_groups = db.Table(
    "persons_groups",
    db.Column("person_id", db.Integer, db.ForeignKey("persons.id")),
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id")),
)


class UserJsonSerializer(JsonSerializer):
    pass


class Group(UserJsonSerializer, db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

    persons = db.relationship(
        "Person", secondary=users_groups, backref=db.backref("groups", lazy="dynamic")
    )

    def __str__(self):
        return "{0}-{1}".format(self.id, self.name)
