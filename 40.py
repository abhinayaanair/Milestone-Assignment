
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form['data']
        return f"Data received: {data}"
    return '''
        <form method="post">
            <input type="text" name="data">
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
