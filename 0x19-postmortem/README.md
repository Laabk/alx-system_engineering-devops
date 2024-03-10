
Impact:




Affected Service: The entire application built on PHP 7 faced a shutdown.
User Impact: Users encountered difficulties accessing their accounts and sending requests.
Extent of Impact: Nearly all users experienced disruptions due to this downtime.
Cause of Issue: The crash stemmed from an update deployed to the production environment while certain methods relied on older development tools (PHP 7, Apache 5).
Timeline:


Detection Time: The issue was noticed at 2:00 AM on 10/07/2023 through alerts in the application's deployment log.
Actions Taken:



Resolution: The application's development state was rolled back to resolve the issue.
Initial Investigation: Initial attempts to adapt methods and variables to the new version led to complications.
Team Involvement: The developers' team was engaged to address the incident.
Resolution Process: Rolling back the application to its previous state resolved the issue, albeit resulting in new users losing their accounts.
Root Cause and Resolution:


Cause: An individual's attempt to upgrade their local development stack inadvertently impacted the entire production environment.
Resolution: Reverting the application to its previous state resolved the issue.
Issue Resolution Process:


The issue was addressed by reverting the application, including data, to a prior state.
Additionally, automated backups were scheduled to prevent future incidents.
Corrective and Preventative Measures:



Use of Docker Containers: Developers' local setups were configured with Docker containers to isolate changes and prevent system-wide impacts.
Approaches to Address the Issue:




Reviewing log files
Rectifying log errors
Identifying relevant files
Recognizing the current error message
Restoring the application to a known good stated
