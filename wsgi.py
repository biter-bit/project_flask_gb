from blog.app import create_app
from blog.extensions import db
from werkzeug.security import generate_password_hash

app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )


@app.cli.command("create-users")
def create_users():
    from blog.models import User
    admin = User(username='admin_2', is_staff=True, password='qqq', email='mixeil@mail.ru')

    db.session.add(admin)
    db.session.commit()

    print("done! created users:", admin)


# @app.cli.command("create-articles")
# def create_articles():
#     from blog.models import Articles
#     news = Articles(title='news_1', description='description_1', author=1)
#     db.session.add(news)
#     db.session.commit()