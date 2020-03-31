from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('Homework1.html')

@app.route('/music')
def music():
   return '<h1>Music</h1>'

@app.route('/music/top100')
def music100():
   return '<h1>Music top 100</h1>'

# route('/')로 오면 home 함수를 실행해서 이걸 줄거야!
# 서버는 이미 경로에 따른


print("시작전")
app.run('0.0.0.0',port=5000,debug=True)
# debug=True : 개발 중인 상태이니 자주 바뀔거야, 그러니 자동으로 업데이트해줘!
print("시작후")
