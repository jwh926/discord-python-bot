import discord
from discord.ext import commands
import python_weather


bot = commands.Bot(command_prefix='!', description='testing')

@bot.event
async def on_ready():
    print('Logged in as', bot.user.name, end=", ")
    print(bot.user.id)

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms')

@bot.command()
async def weather(ctx, day="", *, city):
    client = python_weather.Client(format=python_weather.METRIC)
    w = await client.find(city)
    yesterday = w.forecasts[0]
    today = w.forecasts[1]
    tomorrow = w.forecasts[2]
    print(day, w)
    if day == "yesterday":
        await ctx.send(f'{yesterday.date.strftime("%Y-%m-%d")} {yesterday.sky_text} {yesterday.temperature}')
        await ctx.send(f'{w.location_name}')
        await ctx.send(f'{w.url}')
    elif day == "current":
        await ctx.send(f'{w.current.date.strftime("%H:%M")} {w.current.temperature}°C')
        await ctx.send(f'{w.location_name}')
        await ctx.send(f'{w.url}')
    elif day == "today":
        await ctx.send(f'{today.date.strftime("%Y-%m-%d")} {today.sky_text} {today.temperature}')
        await ctx.send(f'{w.location_name}')
        await ctx.send(f'{w.url}')
    elif day == "tomorrow":
        await ctx.send(f'{tomorrow.date.strftime("%Y-%m-%d")} {tomorrow.sky_text} {tomorrow.temperature}')
        await ctx.send(f'{w.location_name}')
        await ctx.send(f'{w.url}')
    else:
        for forecast in w.forecasts:
            # print(forecast)
            await ctx.send(f'{forecast.date.strftime("%Y-%m-%d")}: {forecast.sky_text} {forecast.temperature}°C')
        await ctx.send(f'{w.location_name}')
        await ctx.send(f'{w.url}')
    await client.close()


bot.run('ODU0NTE4Mjc0MjU1NDg3MDA2.G9qKEC.RadUk3VRwP52S0cL_yBc96rzhPsmQdfnTBa7qM')
