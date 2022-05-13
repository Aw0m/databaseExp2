import jwt
import time

# 设置headers，即加密算法的配置
salt = "project2"


def create_token(user_id: int, username: str) -> str:
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }
    """
    exp（到期时间）声明
    nbf（不早于时间）声明
    iss（发行人）索赔
    aud（观众）声明
    iat（签发于）索赔
    """
    payload = {
        "userID": user_id,
        "userName": username,
        "exp": int(time.time() + 3600 * 24),
        "nbf": int(time.time()),
    }
    token = jwt.encode(payload=payload, key=salt, algorithm='HS256', headers=headers)
    return token


def verify_token(token: str) -> tuple[int, str]:
    try:
        info = jwt.decode(token, salt, algorithms='HS256')
        user_id, username = info["userID"], info["userName"]
        return user_id, username
    except:
        return -1, ""
