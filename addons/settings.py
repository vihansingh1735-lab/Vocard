import os
from dotenv import load_dotenv
from typing import Dict, List, Any, Union, Optional

load_dotenv()


class Settings:
    def __init__(self, settings: Dict) -> None:
        # ================= REQUIRED =================

        # ---- DISCORD TOKEN ----
        self.token: Optional[str] = os.getenv("TOKEN") or settings.get("token")
        if not self.token or not isinstance(self.token, str):
            raise RuntimeError(
                "❌ DISCORD TOKEN NOT FOUND. "
                "Set environment variable TOKEN on Render."
            )

        # ---- CLIENT ID (SAFE PARSE) ----
        raw_client_id = settings.get("client_id") or os.getenv("CLIENT_ID")
        self.client_id: Optional[int] = None
        if raw_client_id and str(raw_client_id).isdigit():
            self.client_id = int(raw_client_id)

        # ================= OPTIONAL TOKENS =================

        self.genius_token: Optional[str] = (
            os.getenv("GENIUS_TOKEN") or settings.get("genius_token")
        )

        self.mongodb_url: Optional[str] = (
            os.getenv("MONGODB_URL") or settings.get("mongodb_url")
        )

        self.mongodb_name: Optional[str] = (
            os.getenv("MONGODB_NAME") or settings.get("mongodb_name")
        )

        # ================= BOT SETTINGS =================

        self.invite_link: str = "https://discord.gg/"

        self.nodes: Dict[str, Dict[str, Union[str, int, bool]]] = settings.get(
            "nodes", {}
        )

        self.max_queue: int = settings.get("default_max_queue", 1000)
        self.bot_prefix: Optional[str] = settings.get("prefix")

        self.activity: List[Dict[str, str]] = settings.get(
            "activity", [{"type": "listening", "name": "/help"}]
        )

        self.logging: Dict[str, Any] = settings.get("logging", {})

        # ---- EMBED COLOR ----
        raw_color = settings.get("embed_color", "0xb3b3b3")
        try:
            self.embed_color: int = int(raw_color, 16)
        except Exception:
            self.embed_color = 0xB3B3B3

        self.bot_access_user: List[int] = settings.get("bot_access_user", [])
        self.sources_settings: Dict[str, Dict[str, str]] = settings.get(
            "sources_settings", {}
        )

        self.cooldowns_settings: Dict[str, List[int]] = settings.get(
            "cooldowns", {}
        )

        self.aliases_settings: Dict[str, List[str]] = settings.get(
            "aliases", {}
        )

        self.controller: Dict[str, Dict[str, Any]] = settings.get(
            "default_controller", {}
        )

        self.voice_status_template: str = settings.get(
            "default_voice_status_template", ""
        )

        self.lyrics_platform: str = settings.get(
            "lyrics_platform", "lrclib"
        ).lower()

        self.ipc_client: Dict[str, Union[str, bool, int]] = settings.get(
            "ipc_client", {}
        )

        self.version: str = settings.get("version", "")
