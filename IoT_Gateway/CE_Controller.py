from aiot_ir_receiver import *
from mqtt import *
from aiot_lcd1602 import LCD1602
import time
import music
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from aiot_rgbled import RGBLed
from machine import RTC
import ntptime
from event_manager import *
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20
import math

aiot_ir_rx = IR_RX(Pin(pin1.pin, Pin.IN)); aiot_ir_rx.start();

aiot_lcd1602 = LCD1602()

# Mô tả hàm này...
def Read_Pass___Information():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  if Check_PASS == 4:
    if aiot_ir_rx.get_code() == IR_REMOTE_A:
      if PASS == Password:
        Door = 'Open Door'
        mqtt.publish('iot_door', Door)
        aiot_lcd1602.clear()
        aiot_lcd1602.backlight_on()
        aiot_lcd1602.move_to(0, 0)
        aiot_lcd1602.putstr('PASSWORD')
        aiot_lcd1602.move_to(0, 1)
        aiot_lcd1602.putstr('PASSED')
        time.sleep_ms(1000)
        PASS = ''
        In_Home = 1
        Security = 0
        aiot_lcd1602.clear()
        Display_LCD()
      else:
        aiot_lcd1602.clear()
        aiot_lcd1602.backlight_on()
        aiot_lcd1602.move_to(0, 0)
        aiot_lcd1602.putstr('PASSWORD')
        aiot_lcd1602.move_to(0, 1)
        aiot_lcd1602.putstr('FAILED')
        Security = (Security if isinstance(Security, (int, float)) else 0) + 1
        time.sleep_ms(1000)
        PASS = ''
        Check_PASS = 0
        In_Home = 1
        aiot_lcd1602.clear()
        Display_LCD()
    if (aiot_ir_rx.get_code() == IR_REMOTE_C) or Change_Pass == 1:
      music.play(music.DADADADUM, wait=False)
      if Change_Pass == 1:
        Password = PASS
        mqtt.publish('iot_door', Door)
        aiot_lcd1602.clear()
        aiot_lcd1602.backlight_on()
        aiot_lcd1602.move_to(0, 0)
        aiot_lcd1602.putstr('PASSWORD')
        aiot_lcd1602.move_to(0, 1)
        aiot_lcd1602.putstr('SUCCESS')
        time.sleep_ms(1000)
        PASS = ''
        Change_Pass = 0
        Check_PASS = 0
        In_Home = 1
        Security = 0
        aiot_lcd1602.clear()
        Display_LCD()
      else:
        Change_Pass = 1
        Check_PASS = 0
        Password = ''
        PASS = ''
    Counter = 0
  elif Check_PASS > 4:
    aiot_lcd1602.clear()
    aiot_lcd1602.move_to(0, 0)
    aiot_lcd1602.putstr('PASSWORD')
    aiot_lcd1602.move_to(0, 1)
    aiot_lcd1602.putstr('FAILED')
    Security = (Security if isinstance(Security, (int, float)) else 0) + 1
    time.sleep_ms(1000)
    PASS = ''
    Check_PASS = 0
    In_Home = 1
    aiot_lcd1602.clear()
    Display_LCD()
  elif Security >= 2:
    aiot_lcd1602.clear()
    aiot_lcd1602.move_to(0, 0)
    aiot_lcd1602.putstr('LOCKED')
    aiot_lcd1602.move_to(0, 1)
    aiot_lcd1602.putstr('SEREVAL MINUTES')
    time.sleep_ms(500)
    aiot_lcd1602.clear()
    Display_LCD()
    time.sleep_ms(500)
    Security_Counter = (Security_Counter if isinstance(Security_Counter, (int, float)) else 0) + 2
  elif Check_PASS < 4 and Counter >= 10:
    Check_PASS = 0
    PASS = ''
    Security = 0
    In_Home = 1
    Counter = 0
    aiot_lcd1602.clear()
    Display_LCD()

