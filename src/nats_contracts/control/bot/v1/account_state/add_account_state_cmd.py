from typing import Literal

from nats_contracts.control.bot.v1.common.models import (
    ContractModel,
    ControlMessage,
    MsgInfo,
)

class AddAccountStatePayload(ContractModel):
    nickname: str
    wallet: str
    
class AddAccountStateInfo(MsgInfo):
    message_type: Literal["state"] = "state"
    message_name: Literal["AddAccountStateCommand"] = "AddAccountStateCommand"
    
class AddAccountStateCmdMsg(ControlMessage[AddAccountStatePayload]):
    message: AddAccountStateInfo
    payload: AddAccountStatePayload
    description: str = "Add account state"