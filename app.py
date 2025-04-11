from flask import Flask
import logging
import random

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    logger.info("This is an INFO log")
    logger.warning("This is a WARNING log")
    logger.error("This is an ERROR log")
    return {"message": "Hello, welcome to the log test app!"}

@app.route('/random')
def random_log():
    level = random.choice(['info', 'warning', 'error', 'debug'])
    if level == 'info':
        logger.info("Random INFO log")
    elif level == 'warning':
        logger.warning("Random WARNING log")
    elif level == 'error':
        logger.error("Random ERROR log")
    else:
        logger.debug("Random DEBUG log")
    return {"log_level": level}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
