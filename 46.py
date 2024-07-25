
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        file.save(f'./uploads/{file.filename}')
        return 'File uploaded successfully!'
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)