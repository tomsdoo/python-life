## life game in python

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
