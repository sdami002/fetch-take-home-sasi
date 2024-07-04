import psycopg2

def load_to_db(data):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = conn.cursor()
    for record in data:
        cursor.execute("""
            INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            record['user_id'], record['device_type'], record['masked_ip'], record['masked_device_id'], 
            record['locale'], record['app_version'], record['create_date']
        ))
    conn.commit()
    cursor.close()
    conn.close()
