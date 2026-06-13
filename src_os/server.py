import threading
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Shared Resource (Tempat simpan data pelari)
data_pelari = []

# Membina MUTEX LOCK untuk konsep OS (Synchronization)
lock = threading.Lock()

@app.route('/api/funrun', methods=['POST'])
def terima_data_iot():
    data = request.get_json()
    
    if not data:
        return jsonify({"status": "Gagal", "mesej": "Tiada data"}), 400

    print(f"[THREAD {threading.get_ident()}] Menerima data: {data}")

    # Guna MUTEX LOCK (Synchronization)
    lock.acquire()
    try:
        data_pelari.append(data)
        
        # Simpan dalam bentuk fail teks (File Management)
        with open("log_pelari.txt", "a") as f:
            f.write(f"ID Pelari: {data.get('pelari_id')}, Masa: {time.time()}\n")
    finally:
        # Lepaskan lock
        lock.release()

    return jsonify({"status": "Sukses", "mesej": "Data selamat disimpan!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)