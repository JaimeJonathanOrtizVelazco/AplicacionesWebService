import cherrypy

import operations


class MyWebService(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def sumar(self):
        data = cherrypy.request.json
        print(data)
        return operations.suma(data)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def restar(self):
        data = cherrypy.request.json
        return operations.resta(data)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def multiplicar(self):
        data = cherrypy.request.json
        return operations.multiplicacion(data)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def dividir(self):
        data = cherrypy.request.json
        return operations.division(data)


if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(MyWebService())
