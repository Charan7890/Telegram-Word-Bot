async def send_message(bot,chat_id,message):
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        return True
    
    except Exception as error:
        print(error)
        return False