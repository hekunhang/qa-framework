import os
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT / "config" / "config.yaml"

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    _all = yaml.safe_load(f)

ENV = os.getenv("ENV") or _all["env"]
CONF = _all["envs"][ENV]

BASE_URL = CONF["base_url"]
TIMEOUT = CONF["timeout"]
USER = _all["user"]
