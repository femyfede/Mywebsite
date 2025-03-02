from mywebsite.wsgi import application

# This is needed to make Django work properly with Vercel
from werkzeug.middleware.proxy_fix import ProxyFix

application.wsgi_app = ProxyFix(application.wsgi_app)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    make_server('', 8000, application).serve_forever()
