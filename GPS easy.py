from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
gps_0 = unit.get(unit.GPS, unit.PORTC)






label0 = M5Label('label0', x=238, y=77, color=0x000, font=FONT_MONT_14, parent=None)
label1 = M5Label('label1', x=243, y=102, color=0x000, font=FONT_MONT_14, parent=None)
label2 = M5Label('label2', x=248, y=129, color=0x000, font=FONT_MONT_14, parent=None)
label3 = M5Label('label3', x=238, y=154, color=0x000, font=FONT_MONT_14, parent=None)


while True:
  label0.set_text(str(gps_0.latitude_decimal))
  label1.set_text(str(gps_0.gps_time))
  label2.set_text(str(gps_0.longitude_decimal))
  label3.set_text(str(gps_0.pos_quality))
  wait_ms(2)