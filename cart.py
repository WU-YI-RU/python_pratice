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

    p_list()
    while  True:
        target_line(" 選項清單 ","=",13)
        print(" 1) 新增購物車內容\n 2) 查看購物車\n 3) 移除商品\n " \
        "4) 結帳並生成訂單\n 5) 檢視過去訂單\n 6) 刪除全部訂單\n 0) 結束程式")
        
        mode = input()

        match mode:
            case "1":
                p_list()
                i_Cart(cart)
            case "2":
                s_cart(cart)
            case "3":
                d_cart(cart)
            case "4":
                b_cart(cart)
            case "5":
                u_file()
            case "6":
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

def p_list():
    target_line(" 商品名稱 ","=",13)
    for key,value in CATALOG.items():
        print(f"品名:{key}  單價:{value}")

def i_Cart(c):
    qname = input("請輸入商品名稱:")
    if qname in CATALOG:     
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

def s_cart(c):
    if len(c) == 0:
        print("購物車為空")
        target_line("","*",50)
    else:
        sum = 0
        target_line(" 購物車 ","=",13)
        for key,value in c.items():
            print(f"{key}  {CATALOG[key]} X {value} = {value*CATALOG[key]} 元")
            sum += value * CATALOG[key]
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

def b_cart(c,order_time = None):
    if len(c) == 0:
        print("購物車為空，不可結帳")
        target_line("","*",50)
    else:
        if order_time == None:
            order_time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"order_{order_time}.csv"
        filepath = os.path.join(ORDER_DIR,filename)
        try:
            with open(filepath,"w",encoding="utf-8-sig") as f:
                total = 0
                writer = csv.writer(f)
                writer.writerow(["訂單時間","商品名稱","單價","數量","小計"])
                for key,value in c.items():
                    writer.writerow([order_time,key,CATALOG[key],value,value*CATALOG[key]])
                    total += value*CATALOG[key]
                    print(f"{key}  {CATALOG[key]} X {value} = {value*CATALOG[key]} 元")
                
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
        print("無任何訂單紀錄")
        return

    ch = input("請選擇指定檔案檢視(或輸入 0 取消):").strip()
    
    if ch == "0":
        print("已取消檢視")
        return
    
    if ch in csv_files:
        file_path = os.path.join(ORDER_DIR,ch)
        print(f"成功找到檔案:{ch} 準備進行查看/修改/刪除~")
        target_line("","=",50)

        all_rows = []  #改用串列讀取
        
        try:
            with open(file_path,"r",encoding = "utf-8-sig") as f:
                reader = csv.reader(f)
                try:
                    header = next(reader) #讓檔案的閱讀器前進一行 嘗試將header刪除
                except StopIteration:
                    print("檔案為空")
                    return
                
                print(f"當前訂單{ch}的商品明細為:")

                #因目前在with內讀取檔案，因此需要縮排
                for row in reader:
                    if row:
                        all_rows.append(row)
                        print(f"訂單成立時間:{row[0]} | 商品名稱:{row[1]} | 商品數量:{row[3]}")

        except Exception as e:
            print(f"讀取檔案失敗: {e}")
            return

        uf_mod = input(" 1) 新增紀錄\n 0) 結束異動紀錄: ")
        match uf_mod:
            case "1":
                insert_row_to_file(file_path,header,all_rows)
            case "0":
                print("結束檢視，可以繼續購物了唷")
            case _:
                print("輸入錯誤指令")
    else:
        print("無該檔案")
        target_line("", "*", 20)

    
def insert_row_to_file(file_path,header,all_rows):
    print("\n當前檔案內容與行號: ")
    for index,item in enumerate(all_rows):
        print(f"行號{index + 1} : {item}")
    target_line("", "-", 20)

    try:
        max_line = len(all_rows)
        target_row = int(input(f"請輸入想要插入的行號 (1 ~ {max_line + 1}): "))
        if target_row < 1 or target_row > (max_line + 1):
            print(f"超出範圍，請輸入 1 到 {max_line + 1} 之間的數字")
            return
        target_row -= 1
    except ValueError:
        print("行號必須是整數")
        return
    
    p_list()
    qname = input("請輸入欲新增的商品名稱:")
    if qname not in CATALOG:
        print("查無此商品，取消新增")
        return
    try:
        qty = int(input("請輸入數量:"))
        if qty <= 0:
            print("數量必須大於 0")
            return
    except ValueError:
        print("數量必須是整數")
        return

    order_time = all_rows[0][0]
    price = CATALOG[qname]
    subtotal = price * qty
    new_row = [order_time, qname, price, qty, subtotal]

    all_rows.insert(target_row,new_row)
    print(f"\n已成功將商品 [{qname}] 插入到第 {target_row + 1} 行！")
    try:
        with open(file_path,"w",encoding = "utf-8-sig",newline = "") as f:
            writer = csv.writer(f)
             #單列資料
            writer.writerow(header)
             #多列資料
            writer.writerows(all_rows)
        print("檔案複寫成功!，異動已儲存")
        target_line("", "=", 50)
    except OSError as e:
        print(f"寫入檔案失敗: {e}")



if __name__ == "__main__":
    main()