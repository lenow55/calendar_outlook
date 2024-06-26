from typing import Tuple, Type

from pydantic import Field, SecretStr

from pydantic_settings import (
    BaseSettings,
    JsonConfigSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    """
    Класс настроек
    """

    client_id: str = Field(description="Url сервиса из НСИ")
    secret: SecretStr = Field(description="guid сервиса от заказчика")

    # список приоритетов файлов, последний файл приоритетнее,
    # поэтому debug_config не надо комитить
    model_config = SettingsConfigDict(json_file=("config.json", "debug_config.json"))

    # Определяю из каких источников и в какой последовательности
    # загружается конфиграция:
    # сначала переменные окружения, потом json файл
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            JsonConfigSettingsSource(settings_cls),
            file_secret_settings,
        )
