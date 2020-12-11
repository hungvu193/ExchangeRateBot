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
2. Start actions server
```
rasa run actions
```

3. Train model and start shell
```
rasa train & rasa shell
```


## License

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
