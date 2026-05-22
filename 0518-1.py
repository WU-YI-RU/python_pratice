

def main():
    catalog = {
    "御飯糰": 35,
    "礦泉水": 20,
    "布丁": 25,
    "關東煮": 15,
    "飯糰": 30,
    }
    mode = 1
    car = {}

    while mode != 0:
        clean()
        print("請選擇\n" 
        "1)新增商品\n" 
        "2)移除商品\n" 
        "3)查看購物車\n" 
        "4)結帳\n" 
        "5)離開：輸入 0 結束" )
        
        mode = input()
        clean()

        match mode:
            case "1":
                newObj(catalog,car)
                clean()
            case "2":
                delObj(catalog,car)
                clean()
            case "3":
                chObj(catalog,car)
                clean()
            case "4":
                overObj(catalog,car)
                clean()
            case _:
                print("輸入未知數請重新輸入")
                clean()


def newObj(catalog,car):
    name = str(input("請輸入商品名稱:"))

    if name not in catalog:
        print("ERROR，商品不再名單內")
    else:
        num = int(input("請輸入商品數量:"))
        #car.setdefault(name,num) 只能創建新的item
        #已存在不存在都可以處理，還可以累加
        car[name] = car.get(name,0)+num

def delObj(catalog,car):
    if car != {}:
        name = input("輸入商品名稱:")
        if name not in catalog:
            print("無此商品")
        else:
            del car[name]
            print(f"刪除成功{name}")
    else:
        print("窮到沒東西可以刪")
    
def chObj(catalog,car):
    if car != {}:
        for key,value in car.items():
            sum = catalog[key]*value
            print(f"商品名稱:{key}  數量:{value} 小計:{sum}元")
    else:
        print("購物車是空的")

def overObj(catalog,car):
    total_p = 0
    total_c = 0
    for key,value in car.items():
        sum = catalog[key]*value
        print(f"商品名稱:{key}  數量:{value} 小計:{sum}元")
        total_p += sum
        total_c += value
    print("************************************************")
    print(f"總計:{total_p}")
    if total_c >= 3:
        print(f"折扣資訊:滿三件打95折   共折扣{total_p*0.05} 共計{total_p*0.95}")
    else:
        print(f"折扣資訊:未滿三件無打折 共計{total_p}")

def clean():
    for i in range(100):
        print("=",end = "")
    print("")

if __name__ == "__main__":
   main()