import telebot

# الإعدادات الجاهزة الخاصة بك
API_TOKEN = '8592913588:AAH7Miy67w6k8tmJ5_0siFx7GBmM-SpPMLA'
ADMIN_ID = 5957783780

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك في بوت الرسائل السرية! أرسل رسالتك الآن وسأوصلها للمالك.")

@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    # معلومات المرسل
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    profile_link = f"tg://user?id={user_id}"
    
    # نص الرسالة التي ستصلك
    admin_msg = f"📩 **رسالة جديدة وصلت!**\n\n"
    admin_msg += f"👤 **المرسل:** [{user_name}]({profile_link})\n"
    admin_msg += f"🆔 **الآيدي:** `{user_id}`\n\n"
    admin_msg += f"📝 **الرسالة:**\n{message.text}"
    
    # إرسال الرسالة لك
    bot.send_message(ADMIN_ID, admin_msg, parse_mode="Markdown")
    
    # الرد على المرسل
    bot.reply_to(message, "✅ تم إرسال رسالتك بنجاح!")

if __name__ == '__main__':
    print("البوت يعمل الآن...")
    bot.infinity_polling()
