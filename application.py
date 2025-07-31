from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Zo')
def home():
    return render_template('kitten.html')

if __name__ == '__main__':
    # Accès depuis un autre appareil en réseau local
    app.run(debug=True, host='0.0.0.0', port=5000)