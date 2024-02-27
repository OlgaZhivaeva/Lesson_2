# Bitly URL shortener

Use the app to create short links and track them

### How to install

Register on the website [Bitli](https://app.bitly.com/Bo1vhyBIxse/home)

Generate a token [GENERIC ACCESS TOKEN](https://app.bitly.com/settings/api)

Store the token in the `BITLY_TOKEN` variable in the  `.env` file:
```
BITLY_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### How to launch

Run the file `main.py`

``` 
python main.py
```


### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).