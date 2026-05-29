import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/CFantasy/index.html"

myheader = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
}

#try:
#    htmlFile = requests.get(url, headers = myheader)
#    print(htmlFile.txt)
#    filePath = "0528bug/0529/ptt-book-01.html"
#    with open(filePath,'wb') as file_obj:
#        #宣告每次讀取10240 長度的內容 (這裡不是換行用)
#        for diskStorage in htmlFile.iter_content(10240):
#            #使用檔案資源變數寫入檔案
#            size = file_obj.write(diskStorage)
#        print(size)
#            
#        print("檔案已儲存")
            
#except Exception as e:
#    print(e)
#    pass


repeat_time = 3
try:
    for i in range(0,repeat_time):
        htmlFile = requests.get(url, headers = myheader)
        result = BeautifulSoup(htmlFile.txt, "html.parser") #把回應文字放到bs4中解析
        paging = result.select(".btn-group.btn-group-paging a")
        prev_link = "" + paging[1]["href"]
        print(prev_link)

        titles = result.select(".title a")

        for title in titles:
            print(f"{title.txt},頁面連結: http://www.ptt.cc{title{"href"}}")
        
        print(paging)

except Exception as err:
    pass