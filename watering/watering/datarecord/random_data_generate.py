import MySQLdb
import random
import time 

db = MySQLdb.connect("127.0.0.1", "wangyiqing8866", "wyq123456789", "DATARECORD", charset='utf8' )
cursor = db.cursor()

while True:
    time_n = time.localtime(time.time())
    year = time_n[0]
    month = time_n[1]
    day = time_n[2]
    hour = time_n[3]
    minute = time_n[4]
    second = time_n[5]
    temperature = round(random.uniform(0,40),2)
    humidity = round(random.uniform(0,40),2)
    cursor.execute("insert into monitor_monitor_3 (year,month,day,hour,minute,second,temperature,humidity) values (%d,%d,%d,%d,%d,%d,%f,%f);"%(year,month,day,hour,minute,second,temperature,humidity))
    db.commit()
    time.sleep(3)

db.close()
