import web

urls = (
    '/', 'Index',
    '/webpy', 'Webpy',
    '/javascript', 'Javascript'
)
app = web.application(urls, globals())
render = web.template.render('templates/', base='layout')

class Index:
    def GET(self):
        return render.index()

class Webpy:
    def GET(self):
        return render.webpy(None)
    def POST(self):
        i = web.input()
        numero1  = int(i.number1)
        numero2 = int(i.number2)
        opcion_boton = i.boton
        resultado = 0
        if opcion_boton == 'sumar':
            resultado = numero1 + numero2
        elif opcion_boton == 'restar':
            resultado = numero1 - numero2
        elif opcion_boton == 'multiplicar':
            resultado = numero1 * numero2
        elif opcion_boton == 'dividir':
            resultado = numero1 / numero2
        return render.webpy(resultado)

class Javascript:
    def GET(self):
        return render.javascript()

if __name__ == "__main__":
    app.run()
