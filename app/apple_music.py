import jwt, time
from requests import get

def get_token(apple_secret_key, apple_key_id, apple_team_id):
    headers = {
        "alg": "ES256",
        "kid": apple_key_id
    }

    payload = {
        "iss": apple_team_id,
        "iat": int(time.time()),
        "exp": int(time.time()) + 120,
    }

    token = jwt.encode(payload, apple_secret_key, algorithm="ES256", headers=headers)
    return {"token": token, "expiry": payload["exp"]}