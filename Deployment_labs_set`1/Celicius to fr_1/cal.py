from flask import Flask, render_template, request

app = Flask(__name__)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

@app.route('/')
def index():
    return render_template('index_temperature.html')

@app.route('/convert', methods=['POST'])
def convert():
    temperature = float(request.form['temperature'])
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']

    if from_unit == 'fahrenheit' and to_unit == 'celsius':
        converted_temperature = fahrenheit_to_celsius(temperature)
    elif from_unit == 'celsius' and to_unit == 'fahrenheit':
        converted_temperature = celsius_to_fahrenheit(temperature)
    else:
        converted_temperature = temperature  # No conversion needed

    return render_template('index_temperature.html', temperature=temperature,
                           from_unit=from_unit, to_unit=to_unit,
                           converted_temperature=converted_temperature)

if __name__ == '__main__':
    app.run(debug=True)
