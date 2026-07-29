import pytest
from config.settings import settings

def test_settings_initialization():
    assert settings.PROJECT_NAME == "Climate Guardian AI"
    assert settings.VERSION == "1.0.0"
    assert settings.ENABLE_PROMPT_GUARD is True

def test_input_token_limits():
    assert settings.MAX_INPUT_TOKENS <= 8192
