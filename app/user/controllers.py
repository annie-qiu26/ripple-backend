from flask import Blueprint, request
from app.user.models import User

blueprint = Blueprint('user', __name__)

def user_from_cookie(req):
    userID = req.cookies.get("uid")
    user = User.queryById(userID)
    if user == None:
        user = User()
    return user
