import sys
from pathlib import Path

# backendフォルダをモジュールパスに追加
sys.path.append(str(Path(__file__).resolve().parents[1]))


#from db_control.mymodels import Base
#from db_control.connect import engine
from db_control.mymodels_MySQL import Base
from db_control.connect_MySQL import engine

from sqlalchemy import inspect


def init_db():
    # インスペクターを作成
    inspector = inspect(engine)

    # 既存のテーブルを取得
    existing_tables = inspector.get_table_names()

    print("Checking tables...")

    # customersテーブルが存在しない場合は作成
    if 'customers' not in existing_tables:
        print("Creating 'customers' table on Azure MySQL...")
        try:
            Base.metadata.create_all(bind=engine)
            print("Tables created successfully on Azure!!")
        except Exception as e:
            print(f"Error creating tables on Azure!: {e}")
            raise
    else:
        print("Tables already exist.")
        

if __name__ == "__main__":
    init_db()
