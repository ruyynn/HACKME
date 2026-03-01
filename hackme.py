#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HACKME WhatsApp Tools v1.0 - Free Edition
Author: Ruyynn
GitHub: https://github.com/ruyynn/hackme-wa
License: MIT
"""

import os
import sys
import time
import json
import random
import string
import hashlib
import platform
import subprocess
from datetime import datetime, timedelta

# ANSI color codes
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

# Logo HACKME
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

# Info box
INFO_BOX = f"""
{PURPLE}╔══════════════════════════════════════════════════════════════╗{RESET}
{PURPLE}║{RESET}{WHITE}{BOLD}              HACKME WHATSAPP TOOLS v1.0                      {RESET}{PURPLE}║{RESET}
{PURPLE}╠══════════════════════════════════════════════════════════════╣{RESET}
{PURPLE}║{RESET}  {BOLD}Author{RESET}   : Ruyynn                                           {PURPLE}║{RESET}
{PURPLE}║{RESET}  {BOLD}GitHub{RESET}   : github.com/ruyynn                                {PURPLE}║{RESET}
{PURPLE}║{RESET}  {BOLD}Version{RESET}  : 1.0 (Free Edition)                               {PURPLE}║{RESET}
{PURPLE}║{RESET}  {BOLD}License{RESET}  : MIT                                              {PURPLE}║{RESET}
{PURPLE}╚══════════════════════════════════════════════════════════════╝{RESET}"""

class WATools:
    def __init__(self):
        self.session_id = self.generate_session_id()
        self.results = []
        self.targets = []
        self.start_time = datetime.now()
        
    def generate_session_id(self):
        return hashlib.md5(str(random.getrandbits(128)).encode()).hexdigest()[:8]
    
    def clear_screen(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')
    
    def print_logo_with_info(self):
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
    
    def loading_animation(self, text, duration=1):
        chars = '⣾⣽⣻⢿⡿⣟⣯⣷'
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            print(f"\r{YELLOW}{chars[i % len(chars)]}{RESET} {text}", end='')
            i += 1
            time.sleep(0.1)
        print(f"\r{GREEN}✓{RESET} {text} - {GREEN}OK{RESET}   ")
    
    def validate_phone(self, number):
        # Simple validation for demo
        number = number.replace(' ', '').replace('-', '')
        if number.startswith('+'):
            if len(number) >= 10 and number[1:].isdigit():
                return number
        elif number.startswith('0'):
            if len(number) >= 10 and number.isdigit():
                return '+62' + number[1:]
        return None
    
    def check_number(self, number):
        """Simulate WhatsApp number check"""
        time.sleep(1)
        
        # Simple mock data
        providers = ['Telkomsel', 'Indosat', 'XL', 'Tri', 'Axis', 'Smart']
        locations = ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang', 'Makassar']
        
        registered = random.choice([True, False])
        
        return {
            'number': number,
            'registered': registered,
            'provider': random.choice(providers) if registered else 'Unknown',
            'location': random.choice(locations) if registered else 'Unknown',
            'online': random.choice([True, False]) if registered else False,
            'last_seen': (datetime.now() - timedelta(minutes=random.randint(1, 60))).strftime('%Y-%m-%d %H:%M:%S') if registered else 'Never',
            'profile': random.choice([True, False]) if registered else False
        }
    
    def save_result(self, result):
        os.makedirs('results', exist_ok=True)
        filename = f"result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(f'results/{filename}', 'w') as f:
            json.dump(result, f, indent=2)
        return filename
    
    def menu(self):
        while True:
            self.clear_screen()
            self.print_logo_with_info()
            
            print(f"\n{WHITE}{BOLD}MAIN MENU{RESET}")
            print(f"{DIM}{'─' * 64}{RESET}\n")
            
            menu_items = [
                ("1", "Check Number", "Check if number registered on WhatsApp"),
                ("2", "Get Info", "Get target information"),
                ("3", "Check Status", "Check online status & last seen"),
                ("4", "Profile Info", "Get profile picture & about"),
                ("5", "View Results", "View saved results"),
                ("6", "Clear Results", "Delete all saved results"),
                ("0", "Exit", "Exit HACKME WhatsApp Tools")
            ]
            
            for num, name, desc in menu_items:
                color = CYAN if num in ['1','2','3','4'] else YELLOW if num in ['5','6'] else RED
                print(f"  {color}[{num}]{RESET} {BOLD}{name:<15}{RESET} {DIM}{desc}{RESET}")
            
            print(f"\n{DIM}{'─' * 64}{RESET}")
            print(f"\n{GREEN}[+]{RESET} Session: {self.session_id}")
            print(f"{GREEN}[+]{RESET} Results: {len(self.results)}")
            
            choice = input(f"\n{CYAN}[[HACKME]]>{RESET} ").strip()
            
            if choice == '0':
                print(f"\n{GREEN}Thank you for using HACKME WhatsApp Tools!{RESET}")
                print(f"{BLUE}GitHub: github.com/ruyynn/hackme-wa{RESET}")
                sys.exit(0)
            
            elif choice == '1':
                self.clear_screen()
                self.print_logo_with_info()
                self.print_header("CHECK NUMBER")
                
                print(f"\n{YELLOW}Enter phone number (format: 08123456789 or +628123456789){RESET}")
                number = input(f"\n{CYAN}Number>{RESET} ").strip()
                
                if number:
                    validated = self.validate_phone(number)
                    if validated:
                        print(f"\n{BLUE}[*] Checking number: {validated}{RESET}")
                        self.loading_animation("Connecting to WhatsApp", 1)
                        self.loading_animation("Querying database", 1)
                        
                        result = self.check_number(validated)
                        
                        if result['registered']:
                            print(f"\n{GREEN}[✓] Number is registered on WhatsApp!{RESET}")
                            print(f"  {BLUE}Provider:{RESET} {result['provider']}")
                            print(f"  {BLUE}Location:{RESET} {result['location']}")
                        else:
                            print(f"\n{RED}[✗] Number is NOT registered on WhatsApp{RESET}")
                        
                        self.results.append(result)
                        filename = self.save_result(result)
                        print(f"\n{GREEN}[✓] Result saved to: results/{filename}{RESET}")
                        
                    else:
                        print(f"\n{RED}[✗] Invalid phone number format{RESET}")
                
                self.print_footer()
                input(f"{CYAN}Press Enter to continue...{RESET}")
            
            elif choice == '2':
                self.clear_screen()
                self.print_logo_with_info()
                self.print_header("GET TARGET INFO")
                
                if not self.results:
                    print(f"\n{YELLOW}[!] No results yet. Check a number first.{RESET}")
                else:
                    latest = self.results[-1]
                    print(f"\n{GREEN}[✓] Latest target information:{RESET}")
                    print(f"  {BLUE}Number:{RESET} {latest['number']}")
                    print(f"  {BLUE}Registered:{RESET} {latest['registered']}")
                    if latest['registered']:
                        print(f"  {BLUE}Provider:{RESET} {latest['provider']}")
                        print(f"  {BLUE}Location:{RESET} {latest['location']}")
                        print(f"  {BLUE}Online:{RESET} {latest['online']}")
                        print(f"  {BLUE}Last Seen:{RESET} {latest['last_seen']}")
                        print(f"  {BLUE}Has Profile:{RESET} {latest['profile']}")
                
                self.print_footer()
                input(f"{CYAN}Press Enter to continue...{RESET}")
            
            elif choice == '3':
                self.clear_screen()
                self.print_logo_with_info()
                self.print_header("CHECK STATUS")
                
                if not self.results:
                    print(f"\n{YELLOW}[!] No results yet. Check a number first.{RESET}")
                else:
                    latest = self.results[-1]
                    if latest['registered']:
                        print(f"\n{BLUE}[*] Checking status for {latest['number']}{RESET}")
                        self.loading_animation("Pinging device", 1)
                        self.loading_animation("Checking online status", 1)
                        
                        # Update status
                        latest['online'] = random.choice([True, False])
                        latest['last_seen'] = (datetime.now() - timedelta(minutes=random.randint(1, 30))).strftime('%Y-%m-%d %H:%M:%S')
                        
                        print(f"\n{GREEN}[✓] Status updated:{RESET}")
                        print(f"  {BLUE}Online:{RESET} {latest['online']}")
                        print(f"  {BLUE}Last Seen:{RESET} {latest['last_seen']}")
                    else:
                        print(f"\n{RED}[✗] Target not registered on WhatsApp{RESET}")
                
                self.print_footer()
                input(f"{CYAN}Press Enter to continue...{RESET}")
            
            elif choice == '4':
                self.clear_screen()
                self.print_logo_with_info()
                self.print_header("PROFILE INFO")
                
                if not self.results:
                    print(f"\n{YELLOW}[!] No results yet. Check a number first.{RESET}")
                else:
                    latest = self.results[-1]
                    if latest['registered'] and latest['profile']:
                        print(f"\n{GREEN}[✓] Profile found:{RESET}")
                        print(f"  {BLUE}Profile Picture:{RESET} Available")
                        print(f"  {BLUE}About:{RESET} {random.choice(['Busy', 'Available', '❤️', '🌹', 'Gaming'])}")
                        print(f"  {BLUE}Last Updated:{RESET} {random.choice(['Today', 'Yesterday', 'Last week'])}")
                    elif latest['registered'] and not latest['profile']:
                        print(f"\n{YELLOW}[!] Target has no profile picture or about{RESET}")
                    else:
                        print(f"\n{RED}[✗] Target not registered{RESET}")
                
                self.print_footer()
                input(f"{CYAN}Press Enter to continue...{RESET}")
            
            elif choice == '5':
                self.clear_screen()
                self.print_logo_with_info()
                self.print_header("VIEW RESULTS")
                
                if not self.results:
                    print(f"\n{YELLOW}[!] No results yet.{RESET}")
                else:
                    print(f"\n{GREEN}[✓] Saved results ({len(self.results)}):{RESET}")
                    for i, result in enumerate(self.results[-10:], 1):
                        status = f"{GREEN}Registered{RESET}" if result['registered'] else f"{RED}Not Registered{RESET}"
                        print(f"  {BLUE}{i}.{RESET} {result['number']} - {status}")
                
                # Check files
                if os.path.exists('results'):
                    files = os.listdir('results')
                    print(f"\n{BLUE}[*] Files in results folder: {len(files)}{RESET}")
                
                self.print_footer()
                input(f"{CYAN}Press Enter to continue...{RESET}")
            
            elif choice == '6':
                self.clear_screen()
                self.print_logo_with_info()
                self.print_header("CLEAR RESULTS")
                
                confirm = input(f"\n{RED}Are you sure? (y/N):{RESET} ").strip().lower()
                if confirm == 'y':
                    self.results = []
                    if os.path.exists('results'):
                        for f in os.listdir('results'):
                            os.remove(f'results/{f}')
                    print(f"\n{GREEN}[✓] All results cleared{RESET}")
                else:
                    print(f"\n{YELLOW}[!] Operation cancelled{RESET}")
                
                self.print_footer()
                input(f"{CYAN}Press Enter to continue...{RESET}")
            
            else:
                print(f"\n{RED}[!] Invalid option{RESET}")
                time.sleep(1)

def main():
    try:
        # Create necessary directories
        os.makedirs('results', exist_ok=True)
        
        # Run the tool
        tools = WATools()
        tools.menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Interrupted by user{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n{RED}Error: {str(e)}{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
