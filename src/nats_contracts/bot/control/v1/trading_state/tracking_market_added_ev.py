from typing import Literal
from typing import Any

from nats_contracts.bot.control.v1.common.models import (
    BotMessage,
    ContractModel,
    MsgInfo,
)

class TrackingMarketAddedEvPayload(ContractModel):
    market: dict[str, Any]
    
class TrackingMarketAddedEvInfo(MsgInfo):
    message_type: Literal["trading_state"] = "trading_state"
    message_name: Literal["TrackingMarketAddedEvent"] = "TrackingMarketAddedEvent"
    
class TrackingMarketAddedEvMsg(BotMessage):
    message: TrackingMarketAddedEvInfo
    payload: TrackingMarketAddedEvPayload
    description: str = "Add tracking market"