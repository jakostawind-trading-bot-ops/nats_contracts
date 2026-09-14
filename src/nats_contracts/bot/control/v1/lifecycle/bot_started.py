from typing import Literal

from nats_contracts.bot.control.v1.common.models import MsgInfo, BotMessage, ContractModel

class BotStartedPayload(ContractModel):
    pass

class BotStartedEventInfo(MsgInfo):
    event_type: Literal["lifecycle"] = "lifecycle"
    event_name: Literal["BotStartedEvent"] = "BotStartedEvent"
    
class BotStartedEvent(BotMessage):
    event: BotStartedEventInfo
    payload: BotStartedPayload
    msg: str = "Bot started"