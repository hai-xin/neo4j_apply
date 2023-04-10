from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.configs.db_config import MYSQL_NAME, MYSQL_PASSWORD, MYSQL_IP, MYSQL_PORT, MYSQL_DATABASE
from src.utils.db_connect import MyPymysqlPool

app = Flask(__name__)
# 发送文件最大时长
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# 连接mysql
# app.config[
# "SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{MYSQL_NAME}:{MYSQL_PASSWORD}@{MYSQL_IP}/{MYSQL_PORT}?charset=utf8'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_NAME}:{MYSQL_PASSWORD}@{MYSQL_IP}/{MYSQL_DATABASE}'
# 'mysql://root:密码@127.0.0.1:3306/dlz'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = True
app.config["SECRET_KEY"] = "ZHANGSan"

db = SQLAlchemy(app)

mysql_db = MyPymysqlPool()
