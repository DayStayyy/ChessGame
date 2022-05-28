#!/bin/bash
# script to install project chessgame
# Benjamin Gelineau 20/05/2022

sudo apt update
sudo apt upgrade
sudo apt-get install iptables 
sudo touch /etc/init.d/mon_firewall
echo -e "#!/bin/bash
iptables -F
sudo iptables -I INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -i eth0 -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -i eth0 -p tcp --dport 19999 -j ACCEPT
sudo iptables -A INPUT -i eth0 -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p icmp -j ACCEPT
sudo iptables -A INPUT -i eth0 -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -i eth0 -j DROP" >> /etc/init.d/mon_firewall
chmod 700 /etc/init.d/mon_firewall
/etc/init.d/mon_firewall

echo -e "
[Unit]
Description=Launch flask server
After=network.target

[Service]
Type=simple
Restart=always
WorkingDirectory=/var/ProjetInfra/chessgame/
ExecStart=python3 -m flask run -h 0.0.0.0 -p 80

[Install]
WantedBy=multi-user.target" >>  /etc/systemd/system/server.service

sudo su -
bash <(curl -Ss https://my-netdata.io/kickstart-static64.sh)
exit
cd ../..
sudo mkdir /var/ProjetInfra
cd /var/ProjetInfra
git clone https://gitlab.com/benji.gelineau/chessgame.git
sudo pip3 install -r requirements.txt
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker pi
sudo apt-get install python3-distutils python3-dev libffi-dev libssl-dev
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
sudo pip3 install docker-compose
curl https://rclone.org/install.sh | sudo bash
cd chessgame
sudo docker compose up -d
sleep 30
sudo systemctl start server.service



