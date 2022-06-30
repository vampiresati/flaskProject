from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/hello')
def hello1():
    return 'Hello, World'
@app.route('/int/<int:roll_number>')
def student(roll_number):
    return f"rollnumber, {escape(roll_number)}!"
@app.route('/string/<string:name>')
def student_name(name):
    return f"name, {escape(name)}!"
@app.route('/float/<float:fee>')
def student_fee(fee):
    return f"fee, {escape(fee)}!"
@app.route('/path/<path:p>')
def studentpath(p):
    return f"path, {escape(p)}!"
@app.route('/uuid/<uuid:p>')
def studentuuid(p):
    return f"uuid, {escape(p)}!"
if __name__ == '__main__':
    app.run()
