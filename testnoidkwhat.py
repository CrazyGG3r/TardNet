import logging
from datetime import datetime


current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

log_filename = f'.\\server log\\server_{current_time}.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logging.getLogger('').addHandler(console_handler)


logging.info('Server started')
logging.warning('Connection timeout')
logging.error('Internal server error')
