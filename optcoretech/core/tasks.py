from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
from core.models import Price
import pytz
 
 
logger = get_task_logger(__name__)
 
 
# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def scraper_example():
    now = datetime.now(pytz.timezone('Asia/Kolkata'))
    a = Price(current_time=now.time())
    a.save()