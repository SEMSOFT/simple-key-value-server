from flask import Flask, request, abort, jsonify
from flask_restful import Resource, Api
import sys
from datamanager import DataManager

app = Flask(__name__)
api = Api(app)

data_manager = DataManager()


class SetValue(Resource):
    def post(self):
        json_data = request.json
        key = json_data.get('key')
        value = json_data.get('value')

        if key is None or value is None:
            abort(400)

        data_manager.append(key, value)

        return {'message': '(%s, %s) has been added to data list' % (key, value)}, 201


class GetValue(Resource):
    def get(self):
        key = request.args.get('key')

        if key is None:
            abort(400)

        try:
            value = data_manager.get_last(key)
            return jsonify({'value': value})
        except:
            abort(404)


class GetHistory(Resource):
    def get(self):
        key = request.args.get('key')

        if key is None:
            abort(400)

        try:
            history = data_manager.get_history(key)
            return jsonify({'values': history})
        except:
            abort(404)


api.add_resource(SetValue, '/set')
api.add_resource(GetValue, '/get')
api.add_resource(GetHistory, '/history')

if __name__ == '__main__':
    args = sys.argv
    app.run(host=args[1], port=int(args[2]))
