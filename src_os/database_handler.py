import os
import openpyxl
from openpyxl.utils import get_column_letter

# Fail Excel (.xlsx wajib untuk fungsi auto-lebar)
EXCEL_FILE = 'hydration_log.xlsx'

def inisialisasi_excel():
    """Mencipta fail Excel baharu bersama tajuk kolum jika belum wujud"""
    if not os.path.exists(EXCEL_FILE):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Log Sistem OS-IoT"
        
        # Susunan tajuk kolum lengkap metrik OS
        headers = ["Tarikh & Masa", "Process ID", "Thread ID", "IP Address", "Quantity (Botol)", "Status"]
        ws.append(headers)
        wb.save(EXCEL_FILE)
        print(f"🎉 Fail {EXCEL_FILE} baharu berjaya dicipta!")

def simpan_ke_excel(data_list):
    """Menambah data ke Excel dan melakukan Auto-Fit pada kolum"""
    wb = openpyxl.load_workbook(EXCEL_FILE)
    ws = wb.active
    
    # Tambah baris data baharu
    ws.append(data_list)
    
    # LOGIK KEAJAIBAN: Mengira dan meluaskan kolum secara automatik (Auto-Fit)
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col.column)
        for cell in col:
            if cell.value:
                max_len = max(max_len, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = max(max_len + 4, 15)
        
    wb.save(EXCEL_FILE)
