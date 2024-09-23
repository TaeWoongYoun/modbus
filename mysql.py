import pymysql 

conn = pymysql.connect(host='localhost', user='root', password='1234', db='developer', charset='utf8') 
cursor = conn.cursor() 

# sql = "CREATE table test(idx INT PRIMARY KEY AUTO_INCREMENT, id VARCHAR(255), name VARCHAR(255))"
# sql = "INSERT INTO test (id, name) VALUES ('xodnd', '윤태웅')" 
sql = "SELECT * FROM test"

cursor.execute(sql) 

# 조회된 결과 가져오기
rows = cursor.fetchall()

# 결과 출력
for row in rows:
    print(row)

# 연결 종료
conn.close()