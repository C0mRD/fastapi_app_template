from pydantic import BaseModel

class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None

class SystemUser(BaseModel):
  id: int = None
  username: str = None
  email: str = None

class AuthenticateModel(BaseModel):
  access_token: str
  token_type: str = "bearer"

class Loginrequest(BaseModel):
  username: str
  password: str