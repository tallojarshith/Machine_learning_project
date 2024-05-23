# Machine_learning_project


## Software And Account Requirements

1. [Gitcli](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
2. [herukoapp](https://www.heroku.com/)


## creating environment 
```
create conda -p venv python==3.7 -y
```
```
conda activate venv
```
```
pip install -r requirements.txt
```
To setup CI/CD pipeline in heruko we need 3 information

```
HEROKU_EMAIL=ramalatha0419@gmail.com
```
```
HERUKO_API_KEY=<>
```
```
HERUKO_APP_NAME=harshith-ml-regression
```
## Build DOCKER IMAGE
```
docker build -t <image_name>:<tagname>
```
>Note: image name for docker must be lowercase

## To list docker image
```
docker image
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 
```


To check running container in docker
```
docker ps
```


To stop docker container
```
docker stop <container_id>
```

Install ipykernel
```
pip install ipykernel
```
