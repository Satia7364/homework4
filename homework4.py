class Classes:
    def __init__(self, code, name, fraction, required, teacher, time):
        self.code = code
        self.name = name
        self.fraction = fraction
        self.required = required
        self.teacher = teacher
        self.time = time
s1 = Classes("5C12001", "遊戲設計", "3", "必修", "林芷澄", "周一：一、二、三")
s2 = Classes("5C12002", "晶片設計", "2", "選修", "張財生", "周三：四、五、六")
s3 = Classes("5C12003", "硬體設計", "3", "必修", "馮建祥", "周五：七、八、九")
print("課程代碼 : " + s1.code + " ,課程名稱 = " + s1.name + " ,學分數 = " + s1.fraction + " ,必修/選修 = " + s1.required + " ,教師 = " + s1.teacher + " ,課程時間 = " + s1.time)
print("課程代碼 : " + s2.code + " ,課程名稱 = " + s2.name + " ,學分數 = " + s2.fraction + " ,必修/選修 = " + s2.required + " ,教師 = " + s2.teacher + " ,課程時間 = " + s2.time)
print("課程代碼 : " + s3.code + " ,課程名稱 = " + s3.name + " ,學分數 = " + s3.fraction + " ,必修/選修 = " + s3.required + " ,教師 = " + s3.teacher + " ,課程時間 = " + s3.time)