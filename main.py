import shutil

working_db = "./database/working_db.db"
current_db = "./database/current_db.db"

shutil.copyfile(working_db, current_db)

os.environ["DB_FILE"] = current_db

#TODO: Add more stuff