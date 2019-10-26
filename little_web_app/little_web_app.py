from flask import Flask


app = Flask(__name__)


@app.route('/')
def base_route():
    return 'Hello World'

@app.route('/hello/<username>')
def user_hello(username):
    return 'Hello %s' % username

@app.route('/hellos/<num_hello>')
def count_hello(num_hello):
    try:
        hello_count = int(num_hello)
    except ValueError:
        return 'Please Use a Valid Integer'

    message = ''

    for x in range(0,hello_count):
        message += ('hello\n\n')
    
    return message

if __name__ == "__main__":
    app.run()