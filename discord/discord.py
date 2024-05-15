import os

from typing import Optional
from discord_webhook import DiscordEmbed, DiscordWebhook
from discord.message_color import MessageColor
from discord.utils import format_data
from exception import QuantException

webhook = DiscordWebhook(
    url=os.environ.get("DISCORD_WEBHOOK_URL")
)


async def send(embed: DiscordEmbed) -> None:
    try:
        webhook.embeds = [embed]
        response = webhook.execute()

    except Exception as e:
        print(e)
        pass


async def send_error(exception: QuantException, data: dict) -> None:
    await send(DiscordEmbed(
        author={
            "name": os.environ.get("DISCORD_WEBHOOK_TOPIC_NAME"),
            "url": os.environ.get("DISCORD_WEBHOOK_TOPIC_URL"),
        },
        title=f"[{exception.name}] {exception.message}",
        fields=format_data(data),
        color=MessageColor.DANGER.value
    ))


async def send_warning(message: str, data: Optional[dict]) -> None:
    await send(DiscordEmbed(
        title="Warning",
        description=message,
        color=MessageColor.WARNING.value,
        fields=format_data(data)
    ))


async def send_info(message: str, data: Optional[dict]) -> None:
    await send(DiscordEmbed(
        title="Warning",
        description=message,
        color=MessageColor.INFO.value,
        fields=format_data(data)
    ))


async def send_success(message: str, data: Optional[dict]) -> None:
    await send(DiscordEmbed(
        title="Warning",
        description=message,
        color=MessageColor.SUCCESS.value,
        fields=format_data(data)
    ))
