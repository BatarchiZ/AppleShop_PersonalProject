import botogram
from emailsender import general_handler

bot = botogram.create("")

@bot.command("start")
def start_command(chat, message):
    chat.send("Welcome to our shop! here you can buy (almost) every apple device you like."
              " Use /commands to see commands list.")

@bot.command("commands")
def commands_command(chat, message):
    chat.send("List of available commands\n"
              "/start - starting message \n"
              "/items - available devices \n"
              "\n"
              "The rest of the commands are replaced by buttons attached to messages")


@bot.command("items")
def btn_command(chat, message):
    btns = botogram.Buttons()
    btns[0].callback("iPhone", "iPhone")
    btns[1].callback("iPad", "iPad")
    btns[3].callback("MacBook", "MacBook")
    # btns[4].callback("Airpods", "Airpods") //Primerno takaye je cena v Kz i v Moskve, net smysla
    chat.send("Select the desired category:", attach=btns)


# MacBook section
###########################################################################################################
@bot.callback("MacBook")
def mbCommandHandler(chat, message):
    btns = botogram.Buttons()
    btns[0].callback("MacBook Air", "mbA")
    btns[1].callback("MacBook Pro", "mbP")
    chat.send("Select the MacBook Model:", attach=btns)

@bot.callback("mbP")
def mbpCommandHandler(chat, message):
    btns = botogram.Buttons()
    btns[0].callback("13-inch MacBook Pro", "13mbp")
    btns[1].callback("14-inch MacBook Pro", "14mbp")
    btns[2].callback("16-inch MacBook Pro", "16mbp")
    chat.send("Select the MacBook Pro size:", attach=btns)

@bot.callback("13mbp")
def mbp13mbaCommandHandler(chat, message):
    order = "MacBook Pro 13-inch"
    general_handler(chat, order)

@bot.callback("14mbp")
def mbp14CommandHandler(chat, message):
    order = "MacBook Pro 14-inch"
    general_handler(chat, order)

@bot.callback("16mbp")
def mbp16CommandHandler(chat, message):
    order = "MacBook Pro 16-inch"
    general_handler(chat, order)

@bot.callback("mbA")
def mbaCommandHandler(chat, message):
    btns = botogram.Buttons()
    btns[0].callback("M1 Chip", "m1mba")
    btns[1].callback("M2 Chip", "m2mba")
    chat.send("Select the chip for your macbook air:", attach=btns)

@bot.callback("m1mba")
def m1mbaCommandHandler(chat, message):
    order = "MacBook Air M1 Chip"
    general_handler(chat, order)

@bot.callback("m2mba")
def m2mbaCommandHandler(chat, message):
    order = "MacBook Air M2 Chip"
    general_handler(chat, order)


###########################################################################################################
# iPhone section
###########################################################################################################

@bot.callback("iPhone")
def ipCommandHandler(chat, message):
    btns = botogram.Buttons()
    btns[0].callback("iPhone 13 Pro Max", "ip13pm")
    btns[1].callback("iPhone 13 Pro", "ip13p")
    btns[2].callback("iPhone 13", "ip13")
    btns[3].callback("iPhone 13 mini", "ip13m")
    chat.send("Select the iPhone Model:", attach=btns)

@bot.callback("ip13pm")
def ip13pmHandler(chat, message):
    order = "iPhone 13 Pro Max"
    general_handler(chat, order)

@bot.callback("ip13p")
def ip13pHandler(chat, message):
    order = "iPhone 13 Pro"
    general_handler(chat, order)

@bot.callback("ip13")
def ip13Handler(chat, message):
    order = "iPhone 13"
    general_handler(chat, order)

@bot.callback("ip13m")
def ip13mHandler(chat, message):
    order = "iPhone 13 mini"
    general_handler(chat, order)

###########################################################################################################



# iPad section
###########################################################################################################
@bot.callback("iPad")
def iPadCommandHandler(chat, message):
    btns = botogram.Buttons()
    btns[0].callback("iPad Pro", "iPadProCommand")
    btns[1].callback("iPad Air", "iPadAirCommand")
    btns[2].callback("iPad", "iPadCommand2")
    chat.send("Select the iPad Model:", attach=btns)

@bot.callback("iPadAirCommand")
def iPadAirCommandHandler(chat, message):
    order = "iPadAir"
    general_handler(chat, order)

@bot.callback("iPadCommand2")
def iPadCommand2Handler(chat, message):
    order = "iPad"
    general_handler(chat, order)

# def username_callback(query, chat, message):
@bot.callback("iPadProCommand")
def iPadProCommanHandler(chat, message):
    order = "iPadPro"
    general_handler(chat, order)
    # chat.send("Please provide contact details")
    # chat.send("Your name:")
    # username = chat.username
    # botSendsEmail(order, username)
    # chat.send(f"Order placed {username}. Our employee will contact you shortly for further information about your {order} order.")
# @bot.command("123")
# def some_func(chat, message):
#     chat.send(str(chat.username))
#     # chat.send(chat.first_name)
# def general_handler(chat, order):
#     username = chat.username
#     botSendsEmail(order, username)
#     chat.send(f"Order placed {username}. Our employee will contact you shortly for further information about your {order} order.")

##############################################################################################################################################
if __name__ == "__main__":
    bot.run()