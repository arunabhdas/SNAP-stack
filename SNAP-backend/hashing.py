from passlib.context import CryptContext

pwdCtx = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hash():
    def bcrypt(password: str):
        hashedPassword = pwdCtx.hash(password)
        return hashedPassword
