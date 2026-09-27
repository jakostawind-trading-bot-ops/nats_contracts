CONTROL_TO_BOT_COMMANDS_JETSTEAM = "CONTROL_TO_BOT_COMMANDS"

CONTROL_TO_BOT_COMMAND_V1_TEMPLATE = (
    "control.to.bot.{bot_id}.command.{subject_suffix}"
)


def generate_control_to_bot_command_subject(
    bot_id: str,
    subject_suffix: str,
) -> str:
    return CONTROL_TO_BOT_COMMAND_V1_TEMPLATE.format(
        bot_id=bot_id,
        subject_suffix=subject_suffix,
    )
