import os
import threading
from datetime import datetime
from flask import Flask, request, jsonify
from database_handler import inisialisasi_excel, simpan_ke_excel

app = Flask(name)

# Mutex Lock - Concurrency Control (Kunci Utama OS)
db_lock = threading.Lock()

@app.route('/api/funrun', methods=['POST'])
def receive_bottle_data():
    data = request.get_json()
    
    quantity = data.get('quantity')
    status_botol = data.get('status')
    
    waktu_sekarang = datetime.now().strftime('%d/%m/%Y %H:%M')
    thread_id = threading.current_thread().name
    process_id = os.getpid()
    ip_address = request.remote_addr

    # Mutex Lock - Mengelakkan Race Condition pada fail Excel
    with db_lock:
        try:
            data_to_log = [waktu_sekarang, process_id, thread_id, ip_address, quantity, status_botol]
            simpan_ke_excel(data_to_log)
            
            print(f"📡 [THREAD {thread_id}] Sukses merekod -> Qty: {quantity}")
            return jsonify({"message": "Data berjaya direkod", "status": "success"}), 200
            
        except Exception as e:
            print(f"❌ Ralat sistem fail: {str(e)}")
            return jsonify({"message": f"Gagal: {str(e)}", "status": "error"}), 500

if name == 'main':
    # Pastikan Excel sedia sebelum server bermula
    inisialisasi_excel()
    app.run(debug=True, host='0.0.0.0', port=5000)