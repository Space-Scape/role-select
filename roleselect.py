import discord
import asyncio
from discord.ext import commands
from discord.ui import Button, View
import os

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)  # Disable the default help command

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="Managing Roles"))

@bot.command()
async def role_panel(ctx):
    # Delete the user's command message
    await ctx.message.delete()

    embed = discord.Embed(
        title=":crossed_swords: Self Role Assign :crossed_swords:",
        description="Select the roles for the content that you wish to be notified for. "
                    "De-select to remove the role from your account.",
        color=discord.Color.red()
    )
    embed.set_footer(text="Select your roles")

    guild = ctx.guild
    custom_emoji_tob = discord.utils.get(guild.emojis, name="tob")
    custom_emoji_cox = discord.utils.get(guild.emojis, name="cox")
    custom_emoji_toa = discord.utils.get(guild.emojis, name="toa")
    custom_emoji_hmt = discord.utils.get(guild.emojis, name="hmt")
    custom_emoji_cm = discord.utils.get(guild.emojis, name="cm")
    custom_emoji_extoa = discord.utils.get(guild.emojis, name="extoa")
    custom_emoji_graardor = discord.utils.get(guild.emojis, name="graardor")
    custom_emoji_sara = discord.utils.get(guild.emojis, name="sara")
    custom_emoji_zammy = discord.utils.get(guild.emojis, name="zammy")
    custom_emoji_arma = discord.utils.get(guild.emojis, name="arma")
    custom_emoji_nex = discord.utils.get(guild.emojis, name="nex")
    custom_emoji_corp = discord.utils.get(guild.emojis, name="corp")
    custom_emoji_callisto = discord.utils.get(guild.emojis, name="callisto")
    custom_emoji_vetion = discord.utils.get(guild.emojis, name="vetion")
    custom_emoji_venenatis = discord.utils.get(guild.emojis, name="venenatis")
    custom_emoji_huey = discord.utils.get(guild.emojis, name="hueycoatl")

    button_tob = Button(label="TOB", style=discord.ButtonStyle.secondary, emoji=custom_emoji_tob)
    button_cox = Button(label="COX", style=discord.ButtonStyle.secondary, emoji=custom_emoji_cox)
    button_toa = Button(label="TOA", style=discord.ButtonStyle.secondary, emoji=custom_emoji_toa)
    button_hmt = Button(label="HMT", style=discord.ButtonStyle.secondary, emoji=custom_emoji_hmt)
    button_cm = Button(label="COX CMs", style=discord.ButtonStyle.secondary, emoji=custom_emoji_cm)
    button_extoa = Button(label="TOA EXP", style=discord.ButtonStyle.secondary, emoji=custom_emoji_extoa)
    button_graardor = Button(label="Graardor", style=discord.ButtonStyle.secondary, emoji=custom_emoji_graardor)
    button_sara = Button(label="Zilyana", style=discord.ButtonStyle.secondary, emoji=custom_emoji_sara)
    button_zammy = Button(label="Tsutsaroth", style=discord.ButtonStyle.secondary, emoji=custom_emoji_zammy)
    button_arma = Button(label="Kree'arra", style=discord.ButtonStyle.secondary, emoji=custom_emoji_arma)
    button_nex = Button(label="Nex", style=discord.ButtonStyle.secondary, emoji=custom_emoji_nex)
    button_corp = Button(label="Corporeal Beast - Corp", style=discord.ButtonStyle.secondary, emoji=custom_emoji_corp)
    button_callisto = Button(label="Callisto", style=discord.ButtonStyle.secondary, emoji=custom_emoji_callisto)
    button_vetion = Button(label="Vet'ion", style=discord.ButtonStyle.secondary, emoji=custom_emoji_vetion)
    button_venenatis = Button(label="Venenatis", style=discord.ButtonStyle.secondary, emoji=custom_emoji_venenatis)
    button_huey = Button(label="Hueycoatl", style=discord.ButtonStyle.secondary, emoji=custom_emoji_huey)

    view = View(timeout=None)
    view.add_item(button_tob)
    view.add_item(button_cox)
    view.add_item(button_toa)
    view.add_item(button_hmt)
    view.add_item(button_cm)
    view.add_item(button_extoa)
    view.add_item(button_graardor)
    view.add_item(button_sara)
    view.add_item(button_zammy)
    view.add_item(button_arma)
    view.add_item(button_nex)
    view.add_item(button_corp)
    view.add_item(button_callisto)
    view.add_item(button_vetion)
    view.add_item(button_venenatis)
    view.add_item(button_huey)

    async def button_callback(interaction):
        role_name = interaction.data['custom_id']
        role = discord.utils.get(interaction.guild.roles, name=role_name)

        if role is None:
            await interaction.response.send_message(f"Error: Role {role_name} not found.", ephemeral=True)
            return

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            feedback_message = await interaction.channel.send(f"{interaction.user.mention}, Role {role_name} removed.")
        else:
            await interaction.user.add_roles(role)
            feedback_message = await interaction.channel.send(f"{interaction.user.mention}, Role {role_name} added.")

        # Acknowledge the interaction and delete the message after 1 second
        await interaction.response.defer()
        await feedback_message.delete(delay=1)

    buttons = [button_tob, button_cox, button_toa, button_hmt, button_cm, button_extoa, button_graardor, button_sara, button_zammy, button_arma, button_nex, button_corp, button_callisto, button_vetion, button_venenatis, button_ffa]
    role_names = ["Theatre of Blood - TOB", "Chambers of Xeric - COX", "Tombs of Amascut - TOA", "Theatre of Blood Hard Mode - HMT", "Chambers of Xeric Challenge Mode - COX CMs", "Tombs of Amascut Expert - TOA EXP", "General Graardor - Bandos GWD", "Commander Zilyana - Saradomin GWD", "K'ril Tsutsaroth - Zamorak GWD", "Kree'arra - Armadyl GWD", "Nex", "Corporeal Beast - Corp", "Callisto", "Vet'ion", "Venenatis", "Hueycoatl"]

    for button, role_name in zip(buttons, role_names):
        button.custom_id = role_name
        button.callback = button_callback

    await ctx.send(embed=embed, view=view)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
