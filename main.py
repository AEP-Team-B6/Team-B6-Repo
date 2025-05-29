import shutil
import os

hotel_reservation_sample_db = "./database/hotel_reservation_sample.db"
current_db = "./database/current_db.db"

shutil.copyfile(hotel_reservation_sample_db, current_db)

os.environ["DB_FILE"] = current_db

#TODO: Add more stuff