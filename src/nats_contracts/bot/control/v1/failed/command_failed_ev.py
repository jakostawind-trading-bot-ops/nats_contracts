from typing import Literal

from nats_contracts.control.bot.v1.common.models import (
    ContractModel,
    ControlMessage,
    MsgInfo,
)

class CommandFailedPayload(ContractModel):
    command_name: str
    error: str

class CommandFailedInfo(MsgInfo):
    message_type: Literal["failed"] = "failed"
    message_name: Literal["CommandFailedEvent"] = "CommandFailedEvent"
    
class CommandFailedEvMsg(ControlMessage[CommandFailedPayload]):
    message: CommandFailedInfo
    payload: CommandFailedPayload
    description: str = "Bot command failed"