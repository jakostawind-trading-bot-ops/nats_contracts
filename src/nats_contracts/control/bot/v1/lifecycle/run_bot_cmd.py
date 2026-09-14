from typing import Literal

from nats_contracts.control.bot.v1.common.models import MsgInfo, ControlMessage, ContractModel

class RunBotPayload(ContractModel):
    pass

class RunBotCommandInfo(MsgInfo):
    command_type: Literal["lifecycle"] = "lifecycle"
    command_name: Literal["RunBotCommand"] = "RunBotCommand"
    
class RunBotCmd(ControlMessage):
    command: RunBotCommandInfo
    payload: RunBotPayload
    msg: str = ""