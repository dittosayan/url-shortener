from apscheduler.schedulers.blocking import BlockingScheduler
import string
import secrets
from pymongo import MongoClient

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='fri', hour=20)
def scheduled_job():
    con_string = os.getenv("mongo_con")
    conn = MongoClient(con_string)
    db = conn["url-shortner"]
    key_col = db["keys"]
    alphabet = string.ascii_letters + string.digits
    for i in range(100):
        x = ''.join(secrets.choice(alphabet) for i in range(6))
        resp = map_col.find_one({"key": str(x)})
        if resp== None:
            key_col.insert_one({"key": str(x)})

sched.start()
