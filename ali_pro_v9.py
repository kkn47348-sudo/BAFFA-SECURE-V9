# BAFFA SECURE V9 - by Ali Baffa
import re

print("""
╔════════════════════════════════╗
║   BAFFA SECURE V9 🔐           ║
║   Fake Email Checker           ║
║   By Ali Baffa - Rawalpindi    ║
╚════════════════════════════════╝
""")

fake_domains = ["tempmail.com", "10minutemail.com", "guerrillamail.com", "mailinator.com", "yopmail.com", "fakeemail.com"]

def check_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "❌ Invalid Format"
    domain = email.split("@")[1].lower()
    if domain in fake_domains or "temp" in domain or "fake" in domain:
        return "⚠️ FAKE / TEMP EMAIL DETECTED!"
    else:
        return "✅ Real Email Lag Raha Hai"

while True:
    email = input("\nEmail daalo (exit ke liye 'q'): ")
    if email.lower() == 'q':
        print("Allah Hafiz Jani! - BAFFA SECURE V9")
        break
    result = check_email(email)
    print(f"Result: {result}")
