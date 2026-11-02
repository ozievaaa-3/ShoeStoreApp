# config.py
from configparser import ConfigParser
from pathlib import Path

config = ConfigParser()

config_path = Path(__file__).resolve().parent / "config.ini"

if not config_path.exists():
    raise FileNotFoundError(
        "Файл config.ini не найден. Создайте его на основе config.ini.example"
    )

config.read(config_path, encoding="utf-8")

DB_CONFIG = {
    'host': config.get('database', 'host'),
    'database': config.get('database', 'database'),
    'user': config.get('database', 'user'),
    'password': config.get('database', 'password'),
    'port': config.getint('database', 'port')
}