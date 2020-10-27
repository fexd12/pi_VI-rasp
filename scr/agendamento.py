# -*- coding: utf-8 -*-

import datetime,time,requests
import RPi.GPIO as GPIO
from config import Config
from pi.leitura_tag import ler

def reles(acesso):

    if acesso:
        GPIO.output(pino_rele_1,1)
        GPIO.output(pino_rele_2,1)
    elif not acesso:
        GPIO.output(pino_rele_1,1)
        GPIO.output(pino_rele_2,0)
    elif acesso == 3:
        GPIO.output(pino_rele_1,0)
        GPIO.output(pino_rele_2,0)

def time_atual():
    data = datetime.datetime.today()

    data_atual = str(data.year) + '-' + str(data.month) + '-' + str(data.day)

    hora_atual = str(data.hour) + ':' + str(data.minute)

    return data_atual,hora_atual

pino_rele_1 = 20
pino_rele_2 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pino_rele_1, GPIO.OUT)
GPIO.setup(pino_rele_2, GPIO.OUT)

conf = Config()

reles(3)

"""
void httpGetAgendamento(String path)
{
  String dados = Get(path);

  if (!dados)
  {
    return;
  }

  //Serial.println("##[RESULT]## ==> " + dados);

  const size_t capacity = JSON_OBJECT_SIZE(12) + 210;

  DynamicJsonDocument doc(capacity);

  // Parse JSON object
  DeserializationError error = deserializeJson(doc, dados);

  if (error)
  {
    Serial.print(F("deserializeJson() failed: "));
    Serial.println(error.c_str());
    return;
  }

  int id = doc["id"];
  int sala_id = doc["sala_id"];
  int users_tags_id = doc["users_tags_id"];
  const char* usuario = doc["usuario"];
  const char* data = doc["data"];
  const char* horario_inicial = doc["horario_inicial"];
  const char* horario_final = doc["horario_final"];
  const char* tag = doc["tag"];
  int acesso = doc["acesso"];
  const char* sala = doc["sala"];
  const char* data_atual = doc["data_atual"];
  const char* hora_atual = doc["hora_atual"];

  if (acesso && data_atual == data && hora_atual == horario_inicial)
  {
    delay(500);
    Serial.println('ligando acesso 1');
    String hora = Get("hora");
    while (hora == horario_final)
    {
      digitalWrite(rele1, HIGH);
      digitalWrite(rele2, HIGH);
      delay(900000);//15 minutos para cada requisicao
      hora = Get("hora");
    }
    delay(500);
  }
  else if (!acesso  && data_atual == data && hora_atual == horario_inicial)
  {
    delay(500);
    Serial.println('ligando acesso 0');
    String hora = Get("hora");
    while (hora == horario_final) {
      digitalWrite(rele1, HIGH);
      digitalWrite(rele2, LOW);
      delay(900000);
      hora = Get("hora");
    }
    delay(500);
  }
  else
  {
    Serial.println('Tag nao possui agendamento.');
  }

} """


#agendamento_tag = url + + leitura()

while True:

    tag,_ = ler()

    response = requests.get(conf.HOST + '/tag/agendamento/' + tag)  # pegar agendamento
    agendamento = response.json()
    print(agendamento)

    data_atual,hora_atual  = time_atual()

    if agendamento['acesso'] and agendamento['data'] == data_atual and agendamento['hora'] == hora_atual:
        print('acesso 1')
        while agendamento['hora_final'] == hora_atual:
            reles(1)
            time.sleep(60)
            _,hora_atual = time_atual()
        reles(3)

    elif not agendamento['acesso'] and agendamento['data'] == data_atual and agendamento['hora'] == hora_atual:
        print('acesso 0')
        while agendamento['hora_final'] == hora_atual:
            reles(0)
            time.sleep(60)
            _,hora_atual = time_atual()
        reles(3)

    else:
        print('erro')
