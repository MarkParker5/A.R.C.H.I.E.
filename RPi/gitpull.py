from .RPi import *
import os
from Command import Callback
import config
################################################################################
def reboot(params):
    if params['bool']:
        os.system('sudo reboot')
    return {
        'text': 'Хорошо',
        'voice': 'Хорошо',
        'type': 'simple',
    }

reboot_cb = Callback(['$text',])
reboot_cb.setStart(reboot)

@RPi.background(answer = 'Проверяю обновления...', voice = 'Проверяю обновления')
def method(params, finish_event):
    if not os.popen('git -C '+config.path+' fetch').readline():
        finish_event.set()
        return {
            'text': 'Установлена последняя версия',
            'voice': 'Установлена последняя версия',
            'type': 'simple',
        }
    os.system('git -C '+config.path+' pull')
    finish_event.set()
    return {
        'text': 'Обновления скачаны. Перезагрузиться?',
        'voice': 'Обновления скачаны. Перезагрузиться?',
        'type': 'question',
        'callback': reboot_cb,
    }

patterns = ['* обновись *', '* можешь обновиться *', '* обнови себя *', '* скачай обновления *']
gitpull = RPi('git pull archie.git', [], patterns)
gitpull.setStart(method)
