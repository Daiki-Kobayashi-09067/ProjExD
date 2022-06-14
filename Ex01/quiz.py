
import random

def main():
    seikai=shutudai()
    kaitou(seikai)

def shutudai():
    qes=[
        {"q":"サザエの旦那の名前は？","a":{"マスオ","ますお","タラオ"}},
        {"q":"カツオの妹の名前は？","a":{"ワカメ","わかめ"}},
        {"q":"タラオはカツオから見てどんな関係？","a":{"甥","おい","甥っ子","おいっこ"}},

    ]
    print("問題")
    r=random.randint(0,2)
    print(qes[r]["q"])
    return qes[r]["a"]

def kaitou(seikai):
    ans=input("答えるんだ")
    if ans in seikai:
        print("正解")
    else:
        print("出直してこい")


    
    
    



