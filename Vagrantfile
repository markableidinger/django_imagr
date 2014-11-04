# -*- mode: ruby -*-
# vi: set ft=ruby :

$postgresSetup = <<EOL
apt-get update
apt-get install --assume-yes postgresql postgresql-contrib
sudo -u postgres createdb psycotest 
sudo -u postgres psql -U postgres postgres <<EOS
  create user admin with password 'password';
  grant all on database psycotest to admin;
EOS
echo "host all all 0.0.0.0/0 password" >> /etc/postgresql/9.1/main/pg_hba.conf
echo "listen_addresses = '*'" >> /etc/postgresql/9.1/main/postgresql.conf
service postgresql restart
EOL


# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.network "forwarded_port", guest: 5432, host: 55432
  config.vm.synced_folder ".", "/opt/sql"
  config.vm.provision :shell, :inline => $postgresSetup
end
