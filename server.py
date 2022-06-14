from flask import Flask, request, abort
import sys

app = Flask(__name__)

data = {}


@app.route('/')
def main_page():
    return 'Welcome to Home screen :)'


@app.route('/set', methods=['POST'])
def set_value():
    if request.method == 'POST':
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
    else:
        # throw an error
        abort(404)


@app.route('/get', methods=['GET'])
def get_last():
    if request.method == 'GET':
        key = request.args.get('key')

        if key is None:
            # throw an error
            abort(404)

        lst = data.get(key)
        if lst is None:
            return '%s is not exists' % key

        return lst[-1]
    else:
        # throw an error
        abort(404)


@app.route('/history', methods=['GET'])
def get_history():
    if request.method == 'GET':
        key = request.args.get('key')

        if key is None:
            # throw an error
            abort(404)

        lst = data.get(key)
        if lst is None:
            return '%s is not exists' % key

        return str(lst)
    else:
        # throw an error
        abort(404)


if __name__ == '__main__':
    args = sys.argv
    app.run(host=args[1], port=int(args[2]))