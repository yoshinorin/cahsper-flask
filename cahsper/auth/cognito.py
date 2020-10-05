import json
import jwt
import requests

from flask import Blueprint, Response, request
from jwt.algorithms import RSAAlgorithm
from cahsper import cahsper
from functools import wraps
from cahsper.utils.exceptions import UnauthorizedException

class Cognito:

    cognito_iss = cahsper.config['CAHSPER_AWS_COGNITO_ISS']
    cognito_app_client_id = cahsper.config['CAHSPER_AWS_COGNITO_APP_CLIENT_ID']
    cognito_jwk_url = cognito_iss + '/.well-known/jwks.json'
    jwk_set = requests.get(cognito_jwk_url).json()

    @classmethod
    def validate_jwt(cls, token):

        header = jwt.get_unverified_header(token)
        jwk = next(filter(lambda x: x['kid'] == header['kid'], cls.jwk_set['keys']))
        public_key = RSAAlgorithm.from_jwk(json.dumps(jwk))

        claims = jwt.decode(
            token,
            public_key,
            issuer=cls.cognito_iss,
            audience=cls.cognito_app_client_id,
            algorithms=jwk['alg'],
            options = dict(
                verify_aud=False
            )
        )

        if claims['client_id'] != cls.cognito_app_client_id:
            raise UnauthorizedException(description='Unauthorized error.')

        if claims['token_use'] != 'access':
            raise UnauthorizedException(description='Unauthorized error.')

        if claims['iss'] != cls.cognito_iss:
            raise UnauthorizedException(description='Unauthorized error.')

        print(claims)

def jwt_validator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get('Authorization') is None:
            raise UnauthorizedException(description='Unauthorized error.')

        token = request.headers['Authorization'].split()
        if len(token) != 2:
            raise UnauthorizedException(description='Unauthorized error.')

        Cognito.validate_jwt(token[1])
        return f(*args, **kwargs)
    return decorated_function

