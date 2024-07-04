import hashlib

def mask_pii(data):
    for record in data:
        if 'device_id' in record:
            record['masked_device_id'] = hashlib.sha256(record['device_id'].encode()).hexdigest()
        if 'ip' in record:
            record['masked_ip'] = hashlib.sha256(record['ip'].encode()).hexdigest()
    return data
