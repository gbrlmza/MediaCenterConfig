## GENERAL
- Install raspian lite
- Enable SSH access (or create a files named "ssh" on boot partition)
- Set correct timezone with raspi-config
- Set aliases(.bashrc)

## PLEX MEDIA SERVER
- Update: sudo apt-get update && sudo apt-get upgrade -y
- sudo apt-get install apt-transport-https -y
- wget -O - https://dev2day.de/pms/dev2day-pms.gpg.key | sudo apt-key add -
- echo "deb https://dev2day.de/pms/ jessie main" | sudo tee /etc/apt/sources.list.d/pms.list
- sudo apt-get update
- sudo apt-get install -t jessie plexmediaserver -y
- sudo nano /etc/default/plexmediaserver (Set PLEX_MEDIA_SERVER_USER=pi)
- sudo reboot
- Access <ip>:32400/web

## Utilities
- sudo apt-get install htop git -y
- git config --global user.name "John Doe"
- git config --global user.email johndoe@example.com
- ssh-keygen

## External HDD USB (from https://pimylifeup.com/raspberry-pi-mount-usb-drive/)
- sudo apt-get install ntfs-3g -y
- sudo mkdir /media/tosh500
- Montar HDD USB (Toshiba 500)
- fstab:
UUID=806E7AEF6E7ADD7A    /media/tosh500 auto nofail,uid=1000,gid=1000,noatime 0 0

## Flexget && Scripts
- sudo apt-get install python-pip python3-pip -y
- Upgrade pip for python 2.7: sudo easy_install --upgrade pip
- sudo pip install transmissionrpc requests python-telegram-bot
- sudo pip3 install transmissionrpc requests python-telegram-bot
- sudo pip install flexget

## Transmission Daemon
- sudo apt-get install transmission-daemon -y

## Samba Shared
- sudo apt-get install samba
- Add to /etc/samba/smb.conf:
  [tosh500]
  path = /media/tosh500
  writeable = yes
  browseable = yes
  public = yes
  create mask = 0644
  directory mask = 0755
  force user = pi
