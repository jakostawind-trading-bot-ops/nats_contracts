from typing import Literal

from nats_contracts.control.bot.v1.common.models import CommandInfo, ControlMessage, ContractModel

class RunBotPayload(ContractModel):
    pass

class RunBotCommandInfo(CommandInfo):
    command_type: Literal["lifecycle"] = "lifecycle"
    command_name: Literal["RunBotCommand"] = "RunBotCommand"
    
class RunBotMsg(ControlMessage):
    command: RunBotCommandInfo
    payload: RunBotPayload
    msg: str = ""