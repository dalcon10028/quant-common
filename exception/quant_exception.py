class QuantException(Exception):
    name: str
    code: int
    message: str

    def __init__(self, **ctx) -> None:
        self.__dict__.update(ctx)


class DiscordError(BaseException):
    name = "discord_error"
    code = 500
    message = "디스코드 웹훅 전송에 실패하였습니다."
