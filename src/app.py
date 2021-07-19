from flask import Flask
app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    return '<h1>Hello!</h1>'


def todos():
    # supongamos que tienes cierta información (some_data) en una variable json
    some_data = { "label": "My first task", "done": False }

    # puedes convertir esa variable en un string json así
    json_text = flask.jsonify(some_data)

    # y luego puedes retorarla (return) en el response body así:
    return json_text



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)