from flask import Flask, render_template, request, redirect
from algoritm import algoritm
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        text = request.form['text']
        ans = algoritm(text)
        if ans[1]:
            return redirect(ans[2].string)
        else:
            return render_template('index.html', text=ans[0])
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
