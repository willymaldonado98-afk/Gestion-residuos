from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista en memoria para almacenar los registros
puntos_reciclaje = []

@app.route("/")
def index():
    return render_template("index.html", puntos=puntos_reciclaje)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form.get("nombre")
    tipo = request.form.get("tipo")
    ubicacion = request.form.get("ubicacion")

    if nombre and tipo and ubicacion:
        puntos_reciclaje.append({
            "nombre": nombre,
            "tipo": tipo,
            "ubicacion": ubicacion
        })
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