# Mô tả hàm này...
def Signal_Remote():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  if Security_Counter >= 5:
    Security = 0
    Security_Counter = 0
    aiot_lcd1602.clear()
    Display_LCD()
  if aiot_ir_rx.get_code() == IR_REMOTE_SETUP:
    if Earthquake == 0:
      In_Home = 0
  if In_Home == 0:
    if Stable == 0:
      Stable = 1
      if aiot_ir_rx.get_code() == IR_REMOTE_0:
        PASS = str(PASS) + '0'
        music.play(['G3:1'], wait=True)
        Display_Pass()
      if aiot_ir_rx.get_code() == IR_REMOTE_1:
        PASS = str(PASS) + '1'
        music.play(['G3:1'], wait=True)
        Display_Pass()
      if aiot_ir_rx.get_code() == IR_REMOTE_2:
        PASS = str(PASS) + '2'
        music.play(['G3:1'], wait=True)
        Display_Pass()
      if aiot_ir_rx.get_code() == IR_REMOTE_3:
        PASS = str(PASS) + '3'
        music.play(['G3:1'], wait=True)
        Display_Pass()
      if aiot_ir_rx.get_code() == IR_REMOTE_4:
        PASS = str(PASS) + '4'
        music.play(['G3:1'], wait=True)
        Display_Pass()
      if aiot_ir_rx.get_code() == IR_REMOTE_5:
        PASS = str(PASS) + '5'
        music.play(['G3:1'], wait=True)
        Display_Pass()
      if aiot_ir_rx.get_code() == IR_REMOTE_6:
        PASS = str(PASS) + '6'
        music.play(['G3:1'], wait=True)
        Display_Pass()
      if aiot_ir_rx.get_code() == IR_REMOTE_7:
        PASS = str(PASS) + '7'
        music.play(['G3:1'], wait=True)
        Display_Pass()
      if aiot_ir_rx.get_code() == IR_REMOTE_8:
        PASS = str(PASS) + '8'
        music.play(['G3:1'], wait=True)
        Display_Pass()
      if aiot_ir_rx.get_code() == IR_REMOTE_9:
        PASS = str(PASS) + '9'
        music.play(['G3:1'], wait=True)
        Display_Pass()
      Stable = 0
    Read_Pass___Information()
    aiot_ir_rx.clear_code()
    time.sleep_ms(200)
    Counter = (Counter if isinstance(Counter, (int, float)) else 0) + 1

# Mô tả hàm này...
def Initialize_Variables():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  DataHTTP = ''
  Sequential = 59
  In_Home = 1
  Stable = 0
  Clock = 0
  Counter = 0
  Security = 0
  Security_Counter = 0
  Earthquake = 0
  Home_mode = ''
  PASS = ''
  Password = '1111'
  Check_PASS = 0
  Change_Pass = 0
  Face_ID = ''
  Door = ''
  Fan_State = 0
  Fan = ''
  Control_Fan = 0
  Fanspeed = 0
  Alarm_State = 0
  Alarm = ''
  Temperature = 0
  Humidity = 0
  Light = ''
  Brightness = ''
  Fire = ''
  th_C3_B4ng_tin = ''
  th_C3_B4ng_tin_2 = ''
  th_C3_B4ng_tin_3 = ''

# Mô tả hàm này...
def Display():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  display.show(Image("01001:10101:10101:11101:10101"))
  time.sleep_ms(200)
  display.show(Image("10010:01010:01010:11010:01010"))
  time.sleep_ms(200)
  display.show(Image("00100:10101:10101:10101:10100"))
  time.sleep_ms(200)
  display.show(Image("01001:01010:01010:01010:01001"))
  time.sleep_ms(200)
  display.show(Image("10010:10101:10101:10101:10010"))
  time.sleep_ms(200)
  display.show(Image("00100:01010:01010:01010:00100"))
  time.sleep_ms(200)
  display.show(Image("01011:10101:10101:10101:01001"))
  time.sleep_ms(200)
  display.show(Image("10111:01010:01010:01010:10010"))
  time.sleep_ms(200)
  display.show(Image("00000:00000:00000:00000:00000"))
  time.sleep_ms(200)

def on_mqtt_message_receive_callback__iot_fan_(Fan):
  global DataHTTP, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan
  if Fan == 'Fan On':
    mqtt.publish('iot_fanspeed', '50')
    Fan = 'Fan On'
    Fan_State = 0
  elif Fan == 'Fan Off':
    if Fan_State == 0:
      mqtt.publish('iot_fanspeed', '0')
      Fan = 'Fan Off'

