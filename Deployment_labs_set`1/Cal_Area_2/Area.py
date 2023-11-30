from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_rectangle.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    length = float(request.form['length'])
    width = float(request.form['width'])

    area = length * width
    perimeter = 2 * (length + width)

    return render_template('index_rectangle.html', length=length, width=width, area=area, perimeter=perimeter)

if __name__ == '__main__':
    app.run(debug=True)
