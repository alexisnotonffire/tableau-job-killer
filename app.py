from quart import Quart, render_template
from job_management import get_jobs_in_progress, cancel_job
import asyncio 

app = Quart(__name__)

@app.route('/')
@app.route('/killjob', defaults={'id': None})
@app.route('/killjob/<string:id>')
async def kill_jobs(id):
    failure = None
    if id != None:
        succeeded = cancel_job(id)
        if succeeded:
            print(f'cancelled job {id}')
        else:
            failure = id
            print(f'failed to cancel job {id}')

    jobs = get_jobs_in_progress()
    return await render_template('index.html', jobs=jobs, failure=failure)

app.run(port=8080)