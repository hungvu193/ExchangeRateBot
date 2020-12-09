## Install 
```
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install "rasa[spacy]"
```

```
docker run -p 8000:8000 rasa/duckling
rasa train & rasa shell
```