from typing import Literal

from nats_contracts.control.bot.v1.common.models import (
    ContractModel,
    ControlMessage,
    MsgInfo,
)

"""
control.to.bot.test_bot.command.V1.trading_state.remove_tracking_market_cmd

{
  "bot_id": "test_bot",
  "message": {
    "message_id": "550e8400-e29b-41d4-a716-446655440000",
    "trace_id": "550e8400-e29b-41d4-a716-446655440001",
    "message_version": "V1",
    "message_type": "trading_state",
    "message_name": "remove_tracking_market_cmd"
  },
  "payload": {
    "market_id": 4641064
  },
  "description": "Remove market from tracking markets",
  "timestamp": 1789862400000
}
"""


class RemoveTrackingMarketPayload(ContractModel):
    market_id: int
    
class RemoveTrackingMarketInfo(MsgInfo):
    message_type: Literal["trading_state"] = "trading_state"
    message_name: Literal["remove_tracking_market_cmd"] = "remove_tracking_market_cmd"
    
class RemoveTrackingMarketCmdMsg(ControlMessage[RemoveTrackingMarketPayload]):
    message: RemoveTrackingMarketInfo
    payload: RemoveTrackingMarketPayload
    description: str = "Remove market from tracking markets"