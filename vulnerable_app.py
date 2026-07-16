"""
DELIBERATELY VULNERABLE SAMPLE
For local security testing and SAST demonstrations only.

Do not deploy this file to production.
The vulnerable functions below are intentionally NOT executed automatically.
"""

import os
import sqlite3
import subprocess

# 1. Hardcoded secret (Gitleaks / Secret Scanners should catch this)
API_KEY = "sk_test_1234567890_MySecretKeyHere"


# 2. SQL Injection Vulnerability (SAST should flag the raw string formatting)
def get_user_profile(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # לא מאובטח! שרשור מחרוזת ישיר במקום שימוש ב-Parameters
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchall()


# 3. Command Injection Vulnerability (SAST should flag shell=True with user input)
def ping_host(hostname):
    # לא מאובטח! תוקף יכול להעביר מחרוזת כמו "8.8.8.8; rm -rf /"
    command = f"ping -c 1 {hostname}"
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    return result.stdout
