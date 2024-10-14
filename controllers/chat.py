from flask import jsonify
from flask_restful import Resource

from llm.llm import model
from controllers import api
from wraps import query_required
from settings import settings

class ChatApi(Resource):

    def get(self):
        return jsonify({"functions": settings.FUNCTIONS}), 200

class C2eApi(Resource):

    @query_required
    def post(self, query: str):
        print("==========c2e=========")
        txt = chat_by_type("c2e", query)
        return txt, 200
    
class E2cApi(Resource):

    @query_required
    def post(self, query: str):
        print("==========e2c=========")
        txt = chat_by_type("e2c", query)
        return txt, 200

class SummaryApi(Resource):

    @query_required
    def post(self, query: str):
        print("==========summary=========")
        txt = chat_by_type("summary", query)
        return txt, 200

def chat_by_type(type: str, query: str) -> str:
    if type not in settings.PROMPTS:
        type = "default"
    return model.chat(settings.PROMPTS[type].format(query))

api.add_resource(C2eApi, "/chat/c2e")
api.add_resource(E2cApi, "/chat/e2c")
api.add_resource(SummaryApi, "/chat/summary")
