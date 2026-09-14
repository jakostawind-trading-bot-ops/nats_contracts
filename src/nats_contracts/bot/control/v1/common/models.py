from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict


class ContractModel(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        frozen=True
    )
    
PayloadT = TypeVar("PayloadT", bound=ContractModel)

class MsgInfo(ContractModel):
    message_id: str
    trace_id: str
    message_version: str = "V1"
    message_type: str
    message_name: str
    
class BotMessage(ContractModel, Generic[PayloadT]):
    bot_id: str
    bot_status: str
    event: MsgInfo
    payload: PayloadT
    msg: str
    timestamp: int # in ms
    