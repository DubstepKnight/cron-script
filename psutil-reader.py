import psutil
import time
import json

def record_cpu_mmr_values():
    f = open('readings', 'a')
    mmr_dict = dict(time=time.time())
    mmr_dict['cpu_percent'] = psutil.cpu_percent()
    mmr_dict['vrtl-mmr'] = psutil.virtual_memory()
    available_mmr_prcnt = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    mmr_dict['used-mmr-prcnt'] = psutil.virtual_memory().percent
    mmr_dict['available-mmr-prcnt'] = available_mmr_prcnt
    f.write(json.dumps(mmr_dict))

while True:
    record_cpu_mmr_values()
    time.sleep(1)