import asyncio
from aiogram import types
from ..Bot import walle


data = []


async def antiflood(msg: types.Message):
    counter = 0
    msgs_ids = []

    try:
        chat_id = msg.chat.id
        msg_id = msg.message_id
        sndr_id = msg.from_user.id
        chat_type = msg.chat.type

        if chat_type == 'supergroup':
            append_to_data = str(chat_id) + ':' + str(sndr_id) + ':' + str(msg_id)
            data.append(append_to_data)
        else:
            pass

        for num, obj in enumerate(data):
            msg_user_ids = str(sndr_id) + ':' + str(msg_id)

            if msg_user_ids in obj:
                msg_to_delete = data[num].split(':')[2]
                msgs_ids.append(msg_to_delete)
                counter += 1

        if counter > 7:
            msgs_ids.clear()
            data.clear()

            for i in range(0, len(msgs_ids)):
                await walle.delete_message(chat_id, msg.message_id)
                await walle.delete_message(chat_id, msgs_ids[i])
        elif counter < 7:
            pass

        if len(data) >  7:
            await msg.answer("Flood detected (пожалуйста не обращайте внимания на это смс)")

        print(data)
        print(counter)
    except Exception as e:
        print(e)