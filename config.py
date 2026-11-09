import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "config.ini")

if not os.path.exists(config_path):
    raise FileNotFoundError(
        "Файл config.ini не найден. Создайте его по образцу config.ini.example"
    )

config.read(config_path, encoding="utf-8")

DB_CONFIG = {
    "host": config["database"]["host"],
    "database": config["database"]["database"],
    "user": config["database"]["user"],
    "password": config["database"]["password"],
    "port": config["database"].getint("port")
}