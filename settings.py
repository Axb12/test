from typing import List, Dict

from pydantic import Field
from pydantic_settings import BaseSettings

class Config(BaseSettings):

    DEBUG: bool = Field(
        description="Enable debug mode for additional logging and development features",
        default=True,
    )

    FUNCTIONS: List[Dict[str, str]] = Field(
        description="chat functions",
        default=[
            {"name": "中译英", "description": "Chinese to English translation", "key": "c2e"},
            {"name": "英译中", "description": "English to Chinese translation", "key": "e2c"},
            {"name": "总结", "description": "Text summarization", "key": "summary"}
        ],
    )

    PROMPTS: Dict[str, str] = Field(
        description="chat prompts",
        default={
            "default": f"{{}}",
            "c2e": f"请把下列内容翻译为英文，内容如下：{{}}",
            "e2c": f"请把下列内容翻译为中文，内容如下：{{}}",
            "summary": f"请把下列内容总结，内容如下：{{}}"
        },
    )
settings = Config()