
class Config:
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
    ALGORITHM = "HS256"
    JWT_SECRET_KEY = "secret"
    JWT_REFRESH_SECRET_KEY = "refresh_secret"


config = Config()
