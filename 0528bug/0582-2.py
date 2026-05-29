import requests
from bs4 import BeautifulSoup

url = "https://www.vscinemas.com.tw/ShowTimes//ShowTimes/GetShowTimes"

args = {
    "CinemaCode" : "TP"
}
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Cookie":"ASP.NET_SessionId=oqicw0zizq4lmggh2a1lb5sk; BIGipServerbzel8JBItPXJdn/VVbM1mw=!dXiXeic5PAOk4+xxxQB2u9Yj1bQcGaIOdVVLxO8Nedw8M6I3dDvHv/BXh5kRjzgXKbfKqBZCZJtPHg==; _gid=GA1.3.1264543619.1779952961; _ga=GA1.3.1674381109.1779952961; QueueITAccepted-SDFrts345E-V3_landingpage=EventId%3Dlandingpage%26RedirectType%3Dsafetynet%26IssueTime%3D1779960171%26Hash%3Daaadb534a714cfa6068aa58b8961cfa015972ada7a748a83bf122808d6b3d049; RT=\"z=1&dm=www.vscinemas.com.tw&si=06208621-e57a-4586-9248-0c70636bd13e&ss=mpp61acz&sl=8&tt=5x&obo=7&rl=1\"; _ga_TK62J3JZHN=GS2.3.s1779960171$o2$g0$t1779960171$j60$l0$h0",
    "Referer":"https://www.vscinemas.com.tw/ShowTimes/",
    "origin":"https://www.vscinemas.com.tw^",
    "Accept":"*/*",
    "Accept-Language":"zh-TW,zh;q=0.9",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "X-requested-with":"XMLHttpRequest"
}
response = requests.post(url, data = args, headers = headers)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text,"html.parser")
result = soup.select("strong.col-xs-12.LangTW.MovieName")

for r in result:
    print(r.string)