def on_mqtt_message_receive_callback__iot_fanspeed_(th_C3_B4ng_tin):
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan
  Fanspeed = int(th_C3_B4ng_tin)
  if Fanspeed == 0 and Fan == 'Fan On':
    mqtt.publish('iot_fan', 'Fan Off')
    Fan_State = 1
  pin10.write_analog(round(translate(Fanspeed, 0, 100, 0, 1023)))

# Mô tả hàm này...
def Fan2():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  mqtt.on_receive_message('iot_fan', on_mqtt_message_receive_callback__iot_fan_)
  mqtt.on_receive_message('iot_fanspeed', on_mqtt_message_receive_callback__iot_fanspeed_)

def on_mqtt_message_receive_callback__iot_alarm_(Alarm):
  global DataHTTP, Fan, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan
  if Alarm == 'Alarm On':
    mqtt.publish('iot_state', '1')
    Alarm = 'Alarm On'
    Alarm_State = 0
  elif Alarm == 'Alarm Off':
    if Alarm_State == 0:
      mqtt.publish('iot_state', '0')
      Alarm = 'Alarm Off'

tiny_rgb = RGBLed(pin16.pin, 4)

def on_mqtt_message_receive_callback__iot_state_(Brightness):
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan
  tiny_rgb.show(0, hex_to_rgb('#000000'))
  if Brightness == '0':
    if Alarm == 'Alarm On':
      mqtt.publish('iot_alarm', 'Alam Off')
      tiny_rgb.show(0, hex_to_rgb('#000000'))
      Alarm_State = 1
  elif Brightness == '1':
    tiny_rgb.show(1, hex_to_rgb('#ffffff'))
  elif Brightness == '2':
    tiny_rgb.show(1, hex_to_rgb('#ffffff'))
    tiny_rgb.show(2, hex_to_rgb('#ffffff'))
  elif Brightness == '3':
    tiny_rgb.show(1, hex_to_rgb('#ffffff'))
    tiny_rgb.show(2, hex_to_rgb('#ffffff'))
    tiny_rgb.show(3, hex_to_rgb('#ffffff'))
  elif Brightness == '4':
    tiny_rgb.show(0, hex_to_rgb('#ffffff'))

# Mô tả hàm này...
def Alarm2():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  mqtt.on_receive_message('iot_alarm', on_mqtt_message_receive_callback__iot_alarm_)
  mqtt.on_receive_message('iot_state', on_mqtt_message_receive_callback__iot_state_)

# Mô tả hàm này...
def Connect_Wifi():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  mqtt.connect_wifi('Tung', 'concutao')
  mqtt.connect_broker(server='io.adafruit.com', port=1883, username='QuangThien15', password='aio_nbtt54UiRqRCXHtxZLXXU1an2GOd')

def on_mqtt_message_receive_callback__iot_door_(Door):
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan
  if Door == 'Open Door':
    pin0.servo_write(0)
    time.sleep_ms(1000)
    pin0.servo_release()
  elif Door == 'Close Door':
    pin0.servo_write(90)
    time.sleep_ms(1000)
    pin0.servo_release()

# Mô tả hàm này...
def Door2():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  mqtt.on_receive_message('iot_state', on_mqtt_message_receive_callback__iot_state_)
  mqtt.on_receive_message('iot_door', on_mqtt_message_receive_callback__iot_door_)

event_manager.reset()

def sound_alarm():
  for count in range(5):
    music.play(['A5:1'], wait=True)
    music.play(['E5:1'], wait=True)

# Mô tả hàm này...
def Earthquake2():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  if accelerometer.sensor.shake(11.5):
    aiot_lcd1602.clear()
    aiot_lcd1602.move_to(0, 0)
    aiot_lcd1602.putstr('Warning!!!')
    aiot_lcd1602.move_to(0, 1)
    aiot_lcd1602.putstr('Earthquake!!!')
    sound_alarm()
    Earthquake = 1
    Sequential = 1
    In_Home = 1
    display.show(Image.NO)

