from typing import Literal

from nats_contracts.control.bot.v1.common.models import (
    ContractModel,
    ControlMessage,
    MsgInfo,
)

class AddPolymarketStatePayload(ContractModel):
    nickname: str
    wallet: str
    
class AddPolymarketStateInfo(MsgInfo):
    message_type: Literal["state"] = "state"
    message_name: Literal["AddPolymarketStateCommand"]
    
class AddPolymarketStateMsg(ControlMessage[AddPolymarketStatePayload]):
    message: AddPolymarketStateInfo
    payload: AddPolymarketStatePayload
    description: str = "Add polymarker state"