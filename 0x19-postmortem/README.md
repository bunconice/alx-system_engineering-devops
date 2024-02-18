# Postmortem

## Issue Summary

* Duration: February 18, 2024, 10:00 AM - 1:00 PM (UTC)
* Impact: The main web application experienced intermittent outages, resulting in a 30% increase in error rates and degraded performance for users accessing the platform.
* Root Cause: A misconfigured firewall rule led to blocking critical API requests, causing service disruptions.

## Timeline

* 10:00 AM: Issue detected through automated monitoring alerts indicating a spike in error rates.
* 10:05 AM: Engineering team notified of the incident.
* 10:15 AM: Investigation commenced, focusing on recent system changes and network configurations.
* 10:45 AM: Initial assumption made that the database server might be overloaded due to recent traffic spikes.
* 11:15 AM: Further investigation revealed no significant load issues on the database server, shifting focus to network infrastructure.
* 11:45 AM: Misleading assumption that a recent deployment might have introduced bugs led to a brief code rollback, which did not resolve the issue.
* 12:15 PM: Incident escalated to network and security teams for deeper analysis.
* 12:30 PM: Firewall logs reviewed, identifying a misconfigured rule blocking critical API traffic.
* 1:00 PM: Issue resolved by correcting the firewall rule and confirming restoration of normal service.

## Root Cause and Resolution

* Root Cause: A misconfigured firewall rule inadvertently blocked incoming API requests from the load balancer to the application servers.
* Resolution: The misconfigured firewall rule was corrected to allow necessary API traffic, restoring proper communication flow between components of the web stack.

## Corrective and Preventative Measures

### Improvements/Fixes

* Strengthening change management processes to prevent misconfigurations during network updates.
* Enhancing monitoring systems to provide early detection of similar network disruptions.
* Implementing thorough testing procedures for firewall rule changes before deployment.

### Tasks to Address the Issue

* Conduct a comprehensive review of all firewall rules to identify and rectify any other potential misconfigurations.
* Enhance documentation and communication protocols surrounding network changes to ensure clarity and accountability.
* Schedule regular training sessions for engineering teams on best practices for network configuration and troubleshooting.

In conclusion, the outage on February 18, 2024, was a result of a misconfigured firewall rule blocking critical API traffic. Through diligent investigation and collaboration across teams, the issue was promptly identified and resolved. Moving forward, implementing corrective measures and enhancing preventative measures will mitigate the risk of similar incidents in the future, ensuring the continued reliability and performance of our web stack infrastructure.
