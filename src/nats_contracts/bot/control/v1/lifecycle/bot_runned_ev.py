from typing import Literal

from nats_contracts.bot.control.v1.common.models import (
    BotMessage,
    ContractModel,
    MsgInfo,
)

class BotRunnedEvPayload(ContractModel):
    previous_status: str
    current_status: str
    
class BotRunnedEvInfo(MsgInfo):
    message_type: Literal["lifecycle"] = "lifecycle"
    message_name: Literal["bot_runned_ev"] = "bot_runned_ev"
    
class BotRunnedEvMsg(BotMessage[BotRunnedEvPayload]):
    message: BotRunnedEvInfo
    payload: BotRunnedEvPayload
    description: str = "Bot runned"