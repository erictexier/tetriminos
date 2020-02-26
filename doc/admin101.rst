Admin 101
======

L'adresse IPv4 du VPS est : 51.178.81.105
L'adresse IPv6 du VPS est : 2001:41d0:0404:0200:0000:0000:0000:4dcf

On server (AS ROOT):  
1. ssh root@IPADDRESS
2. apt-get update && apt-get upgrade
3. hostname set-hostname xaos
4. nano /etc/hosts   (-> add (for example)):  IPADDRESS project-server-name)
5. Add new user:   adduser username (-> set password + name etc ….)
6. adduser username sudo
7. Exit server

# SSH

8. ssh username@IPADDRESS
9. mkdir -p ~/.ssh
Local:
 ssh-keygen -b 4096
 $ ssh-copy-id -i ~/.ssh/mykey username@host
 	or (scp ~/.ssh/id_rsa.pub username@IPADDRESS:~/.ssh/authorized_keys
Server:
sudo chmod 700 ~/.ssh
sudo chmod 600 ~/.ssh/*
Exit server and relog with:  ssh username@IPADDRESS

# TO BE REVIEW - 
Server ( best practices: not allow root logging and no password authentications
sudo nano /etc/ssh/sshd_config  
	-uncomment: PermitRootLogin no (prohibit-password)
    -uncomment: PasswordAuthentication no

sudo systemctl restart sshd


# FIRE WALL (FOR INITIAL TEST)
sudo apt-get install ufw 
sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw allow 5000
sudo ufw enable 
sudo ufw status

On local:
Activate virtualenv and make sure the requirements.txt is there
git clone or scp -r your_project username@IPADDRESS:~/

On Server:
sudo apt-get install python3-pip
sudo apt-get install python3-venv
(Create a virtualenv inside the django_project folder)
python3 -m venv your_project/venv
cd django_project/
source venv/bin/activate
pip install -r requirements.txt
 OR WITH CODA: with conda: while read requirement; do conda install --yes $requirement; done < requirements.txt


FLASK:
        see doc/dependency_and_setting.txt

DJANGO:

Edit settings:
	- ALLOWED_HOSTS = [‘IPADDRESS’]
	- Add STATIC_ROOT: (STATIC_ROOT = os.path.join(BASE_DIR, ‘static’)
python manage.py collectstatic
# start django
python manage.py runserver 0.0.0.0:8000

# now we don’t want to run on django server but instead a production server:
#install apache2
cd
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3

cd /etc/apache2/sites-available/
su cp 000-default.conf django_project.conf

nano django_project.conf
(Before the </VirtualHost> insert:)
Alias /static /home/username/django_project/static
<Directory /home/username/django_project/static>
	Require all granded
</Directory>

Alias /media /home/username/django_project/media
<Directory /home/username/django_project/media>
	Require all granded
</Directory>

<Directory /home/username/django_project/django_project>
	<Files wsgi.py>
		Require all granted
	</Files>
</Directory>

WSGIScriptAlias / /home/username/django_project/django_project/wsgi.py
WSGIDaemonProcess django_app python-path=/home/username/django_project python-home=/home/username/django_project/venv
WSGIProcessGroup django_app

sudo a2ensite django_project
sudo a2dissite 000-default.conf

sudo chown :www-data django_project/db.sqlite3  #(???)
sudo chmod 664 django_project/db.sqlite3 
sudo chmod chown :www-data django_project/

sudo chown -R :www-data django_project/media
sudo chmod -R 775 django_project/media 

sudo touch /etc/config.json
sudo nano …settings.py  (remove but copy first the secret key)

Interfaces réseaux

ifconfig -l

git config --get remote.origin.url


