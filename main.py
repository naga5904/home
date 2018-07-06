from flask import Flask,render_template,request
from socket import gethostname

app = Flask(__name__)

@app.route('/')
def index():
    host = '%s' % gethostname()
    print('hostname = %s',host)

    return render_template('index.html',host=host)


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        res = 'get_value.html'
    elif request.method == 'POST':
        res = 'post_value.html'

    print(res)
    return render_template(res)
#    return res

if __name__ == '__main__':
    app.run()