def on_event_timer_callback_Y_X_t_r_W():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan
  Sequential = (Sequential if isinstance(Sequential, (int, float)) else 0) + 1
  if In_Home == 1 and Sequential == 60 and Earthquake == 0:
    display.show(Image.SMILE)
    Display_LCD()
    Sequential = 1
  if Earthquake == 1 and Sequential == 20:
    Display_LCD()
    Earthquake = 0
    Sequential = 1

event_manager.add_timer_event(1000, on_event_timer_callback_Y_X_t_r_W)

# Mô tả hàm này...
def Display_Pass():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  aiot_lcd1602.clear()
  Check_PASS = len(PASS)
  if Check_PASS == 1:
    Display_PASS = PASS[-1]
  elif Check_PASS == 2:
    Display_PASS = '*' + str(PASS[-1])
  elif Check_PASS == 3:
    Display_PASS = '**' + str(PASS[-1])
  else:
    Display_PASS = '***' + str(PASS[-1])
  aiot_lcd1602.backlight_on()
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr('PASSWORD')
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr(Display_PASS)

def on_mqtt_message_receive_callback__iot_temperature_(th_C3_B4ng_tin_2):
  global DataHTTP, Fan, Alarm, Face_ID, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan
  Temperature = int(th_C3_B4ng_tin_2)

def on_mqtt_message_receive_callback__iot_humidity_(th_C3_B4ng_tin_3):
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan
  Humidity = int(th_C3_B4ng_tin_3)

# Mô tả hàm này...
def Temperature___Humidity():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  mqtt.on_receive_message('iot_temperature', on_mqtt_message_receive_callback__iot_temperature_)
  mqtt.on_receive_message('iot_humidity', on_mqtt_message_receive_callback__iot_humidity_)

def on_mqtt_message_receive_callback__iot_mode_(Home_mode):
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan
  if Home_mode == 'In Home':
    music.play(music.DADADADUM, wait=True)
    In_Home = 1
    aiot_lcd1602.backlight_on()
    Display_LCD()
  elif Home_mode == 'Out Home':
    music.play(music.RINGTONE, wait=True)
    In_Home = 0
    aiot_lcd1602.backlight_off()
    aiot_lcd1602.clear()

# Mô tả hàm này...
def Operating():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  if Clock == 0:
    Clock = 1
    mqtt.on_receive_message('iot_mode', on_mqtt_message_receive_callback__iot_mode_)
    Clock = 0
  Fan2()
  Door2()
  Alarm2()
  Temperature___Humidity()

def on_event_timer_callback_Y_X_t_S_m():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan
  if Temperature > 45 or Humidity > 0 and Humidity < 10:
    Temperature = 0
    Humidity = 0
    for count in range(5):
      LED_RGB()
    Fire = 'Fire'
    mqtt.publish('iot_fire', Fire)

event_manager.add_timer_event(1000, on_event_timer_callback_Y_X_t_S_m)

aiot_dht20 = DHT20(SoftI2C(scl=Pin(22), sda=Pin(21)))

