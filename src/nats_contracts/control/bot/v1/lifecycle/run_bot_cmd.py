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
    "message_type": "lifecycle",
    "message_name": "run_bot_cmd"
  },
  "payload": {},
  "description": "Run bot",
  "timestamp": 1789862400000
}
"""


class RunBotPayload(ContractModel):
    pass


class RunBotCommandInfo(MsgInfo):
    message_type: Literal["lifecycle"] = "lifecycle"
    message_name: Literal["run_bot_cmd"] = "run_bot_cmd"


class RunBotCmdMsg(ControlMessage[RunBotPayload]):
    message: RunBotCommandInfo
    payload: RunBotPayload
    description: str = "Run bot"
