
class Snake:
	def __init__(self):
		self.move_each_x=canv_width/2
		self.move_each_y = canv_height/2
		for x in range(0,7):
			c.create_oval(self.move_each_x,self.move_each_y,self.move_each_x+20,self.move_each_y+20, fill = "orange", tag = "snake")
			self.move_each_x += 20
			


	def MoveRight(self):
		time.sleep(60)
		for x in range(0,7):
				
				c.delete("snake")
				c.create_oval(self.move_each_x,self.move_each_y,self.move_each_x+20,self.move_each_y+20, fill = "orange", tag = "snake")
				self.move_each_x += 20
				

			
	def On_Move(self,e):
		Y = {87 : -10, 38 : -10, 40 : 10, 83 : 10}
		X = {37 : -10, 65 : -10, 39 : 10, 68 : 10}
		if e.keycode in Y:
			self.UpDown = Y[e.keycode]
			self.
		elif e.keycode in X:
			self.LeftRight = X[e.keycode]
			print (self.LeftRight)
			#print ("left or right")
		#print (coordY)
		#print (e.char, e.keycode)
		#print ("keysym=%s, keysym_num=%s" % (e.keysym, e.keysym_num))
		
		



 

def click(e):
        pass
    #    print (e.keycode)


import time
if __name__ == "__main__":
	from tkinter import *
	c = Canvas(width=460,height=460,bg='#cca1eb')
	c.pack()
	canv_width = 230 #достать значение ширины из канвы
	canv_height = 230#достать значение высоты из канвы

	snk = Snake()
	c.bind("<KeyPress>",snk.On_Move)
	snk.MoveRight()
	#c.bind("<KeyPress>",click)
	c.pack()
	c.focus_set()

	mainloop()
""""
oval = c.create_oval(30,10,130,80,fill="orange")
c.create_rectangle(180,10,280,80,tag="rect",fill="lightgreen")
trian = c.create_polygon(330,80,380,10,430,80,fill='white',outline="black")
 
def oval_func(event):
     c.delete(oval)
     c.create_text(30,10,text="Здесь был круг",anchor="w")
def rect_func(event):
     c.delete("rect")
     c.create_text(180,10,text="Здесь был\nпрямоугольник",anchor="nw")
def triangle(event):
     c.create_polygon(350,70,380,20,410,70,fill='yellow',outline="black")
 
c.tag_bind(oval,'<Button-1>',oval_func)
c.tag_bind("rect",'<Button-1>',rect_func)
c.tag_bind(trian,'<Button-1>',triangle)
 """
        
