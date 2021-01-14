import bcrypt

def hash_password(passwd):
  salt = bcrypt.gensalt()
  return bcrypt.hashpw(passwd.encode('utf-8'), salt)


def checkPasword(password, hashed):
  return bcrypt.checkpw(password, hashed)