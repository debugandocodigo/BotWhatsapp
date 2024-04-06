from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from time import sleep


# Função para inicializar o driver do Chrome
def get_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Função para enviar uma mensagem no WhatsApp
def send_message(driver, contato, message):
    try:
        # Localize o campo de pesquisa e digite o nome do contato
        search_box = driver.find_element('xpath', '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(contato)
        search_box.send_keys(Keys.ENTER)

        sleep(2)  # Aumente o tempo de espera se a página não carregar completamente

        # Localize o campo de entrada de texto e insira a mensagem
        message_box = driver.find_element('xpath', '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(message)

        message_box.send_keys(Keys.ENTER)  # Pressione Enter para enviar a mensagem

        sleep(5)  # Aumente o tempo de espera se a página não carregar completamente
    except Exception as e:
        print('Não foi possível enviar a mensagem')


# Inicialize o driver do Chrome
driver = get_driver()

# Abra o WhatsApp Web
driver.get('https://web.whatsapp.com/')
sleep(10)  # Aumente o tempo de espera se a página não carregar completamente

while True:
    while True:
        try:
            # Verifique se o QR Code foi escaneado
            qr_code = driver.find_element('xpath', '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas')
            if not qr_code:
                break
        except Exception as e:
            break

    sleep(20)  # Aumente o tempo de espera se a página não carregar completamente

    # Defina o contato e a mensagem que deseja enviar
    contato = 'Danillo'
    mensagem = 'Olá! Esta é uma mensagem automática.'

    # Envie a mensagem
    send_message(driver, contato, mensagem)

# Fechar o navegador
driver.quit()