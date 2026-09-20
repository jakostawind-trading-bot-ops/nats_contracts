from typing import Literal

from nats_contracts.control.bot.v1.common.models import (
    ContractModel,
    ControlMessage,
    MsgInfo,
)

"""
{
  "bot_id": "bot-1",
  "message": {
    "message_id": "550e8400-e29b-41d4-a716-446655440000",
    "trace_id": "550e8400-e29b-41d4-a716-446655440001",
    "message_version": "V1",
    "message_type": "state",
    "message_name": "add_account_state_cmd"
  },
  "payload": {
    "nickname": "test-account",
    "wallet": "0x0000000000000000000000000000000000000000"
  },
  "description": "Add account state",
  "timestamp": 1789862400000
}
"""


class AddAccountStatePayload(ContractModel):
    nickname: str
    wallet: str
    
class AddAccountStateInfo(MsgInfo):
    message_type: Literal["state"] = "state"
    message_name: Literal["add_account_state_cmd"] = "add_account_state_cmd"
    
class AddAccountStateCmdMsg(ControlMessage[AddAccountStatePayload]):
    message: AddAccountStateInfo
    payload: AddAccountStatePayload
    description: str = "Add account state"
