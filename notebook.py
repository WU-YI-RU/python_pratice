import json
from pathlib import Path


#class InvalidAmountError(Excepttion):
def clean():
    for i in range(100):
        print("=",end = "")

def main():

    file_path = Path("notebook.json")
if file_path.exists():
    print("檔案已存在")
    with open ("notebook.json","r",encoding = "utf-8") as f:
        loaded_data = json.load(f)
    print("先前的資料",loaded_data)
    print("資料型態",type(loaded_data))

else:
    print("檔案不存在")


    clean()
    print("個人記帳本")
    clean()
    mode = input("請輸入 1)新增    2)查看明細  3)儲存離開")
    data = {}



    




if __name__ == "__main__":
    main()