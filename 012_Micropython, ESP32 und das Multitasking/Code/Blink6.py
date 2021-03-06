# Wann wird ein Thread beendet
# und welche Threads sind noch vorhanden?
# Verbesserte Version mit LOCK

from machine import Pin
import time
import _thread

rot = Pin(33, Pin.OUT)
gruen = Pin(25, Pin.OUT)
gelb = Pin(32, Pin.OUT)

anzahl = 10
thread_list = set() # Liste der aktiven Threads
lock = _thread.allocate_lock() # Semaphor (Signalgeber)

def blink(name, led, pause):
    # Hier startet der Thread
    lock.acquire()
    thread_list.add(name)
    lock.release()
    for i in range(anzahl):
        led.on()
        time.sleep(pause)
        led.off()
        time.sleep(pause)
    # Hier wird der Thread beendet
    lock.acquire()
    thread_list.discard(name)
    lock.release()
        
_thread.start_new_thread(blink,("ROT", rot, 1))
_thread.start_new_thread(blink,("GELB", gelb, 0.5))
_thread.start_new_thread(blink,("GRUEN", gruen, 0.25))

# warten bis der erste Thread gestartet ist
while not thread_list: pass

# aktive Threads ausgeben, bis keiner mehr vorhanden ist
while thread_list:
    print(thread_list)
    time.sleep(0.05)

print("Jetzt bin ich wirklich fertig!")





