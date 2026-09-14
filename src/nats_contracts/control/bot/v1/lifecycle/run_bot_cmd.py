from typing import Literal

from nats_contracts.control.bot.v1.common.models import (
    ContractModel,
    ControlMessage,
    MsgInfo,
)


class RunBotPayload(ContractModel):
    pass


class RunBotCommandInfo(MsgInfo):
    message_type: Literal["lifecycle"] = "lifecycle"
    message_name: Literal["RunBotCommand"] = "RunBotCommand"


<<<<<<< HEAD
class RunBotCmd(ControlMessage[RunBotPayload]):
=======
class RunBotCmdMsg(ControlMessage[RunBotPayload]):
>>>>>>> 071e553 (0.3.2 исправлены ключи у дочрних классов)
    message: RunBotCommandInfo
    payload: RunBotPayload
    description: str = ""
