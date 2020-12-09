# [WIP]
## Clone Project
```
git clone https://github.com/hungvu193/ExchangeRateBot.git
```
## Install 
Create virtual environtment
```
cd projectfolder
```
```
python3 -m venv ./venv
```
```
source ./venv/bin/activate
```
Install spacy
```
pip3 install "rasa[spacy]"
```

Install vi-spacy-model
```
pip install https://github.com/trungtv/vi_spacy/raw/master/packages/vi_spacy_model-0.2.1/dist/vi_spacy_model-0.2.1.tar.gz
```

Install pyvi
```
pip install pyvi 
```

Link `vi_spacy_model`
```
python -m spacy link vi_spacy_model vi
```

## Run project
1. Run duckling server
```
docker run -p 8000:8000 rasa/duckling
```

2. Train model and start shell
```
rasa train & rasa shell
```
