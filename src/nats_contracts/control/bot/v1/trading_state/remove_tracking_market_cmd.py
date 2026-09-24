from typing import Literal

from nats_contracts.control.bot.v1.common.models import (
    ContractModel,
    ControlMessage,
    MsgInfo,
)

class RemoveTrackingMarketPayload(ContractModel):
    market_id: int
    
class RemoveTrackingMarketInfo(MsgInfo):
    message_type: Literal["trading_state"] = "trading_state"
    message_name: Literal["remove_tracking_market_cmd"] = "remove_tracking_market_cmd"
    
class RemoveTrackingMarketCmdMsg(ControlMessage[RemoveTrackingMarketPayload]):
    message: RemoveTrackingMarketInfo
    payload: RemoveTrackingMarketPayload
    description: str = "Remove market from tracking markets"