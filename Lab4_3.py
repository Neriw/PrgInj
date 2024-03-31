from datetime import datetime
import time
for i in range(5):
    time.sleep(1)
    print(datetime.now().strftime('%H:%M:%S'))