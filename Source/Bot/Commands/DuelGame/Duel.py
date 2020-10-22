import random
from aiogram import types
from ...Bot import walle
from ...Strings.RU.Errors.PointTargetError import point_target
from ...Strings.RU.Commands.DuelGame import MainText, Win, DrawGame, GameKeyboard, DuelShizoid, DuelDenied, DuelNotForYou
from ....Utils.ReturnNoneReservesFunc import returnNoneReserved


async def duel_command(msg: types.Message):
    try:
        sndr = msg.from_user
        target = msg.reply_to_message

        if target is None:
            await msg.reply(
                point_target,
                parse_mode = 'MarkdownV2'
            )
        else:
            await msg.reply(
                MainText.main_duel_text.format(
                    returnNoneReserved(target.from_user.first_name),
                    target.url,
                    returnNoneReserved(sndr.first_name),
                    sndr.url
                ),
                parse_mode = 'MarkdownV2',
                reply_markup = GameKeyboard.game_keyboard
            )
    except DeprecationWarning:
        pass
    except Exception as e:
        print(e)


async def duel_callb_listener(call: types.CallbackQuery):
    sndr = call.message.reply_to_message.from_user
    target = call.message.reply_to_message.reply_to_message

    modes = ['win', 'draw']
    members = [target.from_user, sndr]

    if call.from_user == sndr:
        await call.message.answer(
            DuelShizoid.shizoid_duel.format(
                sndr.url
                ),
                parse_mode = 'MarkdownV2'
            )
    elif call.from_user != target.from_user:
        await call.message.answer(
            DuelNotForYou.not_for_you.format(
                returnNoneReserved(call.from_user.first_name),
                call.from_user.url
            ),
            parse_mode = 'MarkdownV2'
        )
    else:
        if call.data == 'yes':
            mode = random.choice(modes)

            if mode == 'win':
                winner = random.choice(members)

                await call.message.answer(
                    Win.win_text.format(
                        returnNoneReserved(winner.first_name),
                        winner.url,
                        returnNoneReserved(call.from_user.first_name),
                        call.from_user.url,
                        returnNoneReserved(winner.first_name),
                        winner.url
                    ),
                    parse_mode = 'MarkdownV2'
                )
            elif mode == 'draw':
                winner = random.choice(members)

                await call.message.answer(
                    DrawGame.draw_game_text.format(
                        returnNoneReserved(winner.first_name),
                        winner.url,
                        returnNoneReserved(call.from_user.first_name),
                        call.from_user.url,
                        returnNoneReserved(call.from_user.first_name),
                        call.from_user.url
                    ),
                    parse_mode = 'MarkdownV2'
                )

        elif call.data == 'no':
            await call.message.reply(
                DuelDenied.denied_duel,
                parse_mode = 'MarkdownV2'
            )