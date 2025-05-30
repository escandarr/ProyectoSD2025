from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        df = pd.read_csv('/data/salida_pig/part-r-00000', header=None, names=['comuna', 'total'])
        labels = df['comuna'].tolist()
        values = df['total'].tolist()
    except Exception as e:
        labels, values = [], []
        print(f"Error cargando datos: {e}")

    return render_template('index.html', labels=labels, values=values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
