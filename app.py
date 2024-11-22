from flask import Flask

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# ルートURLにアクセスしたときに表示される内容
@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    # ローカルサーバーを起動
    app.run(debug=True)
