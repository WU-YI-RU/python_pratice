try:
    n = int(input("請輸入基數:"))
    fs = (n+1)/2 -1
    fe = (n+1)/2 -1
    for i in range(n//2+1):

        for j in range(n):
            if j <= fe and j >= fs:
                print("*",end = "")
            else:
                print(" ",end = "")
        print("")
        fe += 1
        fs -= 1
except ValueError as e:
    print("錯誤訊息為:",e,"通常不能顯示這個，會有資安問題")
    print(type(e).__name__,"請藏起來，不然紅藍隊演練你會爆炸")
else:
    print("成功了")
finally:
    print("紀錄已生成")