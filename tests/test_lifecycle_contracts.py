import unittest

from pydantic import ValidationError

from nats_contracts.bot.control.v1.lifecycle.bot_started_ev import (
    BotStartedEvent,
    BotStartedEventInfo,
    BotStartedPayload,
)
from nats_contracts.control.bot.v1.lifecycle.run_bot_cmd import (
    RunBotCmd,
    RunBotCommandInfo,
    RunBotPayload,
)


class BotStartedEventTest(unittest.TestCase):
    def test_fields_match_bot_message_contract(self) -> None:
        event = BotStartedEvent(
            bot_id="bot-1",
            bot_status="running",
            message={"message_id": "message-1", "trace_id": "trace-1"},
            payload={},
            timestamp=1_726_350_000_000,
        )

        self.assertEqual(
            set(BotStartedEvent.model_fields),
            {
                "bot_id",
                "bot_status",
                "message",
                "payload",
                "description",
                "timestamp",
            },
        )
        self.assertIsInstance(event.message, BotStartedEventInfo)
        self.assertIsInstance(event.payload, BotStartedPayload)
        self.assertEqual(event.description, "Bot started")
        self.assertNotIn("msg", event.model_dump())

    def test_message_kind_is_validated(self) -> None:
        with self.assertRaises(ValidationError):
            BotStartedEventInfo(
                message_id="message-1",
                trace_id="trace-1",
                message_type="command",
            )


class RunBotCmdTest(unittest.TestCase):
    def test_fields_match_control_message_contract(self) -> None:
        command = RunBotCmd(
            bot_id="bot-1",
            message={"message_id": "message-1", "trace_id": "trace-1"},
            payload={},
            timestamp=1_726_350_000_000,
        )

        self.assertEqual(
            set(RunBotCmd.model_fields),
            {"bot_id", "message", "payload", "description", "timestamp"},
        )
        self.assertIsInstance(command.message, RunBotCommandInfo)
        self.assertIsInstance(command.payload, RunBotPayload)
        self.assertEqual(command.description, "")
        self.assertNotIn("msg", command.model_dump())

    def test_message_kind_is_validated(self) -> None:
        with self.assertRaises(ValidationError):
            RunBotCommandInfo(
                message_id="message-1",
                trace_id="trace-1",
                message_name="StopBotCommand",
            )


if __name__ == "__main__":
    unittest.main()
