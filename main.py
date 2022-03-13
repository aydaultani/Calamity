import json
import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    if os.path.exists(f"user_messages/{message.author.id}.json"):
        pass
    else:
        with open(f"user_messages/{message.author.id}.json", "w") as fp:
            json.dump({"messages": []}, fp, indent=4)

    if os.path.exists(f"user_info/{message.author.id}.json"):
        pass
    else:
        with open(f"user_info/{message.author.id}.json", "w") as fp:
            # json.dump({"messages" : []} , fp , indent=4)
            pass
    
    if os.path.exists(f"misc_info/all_messages.json"):
        pass
    else:
        with open("misc_info/all_messages.json" , "w") as fp:
            json.dump({"messages" : []} , fp , indent=4)

    with open(f"user_messages/{message.author.id}.json", "r+") as fe:
        data = json.load(fe)
        foo = data.get("messages")
        foo.append(message.content)
        fe.seek(0)
        fe.truncate()
        json.dump({"messages": foo}, fe, indent=4)

    with open(f"user_info/{message.author.id}.json", "r+") as f:
        new_data = {"avatar": "", "nick": "", "username": "", "creation_date": ""}

        new_data[
            "avatar"
        ] = f"https://cdn.discordapp.com/avatars/{message.author.id}/{message.author.avatar}.png?size=1024"
        new_data["nick"] = message.author.nick
        new_data["username"] = message.author.name
        new_data["creation_date"] = str(message.author.created_at)

        json.dump(new_data, f, indent=4)

    with open("misc_info/all_messages.json", "r+") as f:
        data = json.load(f)
        foo = data.get("messages")
        foo.append(message.content)
        f.seek(0)
        f.truncate()
        json.dump({"messages": foo}, f, indent=4)


client.run("token_here")