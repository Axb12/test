from flask import jsonify
from flask_restful import Resource

from controllers import api
from settings import settings

class FunctionsApi(Resource):

    def get(self):
        return {"functions": settings.FUNCTIONS}, 200

api.add_resource(FunctionsApi, "/functions")

