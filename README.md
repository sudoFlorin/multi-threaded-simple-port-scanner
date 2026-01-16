This is a very fast and simple multi-threaded port scanner which utilises Python's threading library which makes it possible to check multiple ports simultaneously, reducing the scan time from hours to minutes.


Upon running the script, it request for the host address to be scanned, and the scan type (Common Ports, or Custom Range)

Please see below the list of predefined ports, services that run on them,  the protocol they use, what they are utilised for and the security risk they pose

| Port | Service | Protocol | Category | Description | Security Risk |
|---|---|---|---|---|---|
| 21 | FTP | TCP | File Transfer | File Transfer Protocol (Control) | High - Credentials sent in plain text |
| 22 | SSH | TCP | Remote Access | Secure Shell for remote login | Low - Encrypted (Industry Standard) |
| 23 | Telnet | TCP | Remote Access | Unencrypted remote login | Critical - All data sent in plain text |
| 25 | SMTP | TCP | Email | Simple Mail Transfer Protocol | Moderate - Can be abused for spam |
| 53 | DNS | TCP/UDP | Infrastructure | Domain Name System | Moderate - Targets for DNS spoofing |
| 80 | HTTP | TCP | Web | Unencrypted web traffic | High - No encryption; use 443 instead |
| 110 | POP3 | TCP | Email | Post Office Protocol | High - Plain text; use 995 instead |
| 135 | RPC | TCP/UDP | Infrastructure | Microsoft Remote Procedure Call | Moderate - Potential for remote exploits |
| 139 | NetBIOS | TCP | File Sharing | NetBIOS Session Service | High - Legacy protocol; often targeted |
| 143 | IMAP | TCP | Email | Accessing emails on a server | High - Plain text; use 993 instead |
| 443 | HTTPS | TCP | Web | Encrypted web traffic | Low - Secure (Standard for Web) |
| 445 | SMB | TCP | File Sharing | Windows file sharing | Critical - Vulnerable to ransomware (EternalBlue) |
| 993 | IMAPS | TCP | Email | Secure IMAP (over SSL/TLS) | Low - Encrypted |
| 995 | POP3S | TCP | Email | Secure POP3 (over SSL/TLS) | Low - Encrypted |
| 1723 | PPTP | TCP/UDP | Networking | VPN Tunneling Protocol | Moderate - Older VPN protocol; weaker security |
| 3306 | MySQL | TCP | Database | MySQL/MariaDB database | Moderate - Should never be exposed to public |
| 3389 | RDP | TCP/UDP | Remote Access | Windows Remote Desktop | High - Target for brute-force attacks |
| 5900 | VNC | TCP | Remote Access | VNC desktop sharing | High - Often poorly secured |
| 8080 | HTTP-Alt | TCP | Web | Web proxies or dev servers | Moderate - Often lacks production hardening ||
| 8080 | HTTP-Alt | TCP      | Web            | Web proxies or development servers             |
