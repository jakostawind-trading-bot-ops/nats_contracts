from typing import Literal
from typing import Any

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
    "message_type": "trading_state",
    "message_name": "tracking_market_added_ev"
  },
  "payload": {
    "market_info": {
      "market_id": 123
    }
  },
  "description": "Added tracking market",
  "timestamp": 1789862400000
}
"""


class TrackingMarketAddedEvPayload(ContractModel):
    market_info: dict[str, Any]
    
class TrackingMarketAddedEvInfo(MsgInfo):
    message_type: Literal["trading_state"] = "trading_state"
    message_name: Literal["tracking_market_added_ev"] = "tracking_market_added_ev"
    
class TrackingMarketAddedEvMsg(BotMessage):
    message: TrackingMarketAddedEvInfo
    payload: TrackingMarketAddedEvPayload
    description: str = "Added tracking market"
