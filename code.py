##Referencias 
# https://circuitpython-async-button.readthedocs.io/en/latest/#
# https://www.youtube.com/watch?v=VYeIR5n5Few&t=30s
import board
import busio
import adafruit_ssd1306
import time
import adafruit_dht
import touchio
from analogio import AnalogIn    
from digitalio import DigitalInOut, Direction, Pull
import asyncio
import digitalio
import async_button

touch1 = 0
touch2 = 0
touch3 = 0
touch4 = 0
touch5 = 0
touch6 = 0
temperatura = 0
umidade = 0
msg = ""
leitura_ldr = 0
i = 0
analog_in = AnalogIn(board.IO1)
inverter = False
i2c = busio.I2C(scl=board.IO9, sda=board.IO8)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)  

async def counter(oled):
    global touch1
    global touch2
    global touch6   
    global touch3
    global touch4
    global touch5
    global temperatura
    global umidade    
    global msg
    global inverter
    global analog_in
    global i
    
    btn2 = DigitalInOut(board.IO2)       # mapea para pino 5 
    btn2.direction = Direction.INPUT     # configura como entrada
    btn2.pull = Pull.UP                  # habilita pull-up interno

    btn3 = DigitalInOut(board.IO3)       # mapea para pino 5 
    btn3.direction = Direction.INPUT     # configura como entrada
    btn3.pull = Pull.UP                  # habilita pull-up interno
    def ler_tensao():
        global analog_in
        leitura_ldr = round((analog_in.value * 3.3)/65535*100,2) 
        return leitura_ldr

    try:
      inverter = False
      dht = adafruit_dht.DHT11(board.IO15)
      i = 0      
      while True:
        temperatura = dht.temperature
        umidade = dht.humidity
        if btn2.value ==0:               # Se botão pressionado
          touch1=1
        else:
          touch1=0
        if btn3.value ==0:               # Se botão pressionado
          touch2=1
        else:
          touch2=0      

        oled.invert(inverter)
        oled.fill(0)
        oled.rect(0, 0, 128, 64, 1)
        oled.rect(2, 2, 124, 60, 1)
        #oled.text('Franzininho Wifi', 4, 4, 1)
        oled.text(msg, 4, 4, 1)        
        oled.text("Temp: {:.1f} Umid: {}%".format(temperatura,umidade), 4, 14, 1)   
        oled.text("LDR: {:.1f}".format(ler_tensao()), 4, 24, 1)
        oled.text("But1: {} But2: {}".format(touch1,touch2), 4, 34, 1)
        oled.text("But3: {} But4: {}".format(touch3,touch4), 4, 44, 1)
        oled.text("But5: {} But6: {}".format(touch5,touch6), 4, 54, 1)                
        #oled.show()
        #inverter = not inverter
        time.sleep(.1)
        print(f"COUNTER: {i}")
        msg=""
        stmp = "                   {}".format(i)
        tmp = len(stmp)
        ttmp =(tmp-20)  
        #print(ttmp)
        #print(stmp[ttmp:tmp])
        oled.text(stmp[ttmp:tmp], 4, 4, 1)
        oled.show()        
        await asyncio.sleep(.1)        
        i += 1        
    finally:
      oled.invert(False)
      oled.fill(0)
      oled.show()

async def button_watcher(oled,Pin,Name):
    button = async_button.SimpleButton(Pin, value_when_pressed=False) 
#    global oled   
    global touch1   
    global touch2 
    global touch6   
    global touch3
    global touch4
    global touch5
    global temperatura
    global umidade   
    global msg
    def ler_tensao():
        global analog_in
        leitura_ldr = round((analog_in.value * 3.3)/65535*100,2) 
        return leitura_ldr    
    while True:
    
        await button.pressed()
        print("{} pressed-{}".format(Name,i))
        msg="{} pressed-{}".format(Name,i)        
        if Name=="But4":
            touch3 = 1
        if Name=="But5":
            touch4 = 1
        if Name=="But6":
            touch5 = 1
        if Name=="But7":
            touch6 = 1
        oled.invert(inverter)
        oled.fill(0)
        oled.rect(0, 0, 128, 64, 1)
        oled.rect(2, 2, 124, 60, 1)
        oled.text(msg, 4, 4, 1)
        oled.text("Temp: {:.1f} Umid: {}%".format(temperatura,umidade), 4, 14, 1)
        oled.text("LDR: {:.1f}".format(ler_tensao()), 4, 24, 1)
        oled.text("But1: {} But2: {}".format(touch1,touch2), 4, 34, 1)        
        oled.text("But3: {} But4: {}".format(touch3,touch4), 4, 44, 1)
        oled.text("But5: {} But6: {}".format(touch5,touch6), 4, 54, 1)                
        oled.show()
#        await asyncio.sleep(.1) 
        await button.released()
        if Name=="But4":
            touch3 = 0
        if Name=="But5":
            touch4 = 0
        if Name=="But6":
            touch5 = 0
        if Name=="But7":
            touch6 = 0   
        print("{} released-{}".format(Name,i))
        msg="{} released-{}".format(Name,i)
        oled.invert(inverter)
        oled.fill(0)
        oled.rect(0, 0, 128, 64, 1)
        oled.rect(2, 2, 124, 60, 1)
        oled.text(msg, 4, 4, 1)
        oled.text("Temp: {:.1f} Umid: {}%".format(temperatura,umidade), 4, 14, 1)
        oled.text("LDR: {:.1f}".format(ler_tensao()), 4, 24, 1)
        oled.text("But1: {} But2: {}".format(touch1,touch2), 4, 34, 1)                              
        oled.text("But3: {} But4: {}".format(touch3,touch4), 4, 44, 1)
        oled.text("But5: {} But6: {}".format(touch5,touch6), 4, 54, 1)                
        oled.show()
#        await asyncio.sleep(.1)        


async def main():
    await asyncio.gather(counter(oled), 
    button_watcher(oled,board.IO6,"But6"),     
    button_watcher(oled,board.IO7,"But7"), 
    button_watcher(oled,board.IO4,"But4"), 
    button_watcher(oled,board.IO5,"But5")) 
#    i = 0
    
asyncio.run(main())