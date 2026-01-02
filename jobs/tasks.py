import time
from celery import shared_task
from .models import Job

@shared_task
def process_job(job_id):
    job = Job.objects.get(id=job_id)
    job.status = Job.STATUS_PROCESSING
    job.save(update_fields=["status"])

    time.sleep(20)

    job.status = Job.STATUS_COMPLETED
    job.save(update_fields=["status"])
