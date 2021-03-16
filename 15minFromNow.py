import time
minutes = 15;
minutestoMillis = minutes * 1000 * 60;
millis = int(time.time() * 1000)
addtime = millis + minutestoMillis;

print(addtime)