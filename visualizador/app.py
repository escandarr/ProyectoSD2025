from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def load_data(path, columns):
    try:
        df = pd.read_csv(path, header=None, names=columns)
        return df[columns[0]].tolist(), df[columns[1]].tolist()
    except Exception as e:
        print(f"Error cargando {path}: {e}")
        return [], []

@app.route('/')
def index():
    labels_comuna, values_comuna = load_data('/data/comuna/part-r-00000', ['comuna', 'total'])
    labels_tipo, values_tipo = load_data('/data/tipo/part-r-00000', ['tipo', 'total'])
    labels_fecha, values_fecha = load_data('/data/fecha/part-r-00000', ['fecha', 'total'])

    return render_template('index.html',
                           comuna_labels=labels_comuna, comuna_values=values_comuna,
                           tipo_labels=labels_tipo, tipo_values=values_tipo,
                           fecha_labels=labels_fecha, fecha_values=values_fecha)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
