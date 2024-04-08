"""
@Author: <mao>
@CreateTime: 2024/04/28
"""
import csv

from sqlalchemy import create_engine, text

if __name__ == '__main__':
    with open('四六级单词.csv', 'rt', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        engine = create_engine('mysql+pymysql://root:000000@192.168.60.128:3306/english_learner')

        # 将数据导入数据库
        with engine.connect() as conn:
            for row in reader:
                word = row[0]
                cn = row[1]
                print(word, cn)
                insert_query = text("INSERT INTO word (word, cn) VALUES (:word, :cn)")
                conn.execute(insert_query, {'word': word, 'cn': cn})
            conn.commit()
