import random
import datetime

trials=5 #最大の繰り返し回数
allchars=10 #対象文字数
abschars=2 #欠損文字数

def main():
    st=datetime.datetime.now()
    for _ in range(trials):
        seikai=shutudai()
        f=kaitou(seikai)
        if f==1:
            break
    ed=datetime.datetime.now()
    


def shutudai():
    #全アルファベット文字のリスト
    alphabets=[chr(c+65) for c in range(26)] #chr(コード)文字
    allchars_list=random.sample(alphabets,allchars)
    print(f"対象文字:{allchars_list}")

#対象文字からabschars個の文字をランダムに選ぶ：欠損文字
abschar_list=random.sample(XXXX,YYYY)
print(f"欠損文字：{abschar_list}") 
#対象文字から欠損文字を除いたものを表示する：表示文字
prechar_list=[ZZZZ]
print(f"表示文字：{prechar_list}")
 

def kaitou(seikai):
    num=int(input("欠損文字はいくつあるでしょうか？"))
    if num !=abschars:
        print("不正解です")
        return 0
    else:
        print("正解です。それでは具体的意欠損文字をひとつずつ入力してください")
        for i in range(abschars):
            c=input(f"{i+1}つ目の文字を入力してください")
            if c not in seikai :
                print("不正解です。またチャレンジしてください")
                return 0
            seikai.remove(c)
        print("正解です。ゲームを終了します")
        return 1
            
               


if __name__ =="__main__":
    main()




