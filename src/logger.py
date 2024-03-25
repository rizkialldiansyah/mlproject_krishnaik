import logging
import sys
from datetime import datetime

# get logger
logger = logging.getLogger()

# create formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

# create handler
stream_handler = logging.StreamHandler(sys.stderr)  # Menggunakan sys.stderr untuk logging ke dalam kontainer Docker

# Menambahkan penanganan kesalahan saat membuat file handler
try:
    file_handler = logging.FileHandler('/app/app.log')  # Menyimpan file log di dalam direktori /app di dalam kontainer
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
except IOError as e:
    logger.error(f"Failed to create file handler: {e}")

# set formatter for stream handler
stream_handler.setFormatter(formatter)

# add handler to the logger
logger.addHandler(stream_handler)

# set log-level
logger.setLevel(logging.INFO)
