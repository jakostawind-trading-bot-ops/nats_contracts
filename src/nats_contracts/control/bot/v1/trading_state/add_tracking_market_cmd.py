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
    "message_type": "trading_state",
    "message_name": "add_tracking_market_cmd"
  },
  "payload": {
    "market_id": 123
  },
  "description": "Track market",
  "timestamp": 1789862400000
}
"""


class AddTrackingMarketPayload(ContractModel):
    market_id: int
    
class AddTrackingMarketInfo(MsgInfo):
    message_type: Literal["trading_state"] = "trading_state"
    message_name: Literal["add_tracking_market_cmd"] = "add_tracking_market_cmd"
    
class AddTrackingMarketCmdMsg(ControlMessage[AddTrackingMarketPayload]):
    message: AddTrackingMarketInfo
    payload: AddTrackingMarketPayload
    description: str = "Add market to tracking markets"
