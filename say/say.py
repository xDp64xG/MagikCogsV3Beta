import discord
from discord.ext import commands

class Say:
    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def say(self, ctx): 
        """Make your bot say something in the channel you use the command in."""

        msg = ctx.message.content
        message = ctx.message
        
        #This gets rid of the command "[p]say"
        msg = msg[5:]

        await message.delete()
        await ctx.send(msg)
