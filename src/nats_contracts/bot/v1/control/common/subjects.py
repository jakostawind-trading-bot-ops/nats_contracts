BOT_TO_CONTROL_EVENT_V1_TEMPLATE = ("bot.{bot_id}.to.control.event.V1.{event_type}.{event_name}")

def generate_bot_to_control_event_V1_subject(
    bot_id: str,
    event_type: str,
    event_name: str
) -> str:
    return BOT_TO_CONTROL_EVENT_V1_TEMPLATE.format(
        bot_id=bot_id,
        event_type=event_type,
        event_name=event_name
    )