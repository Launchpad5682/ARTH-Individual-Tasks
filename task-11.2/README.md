# Restart HTTPd server idempotently 

Restarting HTTPD Service is not
idempotence in nature and also consume more
resources suggest a way to rectify this challenge
in Ansible playbook.

We only need to restart the server only when the configuration files are changed.