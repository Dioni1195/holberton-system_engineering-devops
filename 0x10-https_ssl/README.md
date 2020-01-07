# 0x10-https_ssl
---

## HTTPS SSL
---
- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means
### Files
---
File Name | Description
--- | ---
0-https_abc| What is HTTPS? Why do you need HTTPS? You want to setup HTTPS on your website, where shall you place the certificate?
1-world_wide_web | Configure your domain zone so that the subdomain www points to your load-balancer IP
2-haproxy_ssl_termination | Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www.
