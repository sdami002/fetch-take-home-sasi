from db_loader import load_to_db

def test_db_loader():
    sample_data = [
        {
            'user_id': '123',
            'device_type': 'mobile',
            'masked_ip': 'masked_ip_value',
            'masked_device_id': 'masked_device_id_value',
            'locale': 'en_US',
            'app_version': 1,
            'create_date': '2024-07-03'
        }
    ]
    load_to_db(sample_data)
    print("Data loaded to DB successfully.")

if __name__ == "__main__":
    test_db_loader()
