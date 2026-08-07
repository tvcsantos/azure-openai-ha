"""Constants for the Azure OpenAI Conversation Integration."""

import logging

DOMAIN = "azure_openai_conversation"
LOGGER: logging.Logger = logging.getLogger(__package__)

CONF_API_BASE = "api_base"
CONF_API_MODE = "api_mode"
CONF_API_ROUTE = "api_route"
CONF_API_VERSION = "api_version"
CONF_CHAT_MODEL = "chat_model"
CONF_FILENAMES = "filenames"
CONF_MAX_TOKENS = "max_tokens"
CONF_PROMPT = "prompt"
CONF_PROMPT = "prompt"
CONF_REASONING_EFFORT = "reasoning_effort"
CONF_RECOMMENDED = "recommended"
CONF_TEMPERATURE = "temperature"
CONF_TOP_P = "top_p"
CONF_WEB_SEARCH = "web_search"
CONF_WEB_SEARCH_USER_LOCATION = "user_location"
CONF_WEB_SEARCH_CONTEXT_SIZE = "search_context_size"
CONF_WEB_SEARCH_CITY = "city"
CONF_WEB_SEARCH_REGION = "region"
CONF_WEB_SEARCH_COUNTRY = "country"
CONF_WEB_SEARCH_TIMEZONE = "timezone"

# Azure exposes two API surfaces. The `v1` route (`.../openai/v1/`) takes rolling
# version identifiers, while the older `deployments` route (`.../openai/deployments/`)
# takes dated ones and needs at least 2025-03-01-preview for the Responses API.
API_ROUTE_V1 = "v1"
API_ROUTE_DEPLOYMENTS = "deployments"
API_ROUTES: list[str] = [API_ROUTE_V1, API_ROUTE_DEPLOYMENTS]
DEFAULT_API_ROUTE = API_ROUTE_V1
DEFAULT_API_VERSIONS: dict[str, str] = {
    API_ROUTE_V1: "preview",
    API_ROUTE_DEPLOYMENTS: "2025-04-01-preview",
}

# Which API the conversation agent talks. The Responses API is preferred, but
# some gateways in front of Azure only expose the older Chat Completions API.
API_MODE_RESPONSES = "responses"
API_MODE_CHAT_COMPLETIONS = "chat_completions"
API_MODES: list[str] = [API_MODE_RESPONSES, API_MODE_CHAT_COMPLETIONS]
DEFAULT_API_MODE = API_MODE_RESPONSES

# Models that take `reasoning_effort` instead of `temperature`/`top_p`.
REASONING_MODEL_PREFIXES: tuple[str, ...] = ("o1", "o3", "o4", "gpt-5")

RECOMMENDED_CHAT_MODEL = "gpt-4o-mini"
RECOMMENDED_MAX_TOKENS = 150
RECOMMENDED_REASONING_EFFORT = "low"
RECOMMENDED_TEMPERATURE = 1.0
RECOMMENDED_TOP_P = 1.0
RECOMMENDED_WEB_SEARCH = False
RECOMMENDED_WEB_SEARCH_CONTEXT_SIZE = "medium"
RECOMMENDED_WEB_SEARCH_USER_LOCATION = False

UNSUPPORTED_MODELS: list[str] = [
    "o1-mini",
    "o1-mini-2024-09-12",
    "o1-preview",
    "o1-preview-2024-09-12",
    "gpt-4o-realtime-preview",
    "gpt-4o-realtime-preview-2024-12-17",
    "gpt-4o-realtime-preview-2024-10-01",
    "gpt-4o-mini-realtime-preview",
    "gpt-4o-mini-realtime-preview-2024-12-17",
]

WEB_SEARCH_MODELS: list[str] = [
    "gpt-4.1",
    "gpt-4.1-mini",
    "gpt-4o",
    "gpt-4o-search-preview",
    "gpt-4o-mini",
    "gpt-4o-mini-search-preview",
]
