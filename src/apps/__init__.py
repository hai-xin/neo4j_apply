from flask_sqlalchemy import SQLAlchemy

from src import app
from src.apps import user



def create_app():
    # app.register_blueprint(user.bp)  # 注册user下的蓝图
    # # app.register_blueprint(views.bp)

    # 注册蓝图 url_prefix指定url前缀
    app.register_blueprint(user.bp, url_prefix='/users')
    return app
