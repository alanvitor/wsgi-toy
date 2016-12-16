from app import application as original_app
from middleware import MyHeaderMiddleware

application = MyHeaderMiddleware(original_app)