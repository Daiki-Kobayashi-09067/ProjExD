import tkinter as tk
import maze_maker as mm
from random import randint


def key_down(event):
    global key
    key=event.keysym
    print(f"{key}キーが押されました")

def key_up(event):
    global key
    key=""

def main_proc():
    global cx,cy,mx,my
    delta={"":[0,0],"Up":[0,-1],"Down":[0,+1],"Left":[-1,0],"Right":[+1,0]}
    #cx,cy=cx+delta[key][0],cy+delta[key][1]
    try:
        if  maze_bg[my+delta[key][1]][mx+delta[key][0]]==0:
            mx,my=mx+delta[key][0],my+delta[key][1]
            
    except:
        pass
    cx,cy=mx*100+50,my*100+50
    
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)


if __name__=="__main__":
    root=tk.Tk()
    root.title=("迷えるこうかとん")
    
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_bg=mm.make_maze(15,9) 
    mm.show_maze(canvas,maze_bg)


    tori=tk.PhotoImage(file="fig/3.png")
    teki = tk.PhotoImage(file = "fig/7.png")
    mx,my=1,1
    cx,cy=mx*100,my*100
    bx = randint(100,1400)*mx
    by = randint(0,800)*my
    a=bx+50
    b=by+50

    canvas.create_image(cx, cy, image = tori, tag = "tori")
    canvas.create_image(a, by, image = teki, tag = "teki")


    canvas.create_image(cx,cy,image=tori,tag="tori")
    canvas.create_image(bx,by,image=teki,tag="teki")
    
    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()

