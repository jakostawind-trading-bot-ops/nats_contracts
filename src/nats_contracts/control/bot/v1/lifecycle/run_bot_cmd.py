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


class RunBotCmd(ControlMessage[RunBotPayload]):
    message: RunBotCommandInfo
    payload: RunBotPayload
    description: str = ""
