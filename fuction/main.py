
import logging

from test import x

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m_%d %H:%M:%S %p', format='%(asctime)s-%(levelname)s-%(name)s-%(message)s', handlers=[logging.FileHandler(filename='project.log', mode='w'), logging.StreamHandler()])
logger = logging.getLogger(__name__)

with open('平方.txt', 'w', encoding='utf-8') as f:
    for i in range(20):
        b = x(i)
        f.write(f'{b}')
        logger.info(f'{i}的平方值已写入文件')
