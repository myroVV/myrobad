import discord
from discord.ext import commands
import asyncio


class ModCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod Cog has been loaded\n-----")



    @commands.command(help="Ban a user.")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            return await ctx.send("You can't ban yourself")
        await member.ban(reason=reason)
        em = discord.Embed(title="The Ban Hammer Has Rised!")
        em.description = (f"{ctx.author.mention} Has Banned {member}")
        em.add_field(name=f"**Ban Hammer**", value=f'Banned By {ctx.author.mention}', inline=False)
        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/717867181827817984/719525512715960350/s.png')
        em.colour = (0xFF0000)
        await ctx.send(embed=em)

    @commands.command(help="Kick a user.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            return await ctx.send("You can't kick yourself")
        await member.kick(reason=reason)
        em = discord.Embed(title="The Kick Machine Has Awoken")
        em.description = (f"{ctx.author.mention} Has Kicked {member}")
        em.add_field(name=f"**Kick Machine**", value=f'Kicked By {ctx.author.mention}', inline=False)
        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/546331074876145666/719526555587575919/a.png')
        em.colour = (0xFF0000)
        await ctx.send(embed=em)

    @commands.command(help="Mute a user.")
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, user: discord.Member, *, reason=None):
        if user == ctx.author:
            return await ctx.send("You can't mute yourself")
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        mute = discord.utils.get(ctx.guild.text_channels, name="MUTED-TIME-OUT")
        if not role:
            try:
                global muted
                muted = await ctx.guild.create_role(name="Muted", reason="To use for muting")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(muted, send_messages=False,
                                                read_message_history=False,
                                                read_messages=False)
            except discord.Forbidden:
                return await ctx.send("I have no permissions to make a muted role!")
            await user.add_roles(muted)
            mute1 = discord.Embed(title = f"{user} has been sent to mute area | Reason = {reason}", color =ctx.author.color)
            await ctx.send(embed=mute1)
        else:
            await user.add_roles(role)
            mute = discord.Embed(title = f"{user} has been sent to mute area | Reason = {reason}", color =ctx.author.color)
            await ctx.send(embed=mute)
       
        if not mute:
            overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_message_history=False),
                        ctx.guild.me: discord.PermissionOverwrite(send_messages=True),
                        muted: discord.PermissionOverwrite(read_message_history=True)}
            try:
                channel = await ctx.create_channel('MUTED-TIME-OUT', overwrites=overwrites)
                await channel.send("Welcome to Hell Bruh You will spend your time here until you get unmuted")
            except discord.Forbidden:
                return await ctx.send("I have no permissions to make #MUTED-TIME-OUT")

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(':regional_indicator_x: Sorry you dont have permissions to do this!')

    @commands.command(help="Unmute a member")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, user: discord.Member, *, reason=None):
        if user == ctx.author:
            return await ctx.send("You can't unmute yourself")
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            return await ctx.send("How can I unmute a member if there's no Muted role ??")
        if not discord.utils.find(lambda role: role.name == "Muted", user.roles):
            return await ctx.send(f"**{user.name}** is already unmuted!")
        await user.remove_roles(role)
        mute1 = discord.Embed(title = f"{user} has been unmuted! | Reason = {reason}", color =ctx.author.color)
        return await ctx.send(embed=mute1)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(':regional_indicator_x: Sorry you dont have permissions to do this!')

    @commands.command(help="Delete specified messages.")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=100):
        if amount == 1:
            return await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} Please Purge More Than One Message')
        await ctx.channel.purge(limit=amount)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} You Do Not Have The Role Perm: `manage messages`!')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} You Do Not Have Perms To Ban People!')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} You Do Not Have Perms To Kick People!')

    @commands.command(help="Unban a user.")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user 

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                em = discord.Embed(title="Someone Has Used The Unban Hammer!", color=0xFF0000)
                em.description = (f"{ctx.author.mention} Has UnBanned {user.name}#{user.discriminator}")
                em.add_field(name=f"**UnBan Hammer**", value=f'UnBanned By {ctx.author.mention}', inline=False)
                em.set_thumbnail(url='https://cdn.discordapp.com/attachments/717867181827817984/719525512715960350/s.png')
                return await ctx.send(embed=em)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} You Dont Have Perms Or This Person Cannot Be Unbanned')

    @commands.command(help="Start a Poll.")
    @commands.has_permissions(ban_members=True)
    async def poll(self, ctx, *, desc):
        await ctx.send('@here NEW POLE VOTE TO TAKE PART!')
        embed = discord.Embed(
            colour = discord.Colour.red()
        )
        embed.set_author(name=f"New Poll Vote To Take Part", icon_url=ctx.author.avatar_url)
        embed.description = (f'{ctx.author.mention} Has Started A New Poll')
        embed.add_field(name="World | Poll - Question", value=f"`POLL:` **{desc}**", inline=False)
        embed.set_footer(text="👍 for Yes, ?? for 👎.")
        add_reactions_to = await ctx.send(embed=embed)
        await add_reactions_to.add_reaction("👍")
        await add_reactions_to.add_reaction("👎")

    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(':regional_indicator_x: Sorry you dont have permissions to do this!')  

    @commands.command(help="Start a Poll.")
    @commands.has_permissions(administrator=True)
    async def polln(self, ctx, *, desc):
        embed = discord.Embed(
            colour = discord.Colour.red()
        )
        embed.set_author(name=f"New Poll Vote To Take Part", icon_url=ctx.author.avatar_url)
        embed.description = (f'{ctx.author.mention} Has Started A New Poll')
        embed.add_field(name="World | Poll - Question", value=f"`POLL:` **{desc}**", inline=False)
        embed.set_footer(text="👍 for Yes, 👎 for No.")
        add_reactions_to = await ctx.send(embed=embed)
        await add_reactions_to.add_reaction("👍")
        await add_reactions_to.add_reaction("👎")

    @commands.command(help="Lockdown the current channel.")
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.message.channel.set_permissions(ctx.guild.default_role, read_messages = True, send_messages = False)
        embed = discord.Embed(title="World - Lockdown", color=ctx.author.color)
        embed.add_field(name="**INFO:**", value=f"?? Channel locked.")
        embed.add_field(name="**Requested By**", value=f"{ctx.author.mention}")
        await ctx.send(embed=embed)

 
    @commands.command(help="Unlock the current channel.")
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        # You don't need to define a variable if you're only going to use it once
        await ctx.message.channel.set_permissions(ctx.guild.default_role, read_messages = True, send_messages = True)
        embed = discord.Embed(title="World- Lockdown Over", color=ctx.author.color)
        embed.add_field(name="**INFO:**", value=f"?? Channel unlocked.")
        embed.add_field(name="**Requested By**", value=f"{ctx.author.mention}")
        await ctx.send(embed=embed)
   
    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} This Command Can Only Be Used By Admins') 
        
        
    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} This Command Can Only Be Used By Admins')

    @commands.command(help="Direct message a user.")
    @commands.cooldown(rate=1, per=20, type=commands.BucketType.member)
    @commands.has_permissions(administrator=True)
    async def dm(self, ctx, member : discord.Member, *, msg):
        embed = discord.Embed(description=f"World - Direct Message", timestamp=ctx.message.created_at)
        embed.add_field(name="Direct Message", value=f"{ctx.author.mention} Sent A Message To {member}\n Message: \n `{msg}`")
        embed.set_author(name="Succsesfully Sent Direct Message", icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png")
        embed.set_footer(text=f"World - Direct Message")
        embed.color = (ctx.author.color)
        await ctx.send(embed=embed)
        embed1 = discord.Embed(description=f"You Have Recived A Message", timestamp=ctx.message.created_at)
        embed1.add_field(name="Message:", value=f"`{msg}`\n --------------\n From - {ctx.author.mention}\n Guild = `{ctx.guild}`")
        embed1.set_author(name="World - Direct Message", icon_url=self.bot.user.avatar_url)
        embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png")
        embed1.set_footer(text=f"World - Direct Message")
        embed1.color = (ctx.author.color)
        await member.send(embed=embed1)

    @dm.error
    async def dm_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} You Do Not Have Perms To Direct Message Members!')
    
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds.")
        
        else:
         raise(error)


def setup(bot):
    bot.add_cog(ModCog(bot))
