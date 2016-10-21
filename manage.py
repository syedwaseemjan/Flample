from flample.api import create_app
from flample.extensions import db
from flample.models import Admin

app = create_app()


@app.cli.command()
def test():
    pass


@app.cli.command("create_db")
def create_db():
    db.create_all()


@app.cli.command("init_db")
def init_db():
    pass


@app.cli.command("create_admin")
def create_admin():
    admin = Admin()
    admin.email = "admin@flample.com"
    admin.password = "test123"
    admin.active = True
    db.session.add(admin)

    db.session.commit()


if __name__ == "__main__":
    pass
