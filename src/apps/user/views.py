from flask import request, jsonify

from src import db, mysql_db
from src.models.users_models import User
from src.apps.user import bp
from src.utils.prepar_return import prepare_for_return


@bp.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        name = request.args.get('name')
        return {"res": "data"}
    elif request.method == 'POST':
        data = request.json.get("name")
        print(data)
        return {'res': 'datas'}


@bp.route('/add', methods=["POST"])
def add_user():
    name = request.json.get("name")
    age = request.json.get("age")
    user = User(name=name, age=age)
    try:
        sql = "select * from users"
        res = mysql_db.getAll(sql)
        print(res)
        db.session.add(user)
        db.session.commit()
        return jsonify(prepare_for_return(user.to_dict()))
    except:
        return jsonify(prepare_for_return(data={}, state="false"))
