# Web Crawler Of NGZK News 

## Build Setup

### Prerequisites
 - Python3
 - html2text
 - pymongo
 - beautifulsoup4
 - selenium
 - requests
 - lxml
 
It is recommended to use `pip` to install. Like:
```shell
sudo apt-get install python3-pip
pip3 install html2text pymongo beautifulsoup4 selenium requests lxml
```

### Optional
 - [MongoDB](https://docs.mongodb.com/manual/installation/): Data Persistence
    
    Service at localhost:27017 and non authorization.

 - [PhantomJS](http://phantomjs.org): Translate
    
    Should find in path.

### Build And Run
```shell
cd ${path to main.py}
python3 main.py
```
