from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enlace_ttt')
def enlace_ttt():
    return render_template('enlace_ttt.html')

@app.route('/enlace_bt3')
def enlace_bt3():
    return render_template('enlace_bt3.html')

if __name__ == '__main__':
    app.run(debug=True)
