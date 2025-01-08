from app import app, db, User

def make_admin(student_number):
    with app.app_context():
        user = User.query.filter_by(student_number=student_number).first()
        if user:
            user.is_admin = True
            db.session.commit()
            print(f"{user.first_name} {user.last_name} artık admin yetkisine sahip!")
        else:
            print("Kullanıcı bulunamadı!")

if __name__ == "__main__":
    student_number = input("Admin yapmak istediğiniz kullanıcının öğrenci numarasını girin: ")
    make_admin(student_number) 