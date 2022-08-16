from pydantic import BaseSettings


class Config(BaseSettings):
    """Project Configuration"""

    TELEGRAM_BOT_TOKEN: str = ''

    class Config:
        env_file = '.env'


config = Config()
