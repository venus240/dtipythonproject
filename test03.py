#แสดงข้อมูลหลายๆประเภท ในprint เดียว

#1. ใช้, โดยจะมี space ในแต่ละ,
print("SAU",555,123.456,True,10+50)

#2. ใฃ้ + มีข้อแม้ ข้อมูล,ที่ไม่ใช่ string ต้องแปลงเป็น string และไม่มี space ให้เหมือน ,
print("SAU "+str(555)+' '+str(123.456)+' '+str(True)+' '+str(10+50))

#3. ใช้เมธอดฃื่อ format
print("SAU {} {} {} {}".format(555, 123.456, True, 10+50))
print("SAU {0} {1} {2} {3}".format(555, 123.456, True, 10+50))

#4. ใช้ f-string ***
print(f'SAU {555} {123.456} {True} {10+50}')

#------------------------
#หรณี 1 บรรทัดมีหลาย statment ให้คั่นด้วย ; (stament=คำสั่ง3)
print('aaa'); print(111); print(False)
