import telepot #crea il bot usando telepot
import time #serve per time.sleep

TOKEN='1692902113:AAE1-EaEu5-MxvQ09JW1dSsW9YLpj-OGl1I'

bot = telepot.Bot(TOKEN)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # se MESSAGGIO é TESTO allora
    if content_type == 'text':
        message = msg['text']
        # se COMANDO é contenuto in MESSAGGIO allora
        if '/start' in message:
            bot.sendMessage(chat_id, 'Avvio del BabuBot')
        # elif ELSE IF, invece SE
        elif '/prossimagiocata' in message:
            bot.sendMessage(chat_id, 'Vota il sondaggione!')
        elif '/canalediscord' in message:
            bot.sendMessage(chat_id, 'https://discord.gg/nA7SHxMW')
        elif '/roll20' in message:
            bot.sendMessage(chat_id, 'app.roll20.net')
        elif '/riassuntone' in message:
            bot.sendMessage(chat_id, 'Nelle precedenti puntate i nostri eroi, dopo essersi risvegliati in un laboratorio sconosciuto, hanno scoperto di avere in corpo dei naniti che avrebbero causato la loro morte nell\'arco di 6 ore. Decisi a vendere cara la pelle, in quelle 6 ore gli avventurieri non solo hanno disattivato i naniti, ma hanno sterminato l\'intera popolazione del laboratorio. Cercando di localizzare tale laboratorio per capire come tornare a casa, gli eroi hanno scoperto di essere in realtà in un satellite in orbita sulla terra. A seguito di accurati calcoli, sono riusciti a rientrare sul loro pianeta natale per ammirare uno splendido tramonto alle Hawaii. Il mattino seguente gli eroi si risvegliano in tre alberghi differenti e i più fortunati riescono addirittura a fare colazione prima di dover iniziare a sparare per non lasciarci le penne. Sono braccati. Lo sanno loro, lo sa l\'agenzia Alpha e lo sa il malvagierrimo professor Pic! Cosa succederà ora? Scopritelo nelle prossime puntate!')
        elif '/squeeky' in message:
            bot.sendMessage(chat_id, 'Squiiik')
        # ELSE se non é niente di tutto quello scritto sopra. Se non é comando
        else:
            bot.sendMessage(chat_id, 'Non ho capito')

# Continua a far funzionare il bot
bot.message_loop(on_chat_message)

while 1:
    time.sleep(10)
