import asyncpg
import discord
from discord.ext import commands


class Database(commands.Cog):

    def __init__(self, bot):
        """Initialized the Database cog"""

        self.bot = bot
        self.db = self.bot.db

    async def add_tag(self, tag, author):
        """Adds a tag to the database"""

        async with self.db.acquire() as conn:
            await conn.execute(
                "INSERT INTO tags (tag, author) VALUES ($1, $2)",
                tag, author
            )

    async def get_tag(self, tag):
        """Gets a tag from the database"""

        tag = await self.db.fetchrow(
            "SELECT * FROM tags WHERE tag = $1",
            tag
        )
        return tag

    async def remove_tag(self, tag):
        """Removes a tag from the database"""

        async with self.db.acquire() as conn:
            await conn.execute(
                "DELETE FROM tags WHERE tag = $1",
                tag
            )


def setup(bot):
    bot.add_cog(Database(bot))