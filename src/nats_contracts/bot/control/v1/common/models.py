from pydantic import BaseModel, ConfigDict


class ContractModel(BaseModel):
    model_config = ConfigDict(extra="ignore", frozen=True)


class MsgInfo(ContractModel):
    message_id: str
    trace_id: str
    message_version: str = "V1"
    message_type: str
    message_name: str


class BotMessage[PayloadT: ContractModel](ContractModel):
    bot_id: str
    bot_status: str
    message: MsgInfo
    payload: PayloadT
    description: str
    timestamp: int  # in ms
