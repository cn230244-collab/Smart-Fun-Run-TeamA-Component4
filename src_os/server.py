from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

# 🔒 MEMBINA MUTEX LOCK (Mekanisme OS untuk sekat Race Condition)
mutex_lock = threading.Lock()

# Nama fail log penyimpanan data
LOG_FILE = "log_pelari.txt"

@app.route('/api/funrun', methods=['POST'])
def receive_runner_data():
    data = request.json
    runner_id = data.get("runner_id")
    card_no = data.get("card_no")
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    # Rekod teks yang akan dimasukkan ke dalam fail
    log_entry = f"Pelari {runner_id} - Kad: {card_no} - Masa Scan: {timestamp}\n"

    # ==================== CRITICAL SECTION START ====================
    # Mengunci mutex. Jika thread lain tengah tulis fail, thread ini akan beratur tunggu di sini.
    mutex_lock.acquire()
    
    try:
        # Proses menulis ke dalam satu fail yang sama (Append mode 'a')
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
            # Simulasi proses penulisan mengambil sedikit masa di sebalik tab OS
            time.sleep(0.05) 
    finally:
        # Wajib lepaskan lock supaya pelari seterusnya dalam barisan boleh masuk
        mutex_lock.release()
    # ===================== CRITICAL SECTION END =====================

    return jsonify({
        "status": "Success",
        "message": f"Data Pelari {runner_id} selamat direkodkan oleh Mutex."
    }), 200

if __name__ == '__main__':
    # Server berjalan pada port 5000 dan bersedia menerima multi-thread serentak
    app.run(host='0.0.0.0', port=5000, threaded=True)