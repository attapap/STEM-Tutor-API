import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

try:
    print("กำลังโหลดฐานข้อมูลคะแนน...")
    df_m1 = pd.read_csv('student_scores_m1.csv')
    df_m2 = pd.read_csv('student_scores_m2.csv')
    df_m3 = pd.read_csv('student_scores_m3.csv')
    
    all_students_df = pd.concat([df_m1, df_m2, df_m3], ignore_index=True)
    print(f"โหลดข้อมูลสำเร็จ! จำนวนนักเรียนทั้งหมด {len(all_students_df)} คน")
except Exception as e:
    print(f"เกิดข้อผิดพลาดในการโหลดไฟล์ CSV: {e}")
    all_students_df = pd.DataFrame()

@app.route('/api/get-score/<student_id>', methods=['GET'])
def get_student_score(student_id):
    try:
        mclass = student_id.split('-')[0] if '-' in student_id else 'Unknown'

        if all_students_df.empty:
            return jsonify({"error": "Database is empty"}), 500

        student_data = all_students_df[all_students_df['Student_ID'] == student_id]
        
        if not student_data.empty:
            row = student_data.iloc[0]
            return jsonify({
                "status": "found",
                "mclass": mclass,
                "std_id": str(row['Student_ID']),
		"name": f"{row['First_Name']} {row['Last_Name']}",
                "school": str(row['School_Name']),
                "EN": int(row['EN_Score']),
                "TH": int(row['TH_Score']),
                "MA": int(row['MA_Score']),
                "SC": int(row['SC_Score'])
            })
        else:
            return jsonify({"status": "not_found"}), 404
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # รันบน host 0.0.0.0 และพอร์ต 5050
    app.run(host='0.0.0.0', port=5050)
