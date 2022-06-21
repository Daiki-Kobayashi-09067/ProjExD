import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn=event.widget
    num=btn["text"]
    if num =="=":
        eqn=entry.get()
        res=eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
        entry.insert(tk.END,num)

    if num=="C":
        entry.delete(0,tk.END)
    

    #if num=="^":
    #    eqn=entry.get()
    #    ans=eval(eqn)*eval(eqn)*eval(eqn)
     #   entry.delete(0,tk.END)
     #   entry.insert(tk.END,ans)
    



    
    #elif num=="X":
       # eqn=entry.get()
       # res=eval(eqn)


    
        




    #tkm.showinfo("",f"{num}のボタンが押されました")
   # entry.insert(tk.END,num)

if __name__ == "__main__":

    root=tk.Tk()
    root.title("練習")
    root.geometry("250x650")

    

    r,c=1,0

    entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman",00))
    entry.grid(row=0,column=0,columnspan=3)

    for i,num in enumerate([9,8,7,6,5,4,3,2,1,0,"+","-","/","%","*","**","=","C"]):
        btn=tk.Button(root,text=f"{num}",width=4,height=2,font=("Times New Roman",25))
        btn.bind("<1>",button_click)
        btn.grid(row=r,column=c)
        c+=1
        if(i-2)%3==0:
            r+=1
            c=0
            btn.bind("<1>",button_click)


        


    root.mainloop()




