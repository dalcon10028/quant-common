import json
from unittest import mock

import pytest


@mock.patch('discord_webhook.DiscordWebhook.execute')
class TestDiscord:
    @pytest.mark.asyncio
    async def test_send(self, mock_execute):
        """send should send a message to discord with the embed."""

        # Arrange
        from discord import discord
        from discord_webhook import DiscordEmbed

        embed = DiscordEmbed()

        # Act
        await discord.send(embed)

        # Assert
        mock_execute.assert_called_once_with()

    @pytest.mark.asyncio
    async def test_send_error(self, mock_execute):
        """send_error should send a message to discord with the error message and data."""

        # Arrange
        from discord import discord
        from exception.quant_exception import QuantException

        exception = QuantException(name='name', code=500, message='message')
        data = {'key': 'value'}

        # Act
        await discord.send_error(exception, data)

        # Assert
        mock_execute.assert_called_once_with()

    @pytest.mark.asyncio
    async def test_send_warning(self, mock_execute):
        """send_warning should send a message to discord with the warning message and data."""

        # Arrange
        from discord import discord

        message = 'message'
        data = {'key': 'value'}

        # Act
        await discord.send_warning(message, data)

        # Assert
        mock_execute.assert_called_once_with()

    @pytest.mark.asyncio
    async def test_send_info(self, mock_execute):
        """send_info should send a message to discord with the info message and data."""

        # Arrange
        from discord import discord

        message = 'message'
        data = {'key': 'value'}

        # Act
        await discord.send_info(message, data)

        # Assert
        mock_execute.assert_called_once_with()

    @pytest.mark.asyncio
    async def test_send_success(self, mock_execute):
        """send_success should send a message to discord with the success message and data."""

        # Arrange
        from discord import discord

        message = 'message'
        data = {'key': 'value'}

        # Act
        await discord.send_success(message, data)

        # Assert
        mock_execute.assert_called_once_with()