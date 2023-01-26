import hashlib

# blok verileri
block_data = "Merhaba, bu bir blok içeriğidir"

# blok verilerinin hash değeri
block_hash = hashlib.sha256(block_data.encode()).hexdigest()

# blok numarası
block_number = 1

# önceki blok hash değeri
previous_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"

# nonce değeri
nonce = 0

while True:
    # blok verilerini, blok numarasını, önceki blok hash değerini ve nonce değerini birleştiriyoruz
    data_to_hash = block_data + str(block_number) + previous_block_hash + str(nonce)
    
    # hash değerini hesaplıyoruz
    new_hash = hashlib.sha256(data_to_hash.encode()).hexdigest()
    
    # hash değerinin ilk 4 hanesinin 0 olmasını istiyoruz
    if new_hash[:4] == "0000":
        block_hash = new_hash
        break
    
    # eğer koşul sağlanmadıysa nonce değerini arttırıyoruz
    nonce += 1

print("Blok Hash Değeri:", block_hash)
