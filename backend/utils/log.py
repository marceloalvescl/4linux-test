import logging 

logging.basicConfig(
    format=('%(asctime)s,%(msecs)-3d - %(name)-12s - %(levelname)-8s => '
            '%(message)s'),
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)