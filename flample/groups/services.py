from flample.extensions import Service
from flample.models import Group
from flample.exceptions import FlampleError


class GroupsService(Service):
    __model__ = Group

    def __init__(self, *args, **kwargs):
        super(GroupsService, self).__init__(*args, **kwargs)

    def add_person(self, group, user):
        if user in group.persons:
            raise FlampleError("Person exists")
        group.persons.append(user)
        return self.save(group), user

    def remove_person(self, group, user):
        if user not in group.persons:
            raise FlampleError("Invalid person")
        group.persons.remove(user)
        return self.save(group), user

    def add_group(self, group, user):
        if user in group.persons:
            raise FlampleError("Person exists")
        group.persons.append(user)
        return self.save(group), user

    def remove_group(self, group, user):
        if user not in group.persons:
            raise FlampleError("Invalid person")
        group.persons.remove(user)
        return self.save(group), user
