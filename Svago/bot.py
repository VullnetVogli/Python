import discord
from discord.ext import commands
import io


'''
- Chi scrive i comandi dei bot in una chat != (deve essere scritto solo in spam comandi), lo portiamo subito al criminale o gli diamo un tot di avvertimenti
- Raggiunti gli avvertimenti gli diamo il tag criminale (lasciamo solo criminale) e lo spostiamo in prigione
- Quando chiede scusa nella chat 'richieste' ritorna come prima

'''

client = discord.Client()

messaggi = ('imploro perdono', 'chiedo venia', 'sono gay', 'siete i migliori', 'è il più bel server del mondo', 'mea culpa')

criminali = {}

# Metodo per assegnare un ruolo
async def aggiungi_ruolo(member : discord.Member, ruolo : discord.Role):
    
    role = discord.utils.get(member.guild.roles, name=ruolo)
                        
    await member.add_roles(role)
    
async def rimuovi_ruolo(member : discord.Member, ruolo : discord.Role):
    
    role = discord.utils.get(member.guild.roles, name=ruolo)
    
    await member.remove_roles(role)
    
async def cambia_canale(member, canale : discord.VoiceChannel):
    
    channel = discord.utils.get(member.guild.channels, name=canale)
    
    await member.move_to(channel)   

@client.event
async def on_message(message):
    
    if message.author != client.user:                     
                
        if not 'spam' in message.channel.name:
       
            if str(message.content).startswith('-') or str(message.content).startswith('!') or str(message.content).startswith('pls') or str(message.content).startswith('+') or str(message.content).startswith('>') or str(message.content).startswith('p!') or str(message.content).startswith('w.') or str(message.content).startswith('t!'):
            
                if not message.author in criminali:

                    criminali[message.author] = 1
                
                    await message.channel.send(':rage: Prova a riscriverlo non nella chat apposta e ti scopo il culo. Tentativi: %d/3. :rage:' % (criminali[message.author]))
                
                else:

                    if criminali[message.author] < 2:
                        
                        criminali[message.author] = criminali[message.author] + 1
                        
                        await message.channel.send(':rage: Prova a riscriverlo non nella chat apposta e ti scopo il culo. Tentativi: %d/3. :rage:' % (criminali[message.author]))
                        
                    else:
                        
                        if message.author.voice.channel.name != 'Prigione':
                        
                            criminali[message.author] = criminali[message.author] + 1
                        
                            await message.channel.send(':rage: Ma allora sei deficiente? Dillo: son deficiente, lo so! :rage:')
                                    
                            await aggiungi_ruolo(message.author, 'Criminale')
                                    
                            await cambia_canale(message.author, 'Prigione')
            
            if message.channel.name == 'prigione':
         
                if criminali[message.author] < 3:
                    
                    await message.channel.send('😘🥰 Bravo vedo che hai capito. 😘🥰')          
                    
                    criminali.pop(message.author)
                    
                else:
                        
                    if message.content in messaggi:
                        
                        await message.channel.send('😘🥰 Bravo vedo che hai capito. 😘🥰')          
                        
                        await cambia_canale(message.author, 'Che cazzo ci fai qui')
                        
                        await rimuovi_ruolo(message.author, 'Criminale')
                        
                        criminali.pop(message.author)
                        
                    else:
                        
                        await message.channel.send('🤪🤭 Chiedi perdono. 😘😝')         
    
#async def on_
                        
@client.event
async def on_ready():
    
    print('Logged in as', client.user.name)
    print('----------------------')


client.run('NjgyMTczMzM0NDM1MTM1NDg4.XrrPnA.0q_f01ZxT4Qr0i5bW7po8A91iNA')
