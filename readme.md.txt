# 💀 PhishLink Injector

**🔥 Offensive Tool for Malware Delivery & Drive-by Downloads 🔥**

PhishLink Injector is a powerful Python application designed to act as a central hub for distributing malicious payloads. It generates a stable, high-availability public URL (using Cloudflare Tunnel) that redirects victims to your crafted attack landing page, effectively delivering the malware virus into their system upon clicking.

---

## 🚀 Features

*   **Cloudflare Integration:** Generates a robust, stable `.onion` or standard URL link via `cloudflared` for maximum reach and reliability.
*   **Dynamic Payload:** Serves as a dynamic server capable of hosting the landing page and triggering various attack vectors (Drive-by Downloads, Adware redirects, etc.).
*   **Python Backend:** Easy to deploy on Kali Linux or Termux.

---

## 🛠️ Prerequisites

1.  **Python 3.x** installed.
2.  **Cloudflare Account & Tunnel:** You must have a Cloudflare account and set up a domain or subdomain you wish to tunnel.
3.  **`cloudflared`:** The Cloudflare Tunnel client must be installed and configured on your host machine (Kali/Termux).

## 📥 Installation & Setup

1.  **Clone Repository:**
    ```bash
    git clone [your-repo-url]
    cd PhishLink-Injector