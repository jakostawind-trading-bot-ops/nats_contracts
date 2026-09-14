from typing import Literal

from nats_contracts.bot.control.v1.common.models import (
    BotMessage,
    ContractModel,
    MsgInfo,
)


class BotStartedPayload(ContractModel):
    pass


class BotStartedEventInfo(MsgInfo):
    message_type: Literal["lifecycle"] = "lifecycle"
    message_name: Literal["BotStartedEvent"] = "BotStartedEvent"


class BotStartedEvMsg(BotMessage[BotStartedPayload]):
    message: BotStartedEventInfo
    payload: BotStartedPayload
    description: str = "Bot started"
