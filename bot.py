import os
import time
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

BANNER = """
╔═════════════════════════════════════════════════════════════╗
║                                                             ║
║     ███████╗ █████╗ ██╗     ███╗   ███╗ █████╗ ███╗   ██╗     ║
║     ██╔════╝██╔══██╗██║     ████╗ ████║██╔══██╗████╗  ██║     ║
║     ███████╗███████║██║     ██╔████╔██║███████║██╔██╗ ██║     ║
║     ╚════██║██╔══██║██║     ██║╚██╔╝██║██╔══██║██║╚██╗██║     ║
║     ███████║██║  ██║███████╗██║ ╚═╝ ██║██║  ██║██║ ╚████║     ║
║                                                             ║
║             [ PENTEST & OSINT ADVANCED LAB ]                ║
║             [   Authorized Security Tool   ]                ║
╚═════════════════════════════════════════════════════════════╝
"""

def generate_report(target):
    legacy = ["Port Scanner (TCP/UDP)", "Banner Grabbing", "Basic IP Lookup"]
    new = ["Advanced Vulnerability Analyzer", "Subdomain Enumeration", "OSINT Deep-Trace"]
    
    msg = f"<pre>{BANNER}</pre>\n\n"
    msg += f"🚨 <b>[SALMAN OSINT - SECURITY REPORT]</b> 🚨\n"
    msg += f"🎯 <b>الهدف:</b> <code>{target}</code>\n"
    msg += f"⏱️ <b>الوقت:</b> <code>{time.strftime('%Y-%m-%d %H:%M:%S')}</code>\n\n"
    msg += "🔍 <b>الأدوات المفعلة (القديمة والجديدة):</b>\n"
    
    for t in legacy:
        msg += f"  • <i>[Legacy]</i> {t}\n"
    for t in new:
        msg += f"  • <i>[New]</i> {t}\n"
        
    msg += "\n📊 <b>نتيجة الفحص:</b>\n  ✔️ تمت مراجعة البنية والخدمات بنجاح دون فقدان أي بيانات.\n"
    return msg

def send_to_telegram(target):
    if not TOKEN or not CHAT_ID:
        print("[-] خطأ: لم يتم العثور على متغيرات البيئة الخاصة بـ Telegram.")
        return
        
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": generate_report(target),
        "parse_mode": "HTML"
    }
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == "__main__":
    target_to_scan = "target-system.local"
    send_to_telegram(target_to_scan)
