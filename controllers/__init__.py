from flask import Blueprint
from flask_restful import Api

bp = Blueprint("bp", __name__)
api = Api(bp)

from controllers.chat import *
from controllers.functions import *
