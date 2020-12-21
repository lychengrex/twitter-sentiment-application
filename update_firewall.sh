# The Ubuntu firewall is disabled by default.
# It is still necessary to update your iptables configuration to allow HTTP traffic.
# Set `5050` to another port as you wish
# Reference: https://docs.cloud.oracle.com/en-us/iaas/developer-tutorials/tutorials/flask-on-ubuntu/01oci-ubuntu-flask-summary.htm
sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 5050 -j ACCEPT
sudo netfilter-persistent save