# Basic env

This repo are responsable to keep basic config to use Jupyter Notebook + BigQuery.


## Credential settings

Download your JSON credential service account to project and save in `workspace/keys/google_application_credentials.json`

This project authenticate with GCP using environment variable `GOOGLE_APPLICATION_CREDENTIALS`, then just save in this dir and works!


## Docker settings

From start this repo, go to `.` and run `docker compose up`


## How to use

From access jupyter UI, access `http://localhost:8888`