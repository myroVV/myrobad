from discord.ext import commands
from aiohttp import ClientSession
import discord
import random
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown
from datetime import date, datetime, timedelta


class Rates(commands.Cog):
    """
    funsz
    """



    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Rates Cog has been loaded\n-----")


    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.guild)
    async def gay(self, ctx, member : discord.Member):
            random.randint(0, 100)

            embed = discord.Embed(title="**Gay Meter 69420 :rainbow_flag:**",
                                description=f"{member.mention} ``is {random.randint(0, 100)}% gay!``",
                                colour=discord.Color.blue(),
                                timestamp=datetime.utcnow())

            await ctx.send(embed=embed)

    @gay.error
    async def gay_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                userembed=discord.Embed(title="__**Gay Calculator 4200🏳️‍🌈**__", color=0xffffff)
                userembed.add_field(name="  **Please input a user!**", value="🏳️‍🌈 🏳️‍🌈 🏳️‍🌈 🏳️‍🌈", inline=False)
                await ctx.send(embed=userembed)

                
            if isinstance(error, commands.CommandOnCooldown):
                msg = '``This command is on cooldown, please try again in {:.2f}s``'.format(error.retry_after)
                await ctx.send(msg)
            else:
                raise error    

    



    @commands.command(pass_context=True, aliases=['peepee'])
    @commands.cooldown(1, 3, commands.BucketType.guild)
    async def pp(self, ctx, member: discord.Member):
        sizes = ['8D',
                    '8=D 1 inch LOL!📏',
                    '8==D 2 inches KEKW 📏',
                    '8==D 2 inches KEKW 📏',
                    '8==D 2 inches KEKW 📏',
                    '8==D 2 inches KEKW 📏',
                    '8===D 3 inches D: 📏',
                    '8===D 3 inches D: 📏',
                    '8=====D 5 inches :O 📏',
                    '8=====D 5 inches :O 📏',
                    '8===D 3 inches D: 📏',
                    '8===D 3 inches D: 📏',
                    '8===D 3 inches D: 📏',
                    '8====D 4 inches, ay bruh u good? 📏',
                    '8====D 4 inches, ay bruh u good? 📏',  
                    '8=====D 5 inches :O 📏',
                    '8=====D 5 inches :O 📏',
                    '8====D 4 inches, ay bruh u good? 📏',  
                    '8====D 4 inches, ay bruh u good? 📏',  
                    '8=====D 5 inches :O 📏',
                    '8=====D 5 inches :O 📏',
                    '8==D 2 inches KEKW 📏',
                    '8=====D 5 inches :O 📏',
                    '8======D 6 inches 🤷‍♂️', 
                    '8==D 2 inches KEKW 📏',
                    '8======D 6 inches 🤷‍♂️', 
                    '8======D 6 inches 🤷‍♂️', 
                    '8=====D 5 inches :O 📏',
                    '8======D 6 inches 🤷‍♂️', 
                    '8==D 2 inches KEKW 📏',
                    '8======D 6 inches 🤷‍♂️', 
                    '8======D 6 inches 🤷‍♂️', 
                    '8======D 6 inches 🤷‍♂️', 
                    '8=======D 7 inches 📏',
                    '8==D 2 inches KEKW 📏',
                    '8==D 2 inches KEKW 📏',
                    '8=======D 7 inches 📏',
                    '8=======D 7 inches 📏',
                    '8===D 3 inches D: 📏',
                    '8===D 3 inches D: 📏',
                    '8=======D 7 inches 📏',
                    '8=====D 5 inches :O 📏',
                    '8=======D 7 inches 📏',
                    '8========D 8 inches 📏',
                    '8========D 8 inches 📏',
                    '8=====D 5 inches :O 📏',
                    '8========D 8 inches 📏',
                    '8===D 3 inches D: 📏',
                    '8========D 8 inches 📏',
                    '8=========D 9 inches 📏',
                    '8===D 3 inches D: 📏',
                    '8===D 3 inches D: 📏',
                    '8==========D 10 inches 📏',
                    '8==D 2 inches KEKW 📏',
                    '8======D 6 inches 🤷‍♂️', 
                    '8===========D 11 inches 📏',
                    '8======D 6 inches 🤷‍♂️', 
                    '8============D 12 inches 📏',
                    '8==D 2 inches KEKW 📏',
                    '8=============D 13 inches 📏',
                    '8==D 2 inches KEKW 📏',
                    '8======D 6 inches 🤷‍♂️', 
                    '8==============D 14 inches 📏',
                    '8=====D 5 inches :O 📏',
                    '8===============D 15 inches 📏',
                    '8================D 16 inches 📏',
                    '8==D 2 inches KEKW 📏',
                    '8=====D 5 inches :O 📏',
                    '8=================D 17 inches 📏',
                    '8==================D 18 inches 📏',
                    '8==D 2 inches KEKW 📏',
                    '8==D 2 inches KEKW 📏',
                    '8===================D 19 inches 📏',
                    '8==============================D 30 inches 😵',
                    '8===D 3 inches D: 📏',
                    '8===D 3 inches D: 📏',
                    '8===D 3 inches D: 📏',
                    '8===============================D 31 inches 😵😵',
                    '8===D 3 inches D: 📏',
                    '8===D 3 inches D: 📏',
                    '8========================================D 40 inches!??!?!?!?! 😵😵']
        embed = discord.Embed(title="🍆 PP size Meter 🍆",
                              description=f"{member.mention}'s pp\n**{random.choice(sizes)}**",
                              colour=discord.Color.blue(),
                              timestamp=datetime.utcnow())
        # embed.add_field(name="\u200b", value=f"{random.choice(response)}")
        await ctx.send(embed=embed)



    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.guild)
    async def potacc(self, ctx, member : discord.Member):
            random.randint(0, 100)

            embed = discord.Embed(title="**Pot Accuracy Calculator 7200 🧪**",
                                description=f"{member.mention} has a pot accuracy of **{random.randint(0, 100)}%**",
                                colour=discord.Color.blue(),
                                timestamp=datetime.utcnow())

            await ctx.send(embed=embed)

    @potacc.error
    async def potacc_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                userembed=discord.Embed(title="__**Pot Accuracy Calculator 7200 🧪**__", color=0xffffff)
                userembed.add_field(name="  **Please input a user!**", value="---🧪---", inline=False)
                await ctx.send(embed=userembed)

                
            if isinstance(error, commands.CommandOnCooldown):
                msg = '``This command is on cooldown, please try again in {:.2f}s``'.format(error.retry_after)
                await ctx.send(msg)
            else:
                raise error    

    @pp.error
    async def pp_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                userembed=discord.Embed(title="__**PP Calculator 🍆**__", color=0xffffff)
                userembed.add_field(name="  **Please input a user!**", value="---🍆---", inline=False)
                await ctx.send(embed=userembed)

                
            if isinstance(error, commands.CommandOnCooldown):
                msg = '``This command is on cooldown, please try again in {:.2f}s``'.format(error.retry_after)
                await ctx.send(msg)
            else:
                raise error    



    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.guild)
    async def iq(self, ctx, member : discord.Member):
            random.randint(0, 100)

            embed = discord.Embed(title="**IQ Calcutor 3300 🧠**",
                                description=f"{member.mention} has an iq of **{random.randint(0, 200)}**",
                                colour=discord.Color.blue(),
                                timestamp=datetime.utcnow())

            await ctx.send(embed=embed)



    @iq.error
    async def iq_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                userembed=discord.Embed(title="__**IQ Calcutor 3300 🧠**__", color=0xffffff)
                userembed.add_field(name="  **Please input a user!**", value="---🧠---", inline=False)
                await ctx.send(embed=userembed)


            if isinstance(error, commands.CommandOnCooldown):
                msg = '``This command is on cooldown, please try again in {:.2f}s``'.format(error.retry_after)
                await ctx.send(msg)
            else:
                raise error    
                





    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.guild)
    async def ego(self, ctx, member : discord.Member):
            random.randint(0, 100)

            embed = discord.Embed(title="**Ego Calcutor 1200 📈**",
                                description=f"{member.mention} has an ego of **{random.randint(50, 400)}**",
                                colour=discord.Color.blue(),
                                timestamp=datetime.utcnow())

            await ctx.send(embed=embed)



    @ego.error
    async def ego_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                userembed=discord.Embed(title="__**Ego Calcutor 1200 📈**__", color=0xffffff)
                userembed.add_field(name="  **Please input a user!**", value="---📈---", inline=False)
                await ctx.send(embed=userembed)


            if isinstance(error, commands.CommandOnCooldown):
                msg = '``This command is on cooldown, please try again in {:.2f}s``'.format(error.retry_after)
                await ctx.send(msg)
            else:
                raise error    
                





def setup(client):
    client.add_cog(Rates(client))
