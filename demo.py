from discord.ext import commands
from os import getenv
import os
# import traceback
from pixivpy3 import PixivAPI, AppPixivAPI
import random
import tweepy
import discord

bot = commands.Bot(command_prefix='/')


# @bot.event
# async def on_command_error(ctx, error):
#    orig_error = getattr(error, "original", error)
#    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#    await ctx.send(error_msg)


@bot.command()
async def syamumeigen(ctx):
    consumer_key = getenv("CONSUMER_KEY")
    consumer_secret = getenv("CONSUMER_SECRET")
    access_key = getenv("ACCESS_KEY")
    access_secret = getenv("ACCESS_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # キーワード
    count = 300

    tweet_list = []

    tweets = api.user_timeline(id="syamu_b0t", count=count)
    for tweet in tweets:
        tweet_list.append(tweet.text)

    await ctx.message.channel.send(random.choice(tweet_list))


@bot.command()
async def syamu(ctx):
    await ctx.message.channel.send(random.choice(("https://imgur.com/a/x5bd5I1", "https://imgur.com/a/2ZaJsOX", "https://imgur.com/a/PnO217z", "https://imgur.com/a/b5l7pKb", "https://imgur.com/a/UUSAdPl", "https://imgur.com/a/GRZmI5Y", "https://imgur.com/a/FfZZVRZ", "https://imgur.com/a/ldBMw3Y", "https://imgur.com/a/QlyQ81S", "https://imgur.com/a/g66WLuG", "https://imgur.com/a/hkaE1FH", "https://imgur.com/a/2nfFUh1", "https://imgur.com/a/SF6fuzt", "https://imgur.com/a/wB98Yfb", "https://imgur.com/a/UMQ0Yfd", "https://imgur.com/a/liyzvTD", "https://imgur.com/a/KFj7xRG", "https://imgur.com/a/AB922lk", "https://imgur.com/a/vgzsvmd", "https://imgur.com/a/qQAIwYT", "https://imgur.com/a/qX7OslR", "https://imgur.com/a/ozfwywf", "https://imgur.com/a/LBkuHrm")))


@bot.command()
async def pix(ctx, *args):
    tags = [' '.join(args)]

    # pixivpyのログイン処理
    api = PixivAPI()
    api.auth(refresh_token=getenv("reflesh_token"))
    aapi = AppPixivAPI()
    aapi.auth(refresh_token=getenv("reflesh_token"))

    # print(aapi.trending_tags_illust().trend_tags[0].tag)

    json_result = aapi.search_illust(tags, search_target='partial_match_for_tags')

    with open("pixiv.json", "w") as f:
        f.write(json_result.__str__())

    print(len(json_result.illusts))

    # print(random.randrange(len(json_result.illusts)))
    url = json_result.illusts[random.randrange(len(json_result.illusts))].image_urls.large
    fname = "img" + os.path.splitext(os.path.basename(url))[-1]
    aapi.download(url, name=fname, replace=True)

    file = "./img.jpg"
    await ctx.message.channel.send(file=discord.File(file))


@bot.command()
async def pixR(ctx, *args):
    tags = [' '.join(args) + 'R-18']

    # pixivpyのログイン処理
    api = PixivAPI()
    api.auth(refresh_token=getenv("reflesh_token"))
    aapi = AppPixivAPI()
    aapi.auth(refresh_token=getenv("reflesh_token"))

    # print(aapi.trending_tags_illust().trend_tags[0].tag)

    json_result = aapi.search_illust(tags, search_target='partial_match_for_tags')

    with open("pixiv.json", "w") as f:
        f.write(json_result.__str__())

    print(len(json_result.illusts))

    # print(random.randrange(len(json_result.illusts)))
    url = json_result.illusts[random.randrange(len(json_result.illusts))].image_urls.large
    fname = "img" + os.path.splitext(os.path.basename(url))[-1]
    aapi.download(url, name=fname, replace=True)

    file = "./img.jpg"
    await ctx.message.channel.send(file=discord.File(file))


@bot.command()
async def picture(ctx):
    file = "./img.jpg"
    await ctx.message.channel.send(file=discord.File(file))

@bot.command()
async def syamugazou(ctx):
    pixiv_token = getenv("PIXIV_TOKEN")
    api = PixivAPI()
    api.auth(refresh_token=pixiv_token)
    aapi = AppPixivAPI()
    aapi.auth(refresh_token=pixiv_token)

    json_result = aapi.search_illust("syamu", search_target='partial_match_for_tags')

    aapi.download(json_result.illusts[random.randrange(len(json_result.illusts))].image_urls.large, "./")

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
