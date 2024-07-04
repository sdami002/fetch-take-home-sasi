from data_transformer import mask_pii

def test_data_transformer():
    sample_data = [
        {
            'user_id': '123',
            'device_id': 'device123',
            'ip': '192.168.1.1',
            'device_type': 'mobile',
            'locale': 'en_US',
            'app_version': 1,
            'create_date': '2024-07-03'
        }
    ]
    masked_data = mask_pii(sample_data)
    for record in masked_data:
        print(record)

if __name__ == "__main__":
    test_data_transformer()
