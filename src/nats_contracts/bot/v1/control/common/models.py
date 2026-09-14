from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict


class ContractModel(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        frozen=True
    )
    
PayloadT = TypeVar("PayloadT", bound=ContractModel)

class EventInfo(ContractModel):
    trace_id: str
    event_version: str = "V1"
    event_type: str
    event_name: str
    
class BotMessage(ContractModel, Generic[PayloadT]):
    bot_id: str
    bot_status: str
    event: EventInfo
    payload: PayloadT
    msg: str
    timestamp: int # in ms
    