from typing import Literal

from nats_contracts.control.bot.v1.common.models import (
    ContractModel,
    ControlMessage,
    MsgInfo,
)

"""
{
  "bot_id": "bot-1",
  "message": {
    "message_id": "550e8400-e29b-41d4-a716-446655440000",
    "trace_id": "550e8400-e29b-41d4-a716-446655440001",
    "message_version": "V1",
    "message_type": "failed",
    "message_name": "bot_command_failed_ev"
  },
  "payload": {
    "command_name": "RunBotCommand",
    "error": "Bot is already running"
  },
  "description": "Bot command failed",
  "timestamp": 1789862400000
}
"""


class CommandFailedPayload(ContractModel):
    command_name: str
    error: str

class CommandFailedInfo(MsgInfo):
    message_type: Literal["failed"] = "failed"
    message_name: Literal["bot_command_failed_ev"] = "bot_command_failed_ev"
    
class CommandFailedEvMsg(ControlMessage[CommandFailedPayload]):
    message: CommandFailedInfo
    payload: CommandFailedPayload
    description: str = "Bot command failed"
