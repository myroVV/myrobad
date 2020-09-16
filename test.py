client.run(os.environ['DISCORD_TOKEN'])


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('myro > all'))