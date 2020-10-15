
from . import MFRC522
import time

def leitura():
    try:
        LeitorRFID = MFRC522.MFRC522()

        print('Aproxime seu cartão RFID')

        while True:
            # Verifica se existe uma tag próxima do módulo.
            status, tag_type = LeitorRFID.MFRC522_Request(
                LeitorRFID.PICC_REQIDL)

            if status == LeitorRFID.MI_OK:
                print('Cartão detectado!')

                # Efetua leitura do UID do cartão.
                status, uid = LeitorRFID.MFRC522_Anticoll()

                if status == LeitorRFID.MI_OK:
                    uid = ':'.join(['%X' % x for x in uid])
                    print('UID do cartão: %s' % uid)
                    return uid

            time.sleep(.25)
    except Exception as e:
        return False
