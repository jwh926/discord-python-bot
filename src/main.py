import discord
import interactions
import python_weather

file = open(r"src/token", "r")
token = file.read()
file.close()

bot = interactions.Client(token=token)

@bot.command(
    name="ping",
    description="ping",
    scope=854519080882143262
)
async def ping(ctx: interactions.CommandContext):
    await ctx.send(f'pong! {round(round(bot.latency, 4))}ms')

@bot.command(
    name="weather",
    description="weather",
    scope=854519080882143262,
    options=[
        interactions.Option(
            name="day",
            description="yesterday, today, tomorrow",
            type=interactions.OptionType.STRING,
            required=True
        ),
        interactions.Option(
            name="city",
            description="Where do you live?",
            type=interactions.OptionType.STRING,
            required=True
        )
    ]
)
async def weather(ctx, day: str, *, city: str):
    client = python_weather.Client(format=python_weather.METRIC)
    w = await client.find(city)
    yesterday = w.forecasts[0]
    today = w.forecasts[1]
    tomorrow = w.forecasts[2]
    print(day, w)
    if day == "yesterday":
        await ctx.send(f'{yesterday.date.strftime("%Y-%m-%d")} {yesterday.sky_text} {yesterday.temperature}°C\n{w.location_name}\n{w.url}')
    elif day == "current":
        await ctx.send(f'{w.current.date.strftime("%H:%M")} {w.current.temperature}°C\n{w.location_name}\n{w.url}')
    elif day == "today":
        await ctx.send(f'{today.date.strftime("%Y-%m-%d")} {today.sky_text} {today.temperature}°C\n{w.location_name}\n{w.url}')
    elif day == "tomorrow":
        await ctx.send(f'{tomorrow.date.strftime("%Y-%m-%d")} {tomorrow.sky_text} {tomorrow.temperature}°C\n{w.location_name}\n{w.url}')
    else:
        for forecast in w.forecasts:
            # print(forecast)
            await ctx.send(f'{forecast.date.strftime("%Y-%m-%d")}: {forecast.sky_text} {forecast.temperature}°C\n{w.location_name}\n{w.url}')
    await client.close()

bot.start()