from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
  s = "abc"
  lis = ["a1", "a2", "a3"]
  dic = {"name":"John", "age":24}
  bl = True

  return render_template('index.html', s=s, lis=lis, dic=dic, bl=bl)

if __name__ == '__main__':
  app.run()
