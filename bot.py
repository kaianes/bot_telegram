import telebot

chave_api = "7450737140:AAFrpLAqloHQ8WCU4R86ipxQnu6fiZoDtQo"

bot = telebot.TeleBot(chave_api)

@bot.message_handler(commands=['poema'])
def poema(message):
    bot.reply_to(message, "Aqui vai um livro de indicação para você: 1984 de George Orwell. Uma leitura poderosa sobre liberdade, controle e a luta contra a opressão.")

@bot.message_handler(commands=['filme'])
def filme(message):
    bot.reply_to(message, "Aqui vai um filme de indicação para você: *Interestelar*. Prepare-se para uma viagem épica pelo espaço e pelo tempo!")

@bot.message_handler(commands=['livro'])
def livro(message):
    bot.reply_to(message, "Aqui vai um livro de indicação para você: 1984 de George Orwell. Uma leitura poderosa sobre liberdade, controle e a luta contra a opressão.")

@bot.message_handler(commands=['musica'])
def musica(message):
    bot.reply_to(message, "Aqui vai uma música de indicação para você: Bohemian Rhapsody da banda Queen. Uma obra-prima cheia de emoção e energia!")

def verificar(msg):
    return True

@bot.message_handler(func=verificar)
def responder(msg):
    texto = """
    Escolha uma opção para continuar:
    /poema - para receber um poema
    /filme - para receber uma indicação de filme
    /livro - para receber uma indicação de livro
    /musica - para receber uma indicação de música"""
    bot.reply_to(msg, texto)

bot.polling()