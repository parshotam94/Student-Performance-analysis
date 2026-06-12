
import logging, os
from datetime import datetime

os.makedirs("logs", exist_ok=True)
log_file = f"logs/{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(filename)s:%(lineno)d - %(message)s'
)
