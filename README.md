# Content Bot
A Telegram bot that generates AI-powered content using LLM providers (Gemini, Grok, etc.).
## Features
- Telegram bot interface
- AI content generation (Gemini integration)
- Modular provider system (Gemini, Grok, extensible)
- Clean service-based architecture
- Dependency-injected orchestration layer
- In-memory conversation history with SQLAlchemy persistence hooks
- Streaming-ready provider interface
- Ready for FastAPI expansion
## Project Structure

app/
├── bot/            # Telegram interface (commands, handlers, keyboards)
├── core/           # Configuration, constants, logging
├── providers/      # LLM integrations (Gemini, Grok)
├── services/       # Business logic (content generation, prompt building)
├── repositories/  # Data access layer (users, history)
├── models/        # DB models
├── schemas/       # Pydantic schemas
├── api/           # (Future) FastAPI routes
├── db/            # Database setup
└── main.py        # Entry point

## Setup
### 1. Clone repository
```bash
git clone https://github.com/barbodimani81/content-bot.git
cd content-bot

2. Create virtual environment

python -m venv .venv
source .venv/bin/activate  # macOS/Linux

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Create a .env file:

TELEGRAM_BOT_TOKEN=your_token_here
GEMINI_API_KEY=your_key_here
GROK_API_KEY=
DATABASE_URL=
LLM_PROVIDER=gemini

5. Run the bot

python app/main.py

Commands

* /start – Start the bot
* /help – Show help message

Architecture

The bot is designed with a layered architecture:

* Bot layer → Telegram interaction
* Service layer → Business logic
* Provider layer → AI model integration
* Repository layer → Data persistence (future)

This makes it easy to extend with:

* FastAPI REST API
* Multiple AI providers
* Database storage
* Streaming responses
* Web dashboard

Roadmap

* Inline keyboards (platform selection)
* Conversation state management
* Progress indicators
* FastAPI REST API
* User history tracking
* Admin dashboard

License

MIT
