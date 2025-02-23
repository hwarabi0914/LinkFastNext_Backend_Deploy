from sqlalchemy import create_engine, text  # ← text を追加
import os
from dotenv import load_dotenv
from pathlib import Path

# 環境変数の読み込み
load_dotenv()

# データベース接続情報
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', '3306')  # デフォルト3306を指定
DB_NAME = os.getenv('DB_NAME')

# SSL証明書のパスを指定
ssl_cert = r"C:\Users\hwara\Documents\LinkFastAPINext_practical\backend\db_control\DigiCertGlobalRootCA.crt.pem"

# MySQLのURL構築
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# エンジンの作成（SSL接続を有効化）
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl": {
            "ssl_ca": ssl_cert
        }
    },
    echo=True,
    pool_pre_ping=True,
    pool_recycle=3600
)

