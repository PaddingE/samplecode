# beautiful_flask.py

from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route("/")

def hello():
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    
    soup = BeautifulSoup(target, "html.parser")
    
    output = ""
    for location in soup.select("location"):
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
                )
        output += "<hr/>"
    return output


#flask 설치가 안 돼있으면 콘솔에 pip install flask 입력

#콘솔에 set FLASK_APP=day0425_01_beautiful_flask.py 입력해야 flask 실행시 지정 파일 실행

#파일이 폴더 안에 있는경우
#예) 실행 파일이 samplecode/samplecode_0425 안에 있다고 할때
#    콘솔 명령어를 이용하여 cd samplecode_0425 입력해서
#    samplecode0425 폴더 안으로 이동해서 flask run 명령 사용