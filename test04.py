#รับค่า คือ หยุดให้ user ป้อนทางแป้นพิมพ์
#variable (ตัวแปร) = identifier คือ ชื่อที่ตั้งขึ้นมาเอง

#การแปลง ๖casting/type conversation) -> str( ) , int( ) , float( )
stu_id = input('ป้อน STUDENT ID:')
stuName = input('ป้อน STUDENT Name:')
stu_birth_year = input('ป้อน STUDENT Birth Year:') 
print("---------------------")
print(f"ยินดีต้อนรับ {stu_id} {stuName} สู๋ SAU")
print(f"คุณเกิดปี {stu_birth_year} แปลว่าคุณอายุ {2023 - int(stu_birth_year)} ปี")

print("ใช้ ,--------------------")
print("ยินดีต้อนรับ" ,stu_id,stuName,"สู๋ SAU")
print("คุณเกิดปี" ,stu_birth_year,"แปลว่าคุณอายุ",2023 - int(stu_birth_year), "ปี")

print("ใช้ +--------------------")
print("ยินดีต้อนรับ "+stu_id+" "+stuName+" สู๋ SAU")
print("คุณเกิดปี "+stu_birth_year+" แปลว่าคุณอายุ "+(2023 - int(stu_birth_year))+" ปี")

print("ใช้เมธอด format--------------------")
print("ยินดีต้อนรับ {} {} สู๋ SAU".format(stu_id,stuName))
print("คุณเกิดปี {} แปลว่าคุณอายุ {} ปี".format(stu_birth_year, 2023 - int(stu_birth_year)))

