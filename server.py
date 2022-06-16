from flask import Flask, request, abort, jsonify
from flask_restful import Resource, Api
import sys

app = Flask(__name__)
api = Api(app)

data = {}


class SetValue(Resource):
    def post(self):
        json_data = request.json
        key = json_data.get('key')
        value = json_data.get('value')

        if key is None or value is None:
            abort(400)

        lst = data.get(key)
        if lst is None:
            lst = []
        lst.append(value)

        data.update({key: lst})

        return '(%s, %s) has been added to data list' % (key, value), 201


class GetValue(Resource):
    def get(self):
        key = request.args.get('key')

        if key is None:
            abort(400)

        lst = data.get(key)
        if lst is None:
            abort(404)

        return jsonify({'value': lst[-1]})


class GetHistory(Resource):
    def get(self):
        key = request.args.get('key')

        if key is None:
            abort(400)

        lst = data.get(key)
        if lst is None:
            abort(404)

        return jsonify({'values': lst})


api.add_resource(SetValue, '/set')
api.add_resource(GetValue, '/get')
api.add_resource(GetHistory, '/history')

if __name__ == '__main__':
    args = sys.argv
    app.run(host=args[1], port=int(args[2]))
