from typing import Literal

from nats_contracts.control.bot.v1.common.models import (
    ContractModel,
    ControlMessage,
    MsgInfo,
)

class AddTrackingMarketPayload(ContractModel):
    market_id: int
    
class AddTrackingMarketInfo(MsgInfo):
    message_type: Literal["trading_state"] = "trading_state"
    message_name: Literal["AddTrackingMarket"] = "AddTrackingMarket"
    
class AddTrackingMarketCmdMsg(ControlMessage[AddTrackingMarketPayload]):
    message: AddTrackingMarketInfo
    payload: AddTrackingMarketPayload
    description: str = "Add market to track"