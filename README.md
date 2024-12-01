## life game in python

![python](https://img.shields.io/badge/python-222?style=for-the-badge&logo=python)
![docker](https://img.shields.io/badge/docker-222?style=for-the-badge&logo=docker)

#### with docker

``` sh
docker image build --no-cache -f Dockerfile -t python-life:v1.0.0 .
```

``` sh
docker run -it --rm python-life:v1.0.0
```

#### run locally

``` sh
python app/app.py
```
