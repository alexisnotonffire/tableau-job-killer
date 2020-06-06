# tableau-job-killer
Bare bones interface for killing tasks as currently not possible through the web UI.

Requires a config file matching the format in `config.json.template` to be passed through in the run command.

# quickstart
Up and running in just a handful of commands:
```sh
git clone git@github.com/alexisnotonffire/tableau-job-killer
# Fill out config.json.template now 
docker build -t tabjobkill .
docker run --rm -v $PWD/config.json.template:/app/config.json -p 9901:8080 tabjobkill
```
