from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict


class ContractModel(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        frozen=True
    )
    
PayloadT = TypeVar("PayloadT", bound=ContractModel)

class CommandInfo(ContractModel):
    trace_id: str
    command_version: str = "V1"
    command_type: str
    command_name: str
    
class ControlMessage(ContractModel, Generic[PayloadT]):
    bot_id: str
    command: CommandInfo
    payload: PayloadT
    msg: str
    timestamp: int # in ms
    