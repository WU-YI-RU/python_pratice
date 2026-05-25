from pathlib import Path
import os
from datetime import datetime
import csv

ORDER_DIR = "orders"
CATALOG = {
    "御飯糰": 35,
    "礦泉水": 20,
    "布丁": 25,
    "關東煮": 15,
    "飯糰": 30,
    }

def main():

    try:
        if not os.path.exists(ORDER_DIR):
            os.makedirs(ORDER_DIR)
            print("已建立資料夾")

    except OSError as error:
        print(f"建立資料夾失敗:{error}")
    
    cart = {}

    p_list(CATALOG)
    while  True:
        target_line(" 選項清單 ","=",13)
        print(" 1) 新增購物車內容\n 2) 查看購物車\n 3) 移除商品\n " \
        "4) 結帳並生成訂單\n 5) 閱覽過去訂單\n 6) 修改過去訂單 7)刪除全部過去訂單 0 結束程式")
        
        mode = input()

        match mode:
            case "1":
                p_list(CATALOG)
                i_Cart(CATALOG,cart)
            case "2":
                s_cart(CATALOG,cart)
            case "3":
                d_cart(cart)
            case "4":
                b_cart(CATALOG,cart)
            case "5":
                p_file()
            case "6":
                u_file()
            case "7":
                d_file()
            case "0":
                print("結束本次購物，謝謝您的光臨")
                break
            case _:
                print("請輸入正確指令")


def target_line(name,type,n):
    for i in range(n):
        if name != "" and i == 6:
            print(name,end="")
            continue    
        print(type,end="")
    print("")

def p_list(c):
    target_line(" 商品名稱 ","=",13)
    for key,value in c.items():
        print(f"品名:{key}  單價:{value}")

def i_Cart(cat,c):
    qname = input("請輸入商品名稱:")
    if qname in cat:     
        try:
            qty = int(input("請輸入數量:"))
            if qty <= 0:
                print("請輸入正整數")
                target_line("","*",50)
            else:
                print(f"輸入數量:{qty}")
                c[qname] = c.get(qname,0) + qty
                print("已加入購物車")
                target_line("","=",50)
        except ValueError:
            print("數量必須是整數")
            target_line("","*",50)
    else:
        print("查無此商品")
        target_line("","*",50)

def s_cart(cat,c):
    if len(c) == 0:
        print("購物車為空")
        target_line("","*",50)
    else:
        sum = 0
        target_line(" 購物車 ","=",13)
        for key,value in c.items():
            print(f"{key}  {cat[key]} X {value} = {value*cat[key]} 元")
            sum += value * cat[key]
        target_line("","-",20)
        print(f"總金額: {sum} 元")
        print("")

def d_cart(c):
    if len(c) == 0:
        print("購物車為空")
        target_line("","*",50)
    else:
        all_keys = list(c.keys())
        print("目前購物車內有: ",end = "")
        for key in c:
            if key == all_keys[-1]:
                print(key)
            else:
                print(key,end = " / ")
        dname = input("請輸入預刪除的商品名稱:")
        if dname in c:
            del(c[dname])
            print(f"已刪除{dname}")
            target_line("","=",50)
        else:
            print("查無此商品")
            target_line("","*",50)

def b_cart(cat,c):
    if len(c) == 0:
        print("購物車為空，不可結帳")
        target_line("","*",50)
    else:
        order_time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"order_{order_time}.csv"
        filepath = os.path.join(ORDER_DIR,filename)
        try:
            with open(filepath,"w",encoding="utf-8-sig") as f:
                total = 0
                writer = csv.writer(f)
                writer.writerow(["訂單時間","商品名稱","單價","數量","小計"])
                for key,value in c.items():
                    writer.writerow([order_time,key,cat[key],value,value*cat[key]])
                    total += value*cat[key]
                    print(f"{key}  {cat[key]} X {value} = {value*cat[key]} 元")
                
                target_line("","-",20)
                print(f"共計:{total}元")
                print("")   
                print(f"印出訂單{filename}成功")
                target_line("","=",50)
        except OSError as error:
            print(f"建立資料夾失敗:{error}")
            target_line("","*",50)
        
def p_file():
    try:
        files = os.listdir(ORDER_DIR)
        csv_files = []

        for file in files:
            if file.endswith(".csv"):
                csv_files.append(file)
            if not csv_files:
                print("目前沒有任何訂單檔案，請買多一點")
                target_line("","*",50)
                continue

        target_line("","=",50)
        for file in csv_files:
            print(file)
        target_line("","=",50)

        return csv_files
    
    except OSError as error:
        print(f"讀取訂單資料失敗:{error}")
        target_line("","*",50)
        return []

def d_file():
    try:
        files = os.listdir(ORDER_DIR)
        has_csv = False

        for file in files:
            if file.endswith(".csv"):
                has_csv = True
                file_path = os.path.join(ORDER_DIR, file)
                os.remove(file_path)
                print(f"已成功刪除訂單檔案: {file} ")
            
        if not has_csv:
                print("目前沒有任何訂單檔案，請買多一點")
                target_line("","*",50)
        
    except FileNotFoundError:
        print(f"錯誤：找不到指定的資料夾 '{ORDER_DIR}'")
    except Exception as e:
        print(f"發生錯誤: {e}")

def u_file():
    csv_files = p_file()

    if not csv_files:
        return

    ch = input("請選擇指定檔案做修改(或輸入 0 取消):").strip()
    
    if ch == "0":
        print("已取消修改")
        return
    
    if ch in csv_files:
        file_path = os.path.join(ORDER_DIR,ch)
        print(f"成功找到檔案:{ch} 準備進行修改~")
        target_line("","=",50)

        order_data = {}
        
        try:
            with open(file_path,"r",encoding = "utf-8-sig") as f:
                reader = csv.reader(f)
                header = next(reader) #讓檔案的閱讀器前進一行
                
                for row in reader:
                    if row:
                        order_time = row[0]
                        item_name = row[1]
                        qty = int(row[2])

                        order_data[item_name] = qty
        except Exception as e:
            print(f"讀取檔案失敗: {e}")
            return
        
        print(f"印出當前訂單 {ch} 的商品明細 :")
        for item,q in order_data.items():
            print(f"商品: {item} | 數量: {q} | 單價: {cat.get(item, 0)} 元")
        target_line("", "=", 50)

        


if __name__ == "__main__":
    main()