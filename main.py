# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # import time
    # import datetime
    import os
    # Imports time libraries needed for timer functions

    import discord
    from dotenv import load_dotenv
    from discord.ext import commands
    # Imports the discord functions and commands

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    # Generates the token used for activating connection to bot at the end of code
    bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():

        print(f'{client.user} has connected to Discord!')
    # On the event that the bot is ready, prints that bot is ready to terminal

    @bot.command(name='members', help='Responds with all members and their current roles')
    @commands.has_role('admin')
    # Sets name, description and permission for the command
    async def members(ctx):
        response = ""
        for guild in bot.guilds:
            for member in guild.members:
                response = response + str(member) + " " + str(member.roles) + ", "
            # Iterates through every member, putting their names and roles into the string
        await ctx.send(response)
        # Prints constructed string when it's finished creating

    @bot.command(name='addrole', help='Adds a role to a member in the server')
    @commands.has_permissions(manage_roles=True)
    # Sets name, description and permissions for the command
    async def addrole(ctx, member: discord.Member = None, *, role: discord.Role = None):
        if role is None:
            await ctx.send(f'Provide a role to add')
            return
        # makes sure that a role is specified
        if member is None:
            await ctx.send(f'Provide a member to add a role')
            return
        # makes sure that a member is specified
        await member.add_roles(role)
        await ctx.send(f"Successfully added role, {role} to {member.name}")
        # adds the role to the member and prints it
    bot.run(TOKEN)

    # Runs above code in discord bot


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
