"""Logger module"""

import logging

from pathlib import Path

logger = logging.getLogger("trail_pipeline")

# Set up the logging level
logger.setLevel("DEBUG")

# Define console logging
console_handler = logging.StreamHandler()
console_handler.setLevel("WARNING")
logger.addHandler(console_handler)

# Log file path
path = Path(__file__).parent.parent.parent.joinpath("data", "logs", "pipeline.log")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

# Define file logging
file_handler = logging.FileHandler(path, mode="a", encoding="utf-8")
file_handler.setLevel("DEBUG")
logger.addHandler(file_handler)

# Define a logging format
formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

