# С использованием фреймворка pytest написать тест операции checkText SOAP API https://speller.yandex.net/services/spellservice?WSDL
#
# Тест должен использовать DDT и проверять наличие определенного
# верного слова в списке предложенных исправлений к определенному неверному слову.
#
# Слова должны быть заданы через фикстуры в conftest.py,
# адрес wsdl должен быть вынесен в config.yaml.
#
# Методы работы с SOAP должны быть вынесены в отдельную библиотеку.

import yaml
from zeep import Client, Settings

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)

settings = Settings(strict=False)
url_address = conf['url_address']
client = Client(wsdl=url_address, settings=settings)


def check_text(word: str):
    get_list = client.service.checkText(word)
    return get_list[0]['s']
