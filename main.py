import psycopg2
from psycopg2 import sql

# ✅ DB 연결 설정
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "plainpaper",
    "user": "postgres",
    "password": "postgres"
}

# ✅ main 함수
def main():
    try:
        # 1️⃣ PostgreSQL 연결
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = True  # 자동 커밋 설정
        cur = conn.cursor()

        print("✅ PostgreSQL 연결 성공!")

        # 2️⃣ 간단한 테스트용 테이블 생성
        cur.execute("""
            CREATE TABLE IF NOT EXISTS test_member (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                email VARCHAR(100)
            );
        """)
        print("🧱 테이블 생성 완료 (test_member)")

        # 3️⃣ 데이터 삽입
        cur.execute("""
            INSERT INTO test_member (name, email)
            VALUES (%s, %s)
            RETURNING id;
        """, ("서동진", "test@example.com"))
        new_id = cur.fetchone()[0]
        print(f"📥 데이터 삽입 완료! 새 id = {new_id}")

        # 4️⃣ 데이터 조회
        cur.execute("SELECT * FROM test_member;")
        rows = cur.fetchall()
        print("\n📊 현재 test_member 데이터:")
        for row in rows:
            print(row)

        # 5️⃣ PostgreSQL 버전 확인
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        print(f"\n💡 PostgreSQL 버전: {version}")

    except Exception as e:
        print("❌ 오류 발생:", e)

    finally:
        if conn:
            cur.close()
            conn.close()
            print("🔚 연결 종료")

if __name__ == "__main__":
    main()