"""
Life
Copyright (C) 2020 MrRandom#9258

Life is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later version.

Life is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with Life. If not, see <https://www.gnu.org/licenses/>.
"""

import typing

import discord

from utilities import exceptions, objects


class GuildConfigManager:

    def __init__(self, bot) -> None:
        self.bot = bot

        self.default_guild_config = objects.DefaultGuildConfig()
        self.configs = {}

    async def load(self) -> None:

        guild_configs = await self.bot.db.fetch('SELECT * FROM guild_configs')
        for guild_config in guild_configs:
            self.configs[guild_config['id']] = objects.GuildConfig(data=dict(guild_config))

        print(f'[POSTGRESQL] Loaded guild configs. [{len(guild_configs)} guild(s)]')

    def get_guild_config(self, *, guild_id: int) -> typing.Union[objects.DefaultGuildConfig, objects.GuildConfig]:
        return self.configs.get(guild_id, self.default_guild_config)

    async def create_guild_config(self, *, guild_id: int) -> objects.GuildConfig:

        data = await self.bot.db.fetchrow('INSERT INTO guild_configs (id) values ($1) ON CONFLICT (id) DO UPDATE SET id = excluded.id RETURNING *', guild_id)
        self.configs[guild_id] = objects.GuildConfig(data=dict(data))

        return self.configs[guild_id]

    async def edit_guild_config(self, *, guild_id: int, attribute: str, operation: str = 'set', value: typing.Any = None) -> objects.GuildConfig:

        guild_config = self.get_guild_config(guild_id=guild_id)
        if isinstance(guild_config, objects.DefaultGuildConfig):
            guild_config = await self.create_guild_config(guild_id=guild_id)

        if attribute == 'colour':

            query = 'UPDATE guild_configs SET colour = $1 WHERE id = $2 RETURNING colour'

            if operation == 'set':
                data = await self.bot.db.fetchrow(query, value, guild_id)
            elif operation == 'reset':
                data = await self.bot.db.fetchrow(query, f'0x{str(discord.Colour.gold()).strip("#")}', guild_id)
            else:
                raise exceptions.LifeError('Invalid operation code.')

            guild_config.colour = discord.Colour(int(data['colour'], 16))

        elif attribute == 'prefix':

            if operation == 'add':
                data = await self.bot.db.fetchrow('UPDATE guild_configs SET prefixes = array_append(prefixes, $1) WHERE id = $2 RETURNING prefixes', value, guild_id)
            elif operation == 'remove':
                data = await self.bot.db.fetchrow('UPDATE guild_configs SET prefixes = array_remove(prefixes, $1) WHERE id = $2 RETURNING prefixes', value, guild_id)
            elif operation == 'reset':
                data = await self.bot.db.fetchrow('UPDATE guild_configs SET prefixes = $1 WHERE id = $2 RETURNING prefixes', [], guild_id)
            else:
                raise exceptions.LifeError('Invalid operation code.')

            guild_config.prefixes = data['prefixes']

        elif attribute == 'blacklist':

            if operation == 'set':
                query = 'UPDATE guild_configs SET blacklisted = $1, blacklisted_reason = $2 WHERE id = $3 RETURNING blacklisted, blacklisted_reason'
                data = await self.bot.db.fetchrow(query, True, value, guild_id)
            elif operation == 'reset':
                query = 'UPDATE guild_configs SET blacklisted = $1, blacklisted_reason = $2 WHERE id = $3 RETURNING blacklisted, blacklisted_reason'
                data = await self.bot.db.fetchrow(query, False, 'None', guild_id)
            else:
                raise exceptions.LifeError('Invalid operation code.')

            guild_config.blacklisted = data['blacklisted']
            guild_config.blacklisted_reason = data['blacklisted_reason']

        return guild_config
