# Basic DNS Setup - GitHub Pages

## Objective

Learn the fundamentals of DNS by configuring a custom domain for GitHub Pages and verifying DNS resolution.

## What I Did

* Verified DNS records using:

  * `nslookup`
  * `host`
  * `dig`
* Confirmed that the domain `patrickphat.fyi` resolved correctly.
* Configured the custom domain in **GitHub Pages**.
* Verified that GitHub Pages recognized the custom domain.
* Learned how DNS maps a domain name to the correct web service.

## Commands Used

```bash
nslookup patrickphat.fyi
host patrickphat.fyi
dig github.com
```

## Key Concepts Learned

* **DNS** translates domain names into IP addresses.
* **A Record** maps a domain to an IPv4 address.
* **GitHub Pages** can host a static website using a custom domain.
* A custom domain requires both DNS configuration and GitHub Pages configuration.

## Result

* Successfully verified DNS resolution.
* Successfully connected the custom domain to GitHub Pages.
* Gained a basic understanding of how DNS works before moving to more advanced topics such as Nginx, Reverse Proxy, and Kubernetes Ingress.

## Next Step

Configure DNS records for a cloud server (DigitalOcean Droplet) and compare how DNS points to different services.
