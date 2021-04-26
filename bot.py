# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

count = 0

#Example of bot command
@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

def upCount(ctx):
    #update database and send messages
    ctx.send(f'KKKKKK MAIS UM')
    ctx.send(f'Agora o bobão quitou {count} vezes')
    

def downCount():
    #update database and send messages
    ctx.send(f'Opa, falha no engano')
    ctx.send(f'O bobo quitou apenas {count} vezes')


@bot.command(name='rage', help='Responds with number of times that specific user rage quit')
async def ragequit(ctx, quitter='', option=''):
    if (quitter == '' or option == ''):
        await ctx.send('Você precisa especificar o usuario e o comando (count | up | down)')
        await ctx.send('Exemplo: `!rage @usuario up`')
        return
    
    id_quitter = int(quitter[3:-1])
    
    if (option == 'count'):
        await ctx.send(f'O bobao já quitou {count} vezes')
    elif(option == 'up' and ctx.author.id != id_quitter):
        upCount(ctx)    
    elif(option == 'down' and ctx.author.id != id_quitter):
        downCount(ctx)
    else:
        await ctx.send("Você não pode mudar seus proprios rage quit's bobao")

bot.run(TOKEN)