from typing import Literal
from typing import Any

from nats_contracts.bot.control.v1.common.models import (
    BotMessage,
    ContractModel,
    MsgInfo,
)

class TrackingMarketRemovedEvPayload(ContractModel):
    market_id: int
    
class TrackingMarketRemovedEvInfo(MsgInfo):
    message_type: Literal["trading_state"] = "trading_state"
    message_name: Literal["tracking_market_removed_ev"] = "tracking_market_removed_ev"
    
class TrackingMarketRemovedEvMsg(BotMessage):
    message: TrackingMarketRemovedEvInfo
    payload: TrackingMarketRemovedEvPayload
    description: str = "Tracking market removed"