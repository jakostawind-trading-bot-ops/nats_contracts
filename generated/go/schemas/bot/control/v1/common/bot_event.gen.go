package common

type BotEvent struct {
	BotID     string      `json:"bot_id"`
	BotStatus string      `json:"bot_status"`
	Message   Message     `json:"message"`
	Payload   interface{} `json:"payload"`
	Timestamp string      `json:"timestamp"`
}

type Message struct {
	CausationID   string `json:"causation_id"`
	CorrelationID string `json:"correlation_id"`
	MessageID     string `json:"message_id"`
}
