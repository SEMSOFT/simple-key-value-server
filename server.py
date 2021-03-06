import sys

from flask import Flask, request, abort, make_response
from flask_restful import Resource, Api

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

        return make_response({'status': 'success',
                              'result': {'key': key, 'value': value}}, 200)


class GetValue(Resource):
    def get(self):
        key = request.args.get('key')

        if key is None:
            abort(400)

        try:
            value = data_manager.get_last(key)
            return make_response({'status': 'success',
                                  'result': {'key': key, 'value': value}}, 200)
        except KeyError:
            abort(404)
        except:
            abort(500)


class GetHistory(Resource):
    def get(self):
        key = request.args.get('key')

        if key is None:
            abort(400)

        try:
            history = data_manager.get_history(key)
            return make_response({'status': 'success',
                                  'result': {'key': key, 'values': history}}, 200)
        except KeyError:
            abort(404)
        except:
            abort(500)


api.add_resource(SetValue, '/set')
api.add_resource(GetValue, '/get')
api.add_resource(GetHistory, '/history')

if __name__ == '__main__':
    args = sys.argv
    app.run(host=args[1], port=int(args[2]))
