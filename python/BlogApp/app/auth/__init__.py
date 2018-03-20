from flask import Blueprint
import os,sys

authblue = Blueprint('auth',__name__)

from . import  view