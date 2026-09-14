from typing import Final, Literal

from nats_contracts.bot.v1.control.common.models import EventInfo, BotMessage, ContractModel

class BotStartedPayload(ContractModel):
    pass

class BotStartedEventInfo(EventInfo):
    event_type: Literal["lifecycle"] = "lifecycle"
    event_name: Literal["BotStartedEvent"] = "BotStartedEvent"
    
class BotStartedMsg(BotMessage):
    event: BotStartedEventInfo
    payload: BotStartedPayload
    msg: str = "Bot started"