import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name="monitor", log_dir="logs", file="monitor.log"):
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        os.path.join(log_dir, file),
        maxBytes=5_000_000,
        backupCount=3,
        encoding="utf-8"
    )
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger
