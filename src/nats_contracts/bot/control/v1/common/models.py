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
    
    @classmethod
    def subject_suffix(cls) -> str:
        info_class = cls.model_fields["message"].annotation
        
        message_version = info_class.model_fields["message_version"].default
        message_type = info_class.model_fields["message_type"].default
        message_name = info_class.model_fields["message_name"].default

        if not isinstance(message_type, str) or not isinstance(message_name, str):
            raise ValueError(
                f"{cls.__name__}: message_type и message_name "
                "должны иметь строковые значения по умолчанию"
            )

        return f"{message_version}.{message_type}.{message_name}"
