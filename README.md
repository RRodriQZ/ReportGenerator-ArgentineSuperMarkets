# Report-ArgentineSuperMarkets #

Report from Argentine SuperMarkets prices.

* Supermercado Dia

# Pre Requirements 📋 #
* **Python 3**-**pipenv** / **Docker**

# Configure Gmail 📧
**Configure:** You credentials Gmail

1) Go to folder --> **./mail/config.ini**
2) Set your **user_Gmail** and **password_Gmail**
3) Accept Gmail authorization for application.
4) Go to --> **main.py** and set addressee

# Setup Python Virtual Environment 🔧 #
```cmd
pip install pipenv
```

**Windows** CMD:
```cmd
python -m venv venv
.\venv\Scripts\activate
pip install -e .
```
**Linux / MAC** command:
```cmd
python -m venv venv
source venv/bin/activate
python -m pip install -e .
```
# Running Python Script 🐼 #
```cmd
python main.py
```
**Unittest:**
```cmd
python test.py -v
```
# Running Docker 🐳
```cmd
docker build -t supermarket .
docker run -it supermarket
```
# Author 🖋 #
* Rodrigo Quispe - Developer - [RRodriQZ]

[RRodriQZ]: https://github.com/RRodriQZ