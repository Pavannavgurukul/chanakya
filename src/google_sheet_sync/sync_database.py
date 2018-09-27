from datetime import datetime
# from num
from .utils import get_worksheet
from .config import DATE_TIME_FORMAT
from chanakya.src import db, app
from chanakya.src.models import Student

class SyncChanakya:
    def __init__(self):
        self.worksheet = get_worksheet()
        self.data_frame = self.worksheet.get_as_df()
        self.update_from_sheet_to_chanakya()

    def update_from_sheet_to_chanakya(self):
        """
            Sync the data of student on Google Sheets to Chanakya.
        """
        # self.data_frame.replace(to_replace='', value=None,inplace=True)

        student_rows = [row[1] for row in self.data_frame.iterrows()]
        if student_rows:
            for student_row in student_rows:
                student_id = student_row['Student Id']
                student = Student.query.get(student_id)

                student.name = student_row['Name']

                if student_row['Date of Birth']:
                    student.dob = datetime.strptime(student_row['Date of Birth'], DATE_TIME_FORMAT)
                if student_row['Gender']:
                    student.gender = app.config['GENDER'](student_row['Gender'])
                if student_row['Caste']:
                    student.caste = app.config['CASTE'](student_row['Caste'])
                if student_row['Religion']:
                    student.religion = app.config['RELIGION'](student_row['Religion'])

                student.stage = student_row['Stage'] or None
                student.monthly_family_income = student_row['Monthly Family Income'] or None
                student.total_family_member = student_row['Total Family Member'] or None
                student.family_member_income_detail = student_row['Family Member Income Detail'] or None

                #something to add new contact or update old contact
                db.session.add(student)

            db.session.commit()
