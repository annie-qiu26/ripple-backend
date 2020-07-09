from flask import Blueprint, request
from app.user.models import User

blueprint = Blueprint('user', __name__)

def user_from_cookie(req):
    userID = req.cookies.get("uid")
    print(userID)
    user = User.queryById(userID)
    if user == None:
        user = User()
    return user
