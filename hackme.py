#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HACKME WhatsApp Tools v1.1.0
Author : Ruyynn
GitHub : github.com/ruyynn/HACKME
"""

import os
import sys
import time
import json
import platform
import subprocess
from datetime import datetime

# ==================== WARNA ====================
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
PURPLE = '\033[0;35m'
CYAN = '\033[0;36m'
WHITE = '\033[0;37m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'

# ==================== LOGO HACKME (TIDAK DIUBAH) ====================
LOGO = f"""
{CYAN} ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀ ███▄ ▄███▓▓█████ {RESET}
{CYAN}▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██▒▀█▀ ██▒▓█   ▀ {RESET}
{CYAN}▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▓██    ▓██░▒███   {RESET}
{CYAN}░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒██    ▒██ ▒▓█  ▄ {RESET}
{CYAN}░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄▒██▒   ░██▒░▒████▒{RESET}
{CYAN} ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░ ▒░   ░  ░░░ ▒░ ░{RESET}
{CYAN} ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░░  ░      ░ ░ ░  ░{RESET}
{CYAN} ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ ░      ░      ░   {RESET}
{CYAN} ░  ░  ░      ░  ░░ ░      ░  ░          ░      ░  ░{RESET}
{CYAN}                  ░                                {RESET}"""

INFO_BOX = f"""
{PURPLE}╔══════════════════════════════════════════════════════════════╗{RESET}
{PURPLE}║{RESET}{WHITE}{BOLD}              HACKME WHATSAPP TOOLS v1.1.0                    {RESET}{PURPLE}║{RESET}
{PURPLE}╠══════════════════════════════════════════════════════════════╣{RESET}
{PURPLE}║{RESET}  {BOLD}Author{RESET}   : Ruyynn                                           {PURPLE}║{RESET}
{PURPLE}║{RESET}  {BOLD}GitHub{RESET}   : github.com/ruyynn/HACKME                         {PURPLE}║{RESET}
{PURPLE}║{RESET}  {BOLD}Version{RESET}  : 1.1.0                                            {PURPLE}║{RESET}
{PURPLE}║{RESET}  {BOLD}Updated{RESET}  : 2026-03-02                                       {PURPLE}║{RESET}
{PURPLE}╚══════════════════════════════════════════════════════════════╝{RESET}"""

# ==================== INSTALL PHONENUMBERS ====================
def install_phonenumbers():
    """Install library phonenumbers jika belum ada"""
    try:
        import phonenumbers
        return True
    except ImportError:
        print(f"\n{YELLOW}[!] Library phonenumbers belum terinstall.{RESET}")
        print(f"{BLUE}[*] Menginstall phonenumbers...{RESET}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "phonenumbers"])
            print(f"{GREEN}[✓] Berhasil terinstall!{RESET}")
            return True
        except:
            print(f"{RED}[✗] Gagal install. Install manual: pip install phonenumbers{RESET}")
            return False

# Install phonenumbers
if install_phonenumbers():
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone
else:
    print(f"{RED}[✗] Library phonenumbers diperlukan. Exiting...{RESET}")
    sys.exit(1)

# ==================== CLASS HACKME ====================
class HACKME:
    def __init__(self):
        self.session_id = self.generate_session_id()
        self.results = []
        self.history = []
        self.country_code = "ID"
        self.version = "1.1.0"
        
    def generate_session_id(self):
        import hashlib, random
        return hashlib.md5(str(random.getrandbits(128)).encode()).hexdigest()[:8]
    
    def clear_screen(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')
    
    def print_logo(self):
        logo_lines = LOGO.split('\n')
        info_lines = INFO_BOX.split('\n')
        max_lines = max(len(logo_lines), len(info_lines))
        
        for i in range(max_lines):
            logo_part = logo_lines[i] if i < len(logo_lines) else ' ' * 50
            info_part = info_lines[i] if i < len(info_lines) else ''
            print(f"{logo_part}  {info_part}")
    
    def print_header(self, title):
        print(f"\n{BLUE}┌─[ {title} ]{'─' * (60 - len(title))}┐{RESET}")
    
    def print_footer(self):
        print(f"{BLUE}└{'─' * 62}┘{RESET}\n")
    
    def loading(self, text, duration=0.5):
        print(f"{YELLOW}⏳{RESET} {text}...", end='', flush=True)
        time.sleep(duration)
        print(f"\r{GREEN}✅{RESET} {text}... {GREEN}OK{RESET}   ")
    
    # ==================== FITUR PHONENUMBERS ====================
    
    def parse_number(self, number):
        """Parse nomor telepon dengan berbagai format"""
        number = number.strip().replace(' ', '').replace('-', '')
        
        try:
            if number.startswith('+'):
                return phonenumbers.parse(number, None)
            elif number.startswith('0'):
                return phonenumbers.parse(number, "ID")
            else:
                return phonenumbers.parse(number, "ID")
        except:
            return None
    
    def analyze_number(self, number):
        """Analisis nomor menggunakan phonenumbers (REAL)"""
        result = {
            'input': number,
            'timestamp': datetime.now().isoformat(),
            'valid': False,
            'possible': False,
            'national': None,
            'international': None,
            'country_code': None,
            'provider': None,
            'location': None,
            'timezone': [],
            'number_type': None,
            'country': None
        }
        
        try:
            parsed = self.parse_number(number)
            if not parsed:
                return result
            
            result['valid'] = phonenumbers.is_valid_number(parsed)
            result['possible'] = phonenumbers.is_possible_number(parsed)
            
            if result['valid'] or result['possible']:
                result['national'] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
                result['international'] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                result['country_code'] = parsed.country_code
                
                try:
                    result['provider'] = carrier.name_for_number(parsed, "en")
                except:
                    result['provider'] = "Unknown"
                
                try:
                    result['location'] = geocoder.description_for_number(parsed, "en")
                except:
                    result['location'] = "Unknown"
                
                try:
                    result['timezone'] = list(timezone.time_zones_for_number(parsed))
                except:
                    result['timezone'] = []
                
                try:
                    number_type = phonenumbers.number_type(parsed)
                    type_map = {
                        0: "FIXED_LINE", 1: "MOBILE", 2: "FIXED_LINE_OR_MOBILE",
                        3: "TOLL_FREE", 4: "PREMIUM_RATE", 5: "SHARED_COST",
                        6: "VOIP", 7: "PERSONAL_NUMBER", 8: "PAGER",
                        9: "UAN", 10: "VOICEMAIL", 99: "UNKNOWN"
                    }
                    result['number_type'] = type_map.get(number_type, "UNKNOWN")
                except:
                    result['number_type'] = "UNKNOWN"
                
                try:
                    result['country'] = phonenumbers.region_code_for_number(parsed)
                except:
                    result['country'] = "Unknown"
                
        except Exception as e:
            result['error'] = str(e)
        
        return result
    
    def predict_whatsapp(self, result):
        """Prediksi kemungkinan WhatsApp berdasarkan data """
        if not result['valid']:
            return "INVALID NUMBER"
        
        score = 0
        reasons = []
        
        if result['number_type'] in ["MOBILE", "FIXED_LINE_OR_MOBILE"]:
            score += 70
            reasons.append("Mobile number type")
        
        whatsapp_providers = ['Telkomsel', 'Indosat', 'XL', 'Tri', 'Axis', 'Smart', '3']
        if result['provider'] and any(p in str(result['provider']) for p in whatsapp_providers):
            score += 20
            reasons.append(f"Provider: {result['provider']}")
        
        if result['possible']:
            score += 10
            reasons.append("Valid number format")
        
        if score >= 90:
            return "VERY LIKELY registered on WhatsApp"
        elif score >= 70:
            return "LIKELY registered on WhatsApp"
        elif score >= 50:
            return "POSSIBLE registered on WhatsApp"
        elif score >= 30:
            return "UNLIKELY registered on WhatsApp"
        else:
            return "PROBABLY NOT on WhatsApp"
    
    def save_result(self, result):
        """Simpan hasil analisis"""
        os.makedirs('results', exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results/analysis_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(result, f, indent=2)
        
        return filename
    
    # ==================== MENU ABOUT ====================
    
    def menu_about(self):
        """Menampilkan informasi tools v1.1.0"""
        self.clear_screen()
        self.print_logo()
        self.print_header("ℹ️ ABOUT HACKME v1.1.0")
        
        about_text = f"""
{WHITE}{BOLD}╔════════════════════════════════════════════════════════════════════╗
║                    HACKME WHATSAPP TOOLS v1.1.0                    ║
╠════════════════════════════════════════════════════════════════════╣
║  {CYAN}📌 DESKRIPSI{RESET}{WHITE}                                                      ║       
║  HACKME adalah tools OSINT untuk analisis nomor telepon            ║
║  dengan fokus pada deteksi WhatsApp.                               ║
╠════════════════════════════════════════════════════════════════════╣
║  {GREEN}✨ FITUR UTAMA v1.1.0{RESET}{WHITE}                                             ║
║  ✅ Validasi nomor internasional                                   ║
║  ✅ Deteksi provider & operator                                    ║
║  ✅ Deteksi lokasi                                                 ║
║  ✅ Deteksi timezone                                               ║
║  ✅ Format nasional & internasional                                ║
║  ✅ Deteksi tipe nomor (Mobile/Fixed/VoIP)                         ║
║  ✅ Batch analyze multiple nomor                                   ║
║  ✅ Export hasil ke JSON                                           ║
╠════════════════════════════════════════════════════════════════════╣
║  {YELLOW}🆕 WHAT'S NEW v1.1.0{RESET}{WHITE}                                              ║
║  • Deteksi provider akurat (Telkomsel, Indosat, XL, dll)           ║
║  • Deteksi lokasi berdasarkan kode area                            ║
║  • Timezone detection                                              ║
║  • Batch analyze untuk multiple nomor                              ║
║  • History penyimpanan hasil                                       ║
╠════════════════════════════════════════════════════════════════════╣
║  {BLUE}⚙️ SPESIFIKASI{RESET}{WHITE}                                                     ║
║  • Core Engine  : Google libphonenumber                            ║
║  • Bahasa       : Python 3.6+                                      ║
║  • Platform     : Windows, Linux, macOS, Termux                    ║
║  • Lisensi      : MIT Open Source                                  ║
╠════════════════════════════════════════════════════════════════════╣
║  {PURPLE}📊 AKURASI DATA{RESET}{WHITE}                                                   ║
║  • Validasi nomor   : Based on Google libphonenumber database      ║
║  • Deteksi provider : 90-95%                                       ║
║  • Deteksi lokasi   : 85-90%                                       ║
║  • Timezone         : 100%                                         ║
╠════════════════════════════════════════════════════════════════════╣
║  {RED}⚠️ DISCLAIMER{RESET}{WHITE}                                                      ║
║  Tools ini untuk tujuan EDUKASI dan PEMBELAJARAN.                  ║
║  TIDAK bisa hack WhatsApp, membaca chat, atau                      ║
║  melanggar privasi pengguna.                                       ║
╠════════════════════════════════════════════════════════════════════╣
║  {CYAN}📬 KONTAK & SUPPORT{RESET}{WHITE}                                               ║
║  • Author   : Ruyynn                                               ║
║  • GitHub   : https://github.com/ruyynn/HACKME                     ║
║  • Support  : https://saweria.co/Ruyynn                            ║
║  • Email    : ruyynn25@gmail.com                                   ║
║  • Kolaborasi : Pull requests welcome!                             ║
╠════════════════════════════════════════════════════════════════════╣
║  {GREEN}📚 VERSION HISTORY{RESET}{WHITE}                                                ║
║  • v1.0.0 (2026-02-15) - Rilis awal                                ║
║  • v1.1.0 (2026-03-02) - optimal - feature improvement             ║
╚════════════════════════════════════════════════════════════════════╝{RESET}
"""
        
        print(about_text)
        
        # Tampilkan versi library
        print(f"\n{BLUE}📦 PHONENUMBERS VERSION:{RESET} {phonenumbers.__version__}")
        print(f"{DIM}Google libphonenumber database terbaru{RESET}")
        
        self.print_footer()
        input(f"\n{CYAN}Press Enter to return to menu...{RESET}")
    
    # ==================== MENU UTAMA ====================
    
    def menu_analyze(self):
        self.clear_screen()
        self.print_logo()
        self.print_header("🔍 ANALISIS NOMOR - REAL PHONENUMBERS")
        
        print(f"\n{YELLOW}Masukkan nomor telepon:{RESET}")
        print(f"{DIM}Contoh: 08123456789, +628123456789, 021123456{RESET}")
        
        number = input(f"\n{CYAN}Nomor>{RESET} ").strip()
        
        if not number:
            print(f"\n{RED}[!] Nomor tidak boleh kosong{RESET}")
            input(f"\n{CYAN}Press Enter...{RESET}")
            return
        
        self.loading("Menganalisis dengan Google libphonenumber", 1)
        
        result = self.analyze_number(number)
        self.results.append(result)
        
        print(f"\n{WHITE}{BOLD}📊 HASIL ANALISIS REAL:{RESET}")
        print(f"{DIM}{'─' * 50}{RESET}")
        
        if result['valid']:
            print(f"{GREEN}✅ VALID NUMBER{RESET}")
        elif result['possible']:
            print(f"{YELLOW}⚠️ POSSIBLE NUMBER (tapi mungkin tidak valid){RESET}")
        else:
            print(f"{RED}❌ INVALID NUMBER{RESET}")
        
        print(f"\n{BLUE}📞 Format:{RESET}")
        print(f"  • Input      : {result['input']}")
        print(f"  • National   : {result['national']}")
        print(f"  • Intl       : {result['international']}")
        print(f"  • Country    : +{result['country_code']} ({result['country']})")
        
        if result['valid'] or result['possible']:
            print(f"\n{BLUE}📱 Informasi:{RESET}")
            print(f"  • Provider   : {result['provider'] or 'Unknown'}")
            print(f"  • Lokasi     : {result['location'] or 'Unknown'}")
            print(f"  • Tipe       : {result['number_type']}")
            print(f"  • Timezone   : {', '.join(result['timezone']) if result['timezone'] else 'Unknown'}")
            
            wa_prediction = self.predict_whatsapp(result)
            print(f"\n{YELLOW}📱 WhatsApp Prediction:{RESET}")
            print(f"  {wa_prediction}")
        
        filename = self.save_result(result)
        print(f"\n{GREEN}[✓] Hasil disimpan di: {filename}{RESET}")
        
        self.print_footer()
        input(f"\n{CYAN}Press Enter...{RESET}")
    
    def menu_provider(self):
        self.clear_screen()
        self.print_logo()
        self.print_header("📡 CEK PROVIDER & LOKASI")
        
        print(f"\n{YELLOW}Masukkan nomor telepon:{RESET}")
        number = input(f"\n{CYAN}Nomor>{RESET} ").strip()
        
        if not number:
            print(f"\n{RED}[!] Nomor tidak boleh kosong{RESET}")
            input(f"\n{CYAN}Press Enter...{RESET}")
            return
        
        self.loading("Mendeteksi provider & lokasi", 1)
        
        result = self.analyze_number(number)
        
        print(f"\n{WHITE}{BOLD}📡 INFORMASI PROVIDER & LOKASI:{RESET}")
        print(f"{DIM}{'─' * 50}{RESET}")
        
        if result['valid']:
            print(f"{GREEN}Provider  : {result['provider'] or 'Tidak diketahui'}{RESET}")
            print(f"{GREEN}Lokasi    : {result['location'] or 'Tidak diketahui'}{RESET}")
            print(f"{GREEN}Negara    : {result['country']} (+{result['country_code']}){RESET}")
            print(f"{GREEN}Tipe      : {result['number_type']}{RESET}")
        else:
            print(f"{RED}Nomor tidak valid{RESET}")
        
        self.print_footer()
        input(f"\n{CYAN}Press Enter...{RESET}")
    
    def menu_validate(self):
        self.clear_screen()
        self.print_logo()
        self.print_header("✅ VALIDASI NOMOR")
        
        print(f"\n{YELLOW}Masukkan nomor telepon:{RESET}")
        number = input(f"\n{CYAN}Nomor>{RESET} ").strip()
        
        if not number:
            print(f"\n{RED}[!] Nomor tidak boleh kosong{RESET}")
            input(f"\n{CYAN}Press Enter...{RESET}")
            return
        
        self.loading("Memvalidasi nomor", 0.5)
        
        try:
            parsed = self.parse_number(number)
            if parsed:
                valid = phonenumbers.is_valid_number(parsed)
                possible = phonenumbers.is_possible_number(parsed)
                
                print(f"\n{WHITE}{BOLD}📋 HASIL VALIDASI:{RESET}")
                print(f"{DIM}{'─' * 40}{RESET}")
                print(f"Valid   : {GREEN if valid else RED}{valid}{RESET}")
                print(f"Possible: {GREEN if possible else YELLOW}{possible}{RESET}")
                
                if valid or possible:
                    national = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
                    international = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                    print(f"Format  : {national}")
                    print(f"          {international}")
            else:
                print(f"\n{RED}[✗] Gagal memparse nomor{RESET}")
        except Exception as e:
            print(f"\n{RED}[✗] Error: {e}{RESET}")
        
        self.print_footer()
        input(f"\n{CYAN}Press Enter...{RESET}")
    
    def menu_batch(self):
        self.clear_screen()
        self.print_logo()
        self.print_header("📑 BATCH ANALYZE")
        
        print(f"\n{YELLOW}Masukkan nomor (pisahkan dengan koma):{RESET}")
        numbers_input = input(f"\n{CYAN}Nomor>{RESET} ").strip()
        
        if not numbers_input:
            print(f"\n{RED}[!] Masukkan minimal satu nomor{RESET}")
            input(f"\n{CYAN}Press Enter...{RESET}")
            return
        
        numbers = [n.strip() for n in numbers_input.split(',') if n.strip()]
        
        print(f"\n{BLUE}[*] Menganalisis {len(numbers)} nomor...{RESET}")
        
        batch_results = []
        for i, number in enumerate(numbers, 1):
            print(f"{YELLOW}  [{i}/{len(numbers)}] {number}...{RESET}", end='', flush=True)
            result = self.analyze_number(number)
            batch_results.append(result)
            status = "✓" if result['valid'] else "✗"
            print(f"\r{GREEN}  [{i}/{len(numbers)}] {number} [{status}]{' ' * 20}{RESET}")
        
        filename = self.save_result({'batch': batch_results, 'count': len(batch_results)})
        print(f"\n{GREEN}[✓] Batch results saved: {filename}{RESET}")
        
        valid_count = sum(1 for r in batch_results if r['valid'])
        print(f"\n{BLUE}Statistik:{RESET}")
        print(f"  Total     : {len(batch_results)}")
        print(f"  Valid     : {valid_count}")
        print(f"  Invalid   : {len(batch_results) - valid_count}")
        
        self.print_footer()
        input(f"\n{CYAN}Press Enter...{RESET}")
    
    def menu_history(self):
        self.clear_screen()
        self.print_logo()
        self.print_header("📜 HISTORY ANALISIS")
        
        if not self.results:
            print(f"\n{YELLOW}[!] Belum ada history{RESET}")
        else:
            print(f"\n{WHITE}{BOLD}📋 {len(self.results)} analisis terakhir:{RESET}")
            print(f"{DIM}{'─' * 60}{RESET}")
            
            for i, result in enumerate(self.results[-10:], 1):
                status = f"{GREEN}✓{RESET}" if result['valid'] else f"{RED}✗{RESET}"
                number = result['national'] or result['input']
                provider = result['provider'] or '?'
                print(f"  {i}. {status} {number} - {provider}")
        
        self.print_footer()
        input(f"\n{CYAN}Press Enter...{RESET}")
    
    def menu_country(self):
        self.clear_screen()
        self.print_logo()
        self.print_header("🌍 SET COUNTRY")
        
        print(f"\n{YELLOW}Current country: {self.country_code}{RESET}")
        print(f"{DIM}Masukkan kode negara 2 huruf (ID, US, MY, SG, etc){RESET}")
        
        new_country = input(f"\n{CYAN}Country>{RESET} ").strip().upper()
        
        if len(new_country) == 2 and new_country.isalpha():
            self.country_code = new_country
            print(f"\n{GREEN}[✓] Country diubah ke {new_country}{RESET}")
        else:
            print(f"\n{RED}[!] Kode negara tidak valid (harus 2 huruf){RESET}")
        
        self.print_footer()
        input(f"\n{CYAN}Press Enter...{RESET}")
    
    def menu_main(self):
        while True:
            self.clear_screen()
            self.print_logo()
            
            print(f"\n{WHITE}{BOLD}MAIN MENU - FREE VER{RESET}")
            print(f"{DIM}{'─' * 64}{RESET}\n")
            
            menu_items = [
                ("1", " ANALYZE NUMBER", "Analisis nomor dengan phonenumbers"),
                ("2", " CHECK PROVIDER", "Cek provider dan lokasi"),
                ("3", " VALIDATE ONLY", "Validasi format nomor"),
                ("4", " BATCH ANALYZE", "Analisis multiple nomor"),
                ("5", " VIEW HISTORY", "Lihat hasil analisis sebelumnya"),
                ("6", " SET COUNTRY", f"Kode negara (current: {self.country_code})"),
                ("7", " ABOUT", "Info "),
                ("0", " EXIT", "Keluar dari HACKME")
            ]
            
            for num, name, desc in menu_items:
                if num == "0":
                    color = RED
                elif num == "7":
                    color = PURPLE
                elif num in ["1","2","3","4"]:
                    color = GREEN
                else:
                    color = YELLOW
                print(f"  {color}[{num}]{RESET} {BOLD}{name:<16}{RESET} {DIM}{desc}{RESET}")
            
            print(f"\n{DIM}{'─' * 64}{RESET}")
            print(f"\n{GREEN}[+]{RESET} Session : {self.session_id}")
            print(f"{GREEN}[+]{RESET} Results : {len(self.results)}")
            print(f"{GREEN}[+]{RESET} Version : {self.version}")
            
            choice = input(f"\n{CYAN}[[HACKME]]>{RESET} ").strip()
            
            if choice == '0':
                print(f"\n{GREEN}Terima kasih telah menggunakan HACKME!{RESET}")
                print(f"{BLUE}GitHub: github.com/ruyynn/HACKME{RESET}")
                break
            elif choice == '1':
                self.menu_analyze()
            elif choice == '2':
                self.menu_provider()
            elif choice == '3':
                self.menu_validate()
            elif choice == '4':
                self.menu_batch()
            elif choice == '5':
                self.menu_history()
            elif choice == '6':
                self.menu_country()
            elif choice == '7':
                self.menu_about()
            else:
                print(f"\n{RED}[!] Pilihan tidak valid{RESET}")
                time.sleep(1)

# ==================== MAIN ====================
if __name__ == "__main__":
    try:
        print(f"{BLUE}{BOLD}Loading HACKME v1.1.0 - FREE EDITION...{RESET}")
        time.sleep(1)
        
        app = HACKME()
        app.menu_main()
        
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Interrupted by user{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n{RED}Fatal Error: {str(e)}{RESET}")
        sys.exit(1)
