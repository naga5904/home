from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


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

