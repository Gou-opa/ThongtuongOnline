from engine.server.economy import Economy
from engine.server.nature import Resource
from configs import *
import time

counter = 0
while True:
    Economy.tick()
    if counter % 100:
        time.sleep(BILL_TIME)
        continue
    else:
        Resource.creation()
        counter += 1