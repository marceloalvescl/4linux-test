from app import app
from utils.log import logger


if __name__ == '__main__':
    logger.info("Inicializando o serviço de backend Consumir APIs...")
    logger.info("Inicializado e pronto para uso!")
    app.run(host="127.0.0.1", port=int(81), debug=True)