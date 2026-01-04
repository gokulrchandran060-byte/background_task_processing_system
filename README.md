# Background Task Processing System

## Overview
This project demonstrates background task execution using **Celery** in a **Django REST** application.
Long-running tasks are executed outside the API request–response cycle, and job execution progress is tracked using the database.

---

## Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL
- Celery
- Redis

---

## Problem Statement
Some backend operations take longer to complete and should not block API responses.
This project demonstrates how such operations can be executed in the background while allowing clients to track their progress.

---

## High-Level Architecture

Client
  |
  v
Django REST API
- Create job
- Trigger background task
  |
  v
Redis (Message Broker)
  |
  v
Celery Worker
- Execute task
- Update job status
  |
  v
PostgreSQL (Job state storage)

---

## What This Project Implements

### Background Task Execution
When a job is created through the API, execution is delegated to a **Celery worker** using Redis as a message broker.
The API does not wait for task completion.

---

### Job Tracking
Each job is stored in the database with a status field that tracks execution progress.

Job lifecycle:
PENDING → PROCESSING → COMPLETED

The worker updates the job status as execution progresses.

---

## API Endpoints

### Create Job
POST /api/v1/jobs/

Creates a job and triggers background execution.

Example request:
{
  "name": "Generate report"
}

---

### Get Job Status
GET /api/v1/jobs/{id}/

Returns the current execution status of the job.

---

## Background Worker Behavior
The Celery worker:
- Fetches the job from the database
- Marks it as PROCESSING
- Executes the task logic
- Updates the job status to COMPLETED

All execution happens outside the API process.

---

## Failure Behavior
If the message broker (Redis) is unavailable, task submission fails and the API returns an error.
This reflects the dependency of background execution on the broker.

---

## Scope and Limitations
This project focuses on demonstrating background task processing.

The following were intentionally kept out of scope:
- Scheduled tasks
- Retry mechanisms
- Multiple workers
- Real-time status updates

---

## Key Takeaways
- Background tasks can be executed independently of API requests
- Job execution state can be tracked using the database
- Celery workers operate separately from the Django API process

---

## Summary
This project demonstrates how Django APIs can trigger background jobs using Celery and Redis,
while tracking execution progress through a database-backed job model.

---


