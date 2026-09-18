BOT_TO_CONTROL_EVENT_V1_TEMPLATE = (
    "bot.{bot_id}.to.control.event.{subject_suffix}"
)


def generate_bot_to_control_event_subject(
    bot_id: str,
    subject_suffix: str,
) -> str:
    return BOT_TO_CONTROL_EVENT_V1_TEMPLATE.format(
        bot_id=bot_id,
        subject_suffix=subject_suffix,
    )
