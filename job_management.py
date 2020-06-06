import json 
import tableauserverclient as tsc 
import logging

# Set config for server
with open(f'{os.pwd()}/config.json') as f:
    cfg = json.load(f)['server']
    logging.info('loaded configuration file')


tableau = tsc.Server(cfg['url'], use_server_version=True)
auth = tsc.TableauAuth(cfg['user'], cfg['password'], cfg['site'])
# End config

def get_jobs_in_progress():
    with tableau.auth.sign_in(auth):
        return list(j for j in tsc.Pager(tableau.jobs))
    

def cancel_job(job_id):
    try:
        with tableau.auth.sign_in(auth):
            tableau.jobs.cancel(job_id)

        return True 
    except (tsc.InternalServerError, tsc.ServerResponseError, tsc.NonXMLResponseError):
        return False

