#!/bin/bash

# Update the package list
sudo apt update

# Open Ports
sudo ufw allow 80
sudo ufw allow 443

# Install NGINX
sudo apt install nginx -y

# Install MariaDB
sudo apt install mariadb-server mariadb-client -y

# Secure the MariaDB installation
sudo mysql_secure_installation

# Install PHP 8.1 and required extensions
sudo apt install ca-certificates apt-transport-https -y
sudo wget -q https://packages.sury.org/php/apt.gpg -O- | sudo apt-key add -
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php.list
sudo apt update
sudo apt install php8.1-fpm php8.1-mysql php8.1-curl php8.1-gd php8.1-intl php8.1-mbstring php8.1-soap php8.1-xml php8.1-zip -y

# Configure NGINX and PHP-FPM
sudo sed -i 's/# server_names_hash_bucket_size 64;/server_names_hash_bucket_size 64;/g' /etc/nginx/nginx.conf
sudo sed -i 's|index index.html index.htm index.nginx-debian.html;|index index.php index.html index.htm;|g' /etc/nginx/sites-available/default
sudo sed -i 's|#location ~ \\\.php$ {|location ~ \\\.php$ {|g' /etc/nginx/sites-available/default
sudo sed -i 's|#\tinclude snippets/fastcgi-php.conf;|\tinclude snippets/fastcgi-php.conf;|g' /etc/nginx/sites-available/default
sudo sed -i 's|#\tfastcgi_pass unix:/run/php/php8.1-fpm.sock;|\tfastcgi_pass unix:/run/php/php8.1-fpm.sock;|g' /etc/nginx/sites-available/default

# Restart NGINX and PHP-FPM
sudo systemctl restart nginx
sudo systemctl restart php8.1-fpm

# Download and extract the latest version of WordPress
cd ~
wget -q https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
rm latest.tar.gz

# Set the correct permissions
sudo chown -R www-data:www-data ~/wordpress/
sudo chmod -R 755 ~/wordpress/

# Create a new NGINX server block for WordPress
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/wordpress

# Edit the server block to remove the /wordpress path
sudo sed -i 's|root /home/$USER/wordpress;|root /home/$USER/;|g' /etc/nginx/sites-available/wordpress
sudo sed -i 's|location /wordpress {|location / {|g' /etc/nginx/sites-available/wordpress
sudo sed -i 's|try_files $uri $uri/ /wordpress/index.php?$args;|try_files $uri $uri/ /index.php?$args;|g' /etc/nginx/sites-available/wordpress

# Set the server name to your domain name
# Ask the user for the domain name
read -p "Enter your domain name (without www): " domain_name

# Set the server name to the user's domain name
sudo sed -i "s|server_name your-domain.com www.your-domain.com;|server_name $domain_name www.$domain_name;|g" /etc/nginx/sites-available/wordpress


# Enable the server block and disable the default one
sudo ln -s /etc/nginx/sites-available/wordpress /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default

