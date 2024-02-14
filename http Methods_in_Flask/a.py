from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        return render_template('df.html')
    elif request.method == 'POST':
        return render_template('l.html', data=request.form['data'])
    else:
        return 'Unsupported HTTP method.'

if __name__ == '__main__':
    app.run(debug=True)
