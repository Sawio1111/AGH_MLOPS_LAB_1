import pytest
import os
from unittest import mock
from settings import Settings
from pydantic_core import ValidationError

from main import export_envs


def test_settings_accepts_valid_environment(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "dev")
    monkeypatch.setenv("APP_NAME", "MyApp")
    monkeypatch.setenv("API_KEY", "secret")

    settings = Settings()

    assert settings.ENVIRONMENT == "dev"
    assert settings.APP_NAME == "MyApp"
    assert settings.API_KEY == "secret"


def test_settings_rejects_invalid_environment(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "invalid_env")
    monkeypatch.setenv("APP_NAME", "MyApp")
    monkeypatch.setenv("API_KEY", "secret")

    with pytest.raises(ValidationError) as exc_info:
        Settings()

    assert "Invalid environment" in str(exc_info.value)


@pytest.mark.parametrize(
    "env, expected_api_key",
    [("dev", "dev-key-from-yaml"), ("prod", "prod-key-from-yaml"), ("test", "")],
)
def test_export_env_sets_api_key(monkeypatch, env, expected_api_key):
    monkeypatch.delenv("API_KEY", raising=False)

    with mock.patch("yaml.safe_load", return_value={"API_KEY": expected_api_key}):
        monkeypatch.setattr("os.path.exists", lambda path: True)

        export_envs(env)

        assert os.environ["API_KEY"] == expected_api_key
