from typing import Literal

from nats_contracts.bot.control.v1.common.models import EventInfo, BotMessage, ContractModel

class BotStartedPayload(ContractModel):
    pass

class BotStartedEventInfo(EventInfo):
    event_type: Literal["lifecycle"] = "lifecycle"
    event_name: Literal["BotStartedEventTest"] = "BotStartedEventTest"
    
class BotStartedMsg(BotMessage):
    event: BotStartedEventInfo
    payload: BotStartedPayload
    msg: str = "Bot started"