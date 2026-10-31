import csv
import random

# ข้อมูลตั้งต้นสำหรับสุ่ม
first_names = ["สมชาย", "วนิดา", "ณัฐพล", "สุจิตรา", "กฤษดา", "พรพิมล", "ศุภชัย", "อารียา", "ธนกร", "วิลาวัลย์", "นพดล", "สุดา", "ชัยวัฒน์", "รัตนา", "เอกพล"]
last_names = ["รักเรียน", "ใจดี", "มุ่งมั่น", "งามตา", "กล้าหาญ", "บุญมา", "แสงทอง", "ประเสริฐ", "สุขสวัสดิ์", "วิชาดี", "เจริญรุ่ง", "ยอดเยี่ยม", "มั่นคง"]

# สร้างรายชื่อโรงเรียน 60 แห่ง (เพชรบุรี 30, ประจวบฯ 30)
schools = []
for i in range(1, 31):
    schools.append({"province": "เพชรบุรี", "school_name": f"โรงเรียนประจำจังหวัดเพชรบุรี_{i}"})
for i in range(1, 31):
    schools.append({"province": "ประจวบคีรีขันธ์", "school_name": f"โรงเรียนมัธยมประจวบ_{i}"})

# สร้างข้อมูลนักเรียน 5,000 คน
students_data = []
for i in range(1, 6001):
    school_info = random.choice(schools)
    student = {
        "Student_ID": f"M2-{680000 + i}",
        "First_Name": random.choice(first_names),
        "Last_Name": random.choice(last_names),
        "Province": school_info["province"],
        "School_Name": school_info["school_name"],
        "EN_Score": random.randint(40, 100),
        "TH_Score": random.randint(50, 100),
        "MA_Score": random.randint(35, 100),
        "SC_Score": random.randint(40, 100)
    }
    students_data.append(student)

# บันทึกลงไฟล์ CSV
filename = "student_scores_m2.csv"
fields = ["Student_ID", "First_Name", "Last_Name", "Province", "School_Name", "EN_Score", "TH_Score", "MA_Score", "SC_Score"]

with open(filename, mode='w', encoding='utf-8-sig', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students_data)

print(f"สร้างไฟล์ {filename} จำนวน 5,000 รายการ สำเร็จเรียบร้อยแล้ว!")