# Mô tả hàm này...
def Display_LCD():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  aiot_dht20.read_dht20()
  Humidity = aiot_dht20.dht20_temperature()
  Humidity = round(Humidity)
  mqtt.publish('iot_humidity', Humidity)
  time.sleep_ms(200)
  Temperature = aiot_dht20.dht20_humidity()
  Temperature = round(((Temperature - 32) * 5) / 9)
  mqtt.publish('iot_temperature', Temperature)
  time.sleep_ms(200)
  Light = round(translate((pin2.read_analog()), 0, 4095, 0, 100))
  mqtt.publish('iot_light', Light)
  time.sleep_ms(200)
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr(Temperature)
  aiot_lcd1602.move_to(2, 0)
  aiot_lcd1602.putstr('*C')
  aiot_lcd1602.move_to(4, 0)
  aiot_lcd1602.putstr('  ')
  aiot_lcd1602.move_to(6, 0)
  aiot_lcd1602.putstr(Humidity)
  aiot_lcd1602.move_to(8, 0)
  aiot_lcd1602.putstr('%')
  aiot_lcd1602.move_to(9, 0)
  aiot_lcd1602.putstr('H')
  aiot_lcd1602.move_to(10, 0)
  aiot_lcd1602.putstr('  ')
  aiot_lcd1602.move_to(12, 0)
  aiot_lcd1602.putstr(Light)
  aiot_lcd1602.move_to(14, 0)
  aiot_lcd1602.putstr('%')
  aiot_lcd1602.move_to(15, 0)
  aiot_lcd1602.putstr('L')
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr(('%0*d' % (2, RTC().datetime()[2])))
  aiot_lcd1602.move_to(2, 1)
  aiot_lcd1602.putstr('/')
  aiot_lcd1602.move_to(3, 1)
  aiot_lcd1602.putstr(('%0*d' % (2, RTC().datetime()[1])))
  aiot_lcd1602.move_to(5, 1)
  aiot_lcd1602.putstr('/')
  aiot_lcd1602.move_to(6, 1)
  aiot_lcd1602.putstr((('%0*d' % (2, RTC().datetime()[0]))[2 : 4]))
  aiot_lcd1602.move_to(8, 1)
  aiot_lcd1602.putstr('   ')
  aiot_lcd1602.move_to(11, 1)
  aiot_lcd1602.putstr(('%0*d' % (2, RTC().datetime()[4])))
  aiot_lcd1602.move_to(13, 1)
  aiot_lcd1602.putstr(':')
  aiot_lcd1602.move_to(14, 1)
  aiot_lcd1602.putstr(('%0*d' % (2, RTC().datetime()[5])))
  time.sleep_ms(100)

# Mô tả hàm này...
def LED_RGB():
  global DataHTTP, Fan, Alarm, Face_ID, th_C3_B4ng_tin_2, Check_PASS, Security, Sequential, th_C3_B4ng_tin, Brightness, Door, Temperature, th_C3_B4ng_tin_3, Clock, Humidity, PASS, Security_Counter, In_Home, Fanspeed, Home_mode, Counter, Stable, Display_PASS, Password, Earthquake, Fan_State, Alarm_State, Fire, Change_Pass, Light, Control_Fan, aiot_lcd1602, aiot_dht20, tiny_rgb, aiot_ir_rx
  music.play(music.DADADADUM, wait=False)
  tiny_rgb.show(1, hex_to_rgb('#ff0000'))
  tiny_rgb.show(2, hex_to_rgb('#ffff00'))
  tiny_rgb.show(3, hex_to_rgb('#00ff00'))
  tiny_rgb.show(4, hex_to_rgb('#0000ff'))
  time.sleep_ms(250)
  tiny_rgb.show(1, hex_to_rgb('#0000ff'))
  tiny_rgb.show(2, hex_to_rgb('#ff0000'))
  tiny_rgb.show(3, hex_to_rgb('#ffff00'))
  tiny_rgb.show(4, hex_to_rgb('#00ff00'))
  time.sleep_ms(250)
  tiny_rgb.show(1, hex_to_rgb('#00ff00'))
  tiny_rgb.show(2, hex_to_rgb('#0000ff'))
  tiny_rgb.show(3, hex_to_rgb('#ff0000'))
  tiny_rgb.show(4, hex_to_rgb('#ffff00'))
  time.sleep_ms(250)
  tiny_rgb.show(1, hex_to_rgb('#ffff00'))
  tiny_rgb.show(2, hex_to_rgb('#00ff00'))
  tiny_rgb.show(3, hex_to_rgb('#0000ff'))
  tiny_rgb.show(4, hex_to_rgb('#ff0000'))
  time.sleep_ms(250)
  tiny_rgb.show(0, hex_to_rgb('#ffffff'))
  time.sleep_ms(1000)
  tiny_rgb.show(0, hex_to_rgb('#000000'))

if True:
  Connect_Wifi()
  display.show(Image.HEART)
  Display()
  Initialize_Variables()
  ntptime.settime()
  (year, month, mday, week_of_year, hour, minute, second, milisecond) = RTC().datetime()
  RTC().init((year, month, mday, week_of_year, hour+7, minute, second, milisecond))
  aiot_lcd1602.clear()
  aiot_lcd1602.backlight_on()
  aiot_ir_rx.clear_code()
  Operating()

while True:
  event_manager.run()
  mqtt.check_message()
  Signal_Remote()
  Earthquake2()
  time.sleep_ms(1000)
