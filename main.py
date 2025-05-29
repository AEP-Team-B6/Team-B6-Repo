import shutil
import os

hotel_reservation_sample_db = "./database/hotel_reservation_sample.db"
current_db = "./database/current_db.db"

shutil.copyfile(hotel_reservation_sample_db, current_db)

os.environ["DB_FILE"] = current_db

#TODO: Add more stuff


# Individuelle Testing -------------------

While False:
    # Testbereich (auf True sezten zum Testen)    









# Funktionierender Code------------------------
While True:
    #Funktionierende Userstories (auf False sezten zum Testen)
