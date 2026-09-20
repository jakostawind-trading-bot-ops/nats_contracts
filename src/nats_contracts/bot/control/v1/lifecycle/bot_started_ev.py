from typing import Literal

from nats_contracts.bot.control.v1.common.models import (
    BotMessage,
    ContractModel,
    MsgInfo,
)

"""
{
  "bot_id": "bot-1",
  "bot_status": "running",
  "message": {
    "message_id": "550e8400-e29b-41d4-a716-446655440000",
    "trace_id": "550e8400-e29b-41d4-a716-446655440001",
    "message_version": "V1",
    "message_type": "lifecycle",
    "message_name": "bot_started_ev"
  },
  "payload": {},
  "description": "Bot started",
  "timestamp": 1789862400000
}
"""


class BotStartedPayload(ContractModel):
    pass


class BotStartedEventInfo(MsgInfo):
    message_type: Literal["lifecycle"] = "lifecycle"
    message_name: Literal["bot_started_ev"] = "bot_started_ev"


class BotStartedEvMsg(BotMessage[BotStartedPayload]):
    message: BotStartedEventInfo
    payload: BotStartedPayload
    description: str = "Bot started"
