from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/calculocompra", methods=['GET', 'POST'])
def calculocompra():
    if request.method == "POST":
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        valortarro = 9000

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_sin_descuento = valortarro * cantidad
        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template('calculocompra.html', nombre=nombre, edad=edad,
                               total_sin_descuento=total_sin_descuento, cantidad=cantidad, descuento=descuento,
                               total_con_descuento=total_con_descuento)

    return render_template('calculocompra.html')

@app.route('/iniciosesion', methods=['GET', 'POST'])
def iniciosesion():
    mensaje_bienvenida = None
    intento_incorrecto = False

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario == 'juan' and contrasena == 'admin':
            mensaje_bienvenida = f"Bienvenido administrador {usuario}"
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje_bienvenida = f"Bienvenido usuario {usuario}"
        else:
            intento_incorrecto = True

    return render_template('iniciosesion.html', mensaje_bienvenida=mensaje_bienvenida,
                           intento_incorrecto=intento_incorrecto)


if __name__ == '__main__':
    app.run(debug=True)


