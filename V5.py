print("This is the Island Support Bracket Tool")
print('>>>>>>>>>>>>>>>>>>>>>>>All Measurements are in Inches>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#print('All Measurements are in Inches')
cabinet_size = input("1.Enter the 'Depth' of the 'cabinet', (from front to back): ")
overhang_front_deep = input("2.How 'deep' is the 'front overhang'? ")
#overhang_front_wide = input("3.What length is the countertop (from left to right)? ")
#overhang_side_deep = input("4.What is the 'depth' of the 'side overhang'? ")
cabinet_side_wide = input ("3.What is the length of the cabinet, (from left to right)? ")
#overhang_left_or_right = input ("6.Is your side overhang on the 'Left ' or 'Right? ")
cab_color = input ("4.What color: B for Black and W for White ")
#x = input("Type a number: ")
#y = input("Type another number: ")

ib = int(cabinet_size) + int(overhang_front_deep) - 5
numbks = int(overhang_front_deep) // 24 
#ext = int(overhang_side_deep) + 5

# Basic if statement

if cabinet_size < overhang_front_deep:
    print("STOP!! The depth of the overhang is too deep: get a Custom Bracket design made. ")



#side = (overhang_left_or_right) 
cab = int(cabinet_size)
side_ext = int(cabinet_size) // 24 
#side_wide = int(cabinet_side_wide) // 22 
inside_wide = int(cabinet_side_wide) // 24 +1

    
print('The Order: ',inside_wide, '(IB-',cab_color,ib,') inch Island Brackets. This is for a' , cab, 'inch cabinte and a',overhang_front_deep,'inch overhang.')
#print('System Notes:' ,ib , 'inch IB with',side_wide , ext, 'inch' ,side ,' extensions.. Extends ',side ,cab, 'inch base cabinet.') 

#system notes: 33 inch ib with two 17 inch extensions.. Extends right. 24 inch base.

