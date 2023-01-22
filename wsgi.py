from blog.app import create_app
from blog.models.database import db

app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    from blog.models.user import User
    admin = User(username='admin', is_staff=True)
    james = User(username="james")

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print("done! created users:", admin, james)

# @app.cli.command("create-articles")
# def create_articles():
#     from blog.models.user import Articles
#     news = Articles(title='news_1', description='description_1')