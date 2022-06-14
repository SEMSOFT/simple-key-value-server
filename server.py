from flask import Flask, request, abort
from flask_restful import Resource, Api
import sys

app = Flask(__name__)
api = Api(app)

data = {}


class SetValue(Resource):
    def post(self):
        key = request.form.get('key')
        value = request.form.get('value')
        if key is None or value is None:
            abort(404)
            # throw an error

        lst = data.get(key)
        if lst is None:
            lst = []
        lst.append(value)

        data.update({key: lst})

        return '(%s, %s) has been added to data list' % (key, value)


class GetValue(Resource):
    def get(self):
        key = request.args.get('key')

        if key is None:
            # throw an error
            abort(404)

        lst = data.get(key)
        if lst is None:
            return '%s is not exists' % key

        return lst[-1]


class GetHistory(Resource):
    def get(self):
        key = request.args.get('key')

        if key is None:
            # throw an error
            abort(404)

        lst = data.get(key)
        if lst is None:
            return '%s is not exists' % key

        return str(lst)


api.add_resource(SetValue, '/set')
api.add_resource(GetValue, '/get')
api.add_resource(GetHistory, "/history")


if __name__ == '__main__':
    args = sys.argv
    app.run(host=args[1], port=int(args[2]))
