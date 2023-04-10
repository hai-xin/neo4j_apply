from flask import Blueprint

bp = Blueprint('view', __name__)  # 导入蓝图

from src.apps.user.views import *