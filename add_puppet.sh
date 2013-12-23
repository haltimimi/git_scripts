#!/bin/bash

wget http://apt.puppetlabs.com/puppetlabs-release-precise.deb

dpkg -i puppetlabs-release-precise.deb

echo "__installing puppet"
apt-get -qq update 

apt-get install -y -qq puppet
echo "__done__"
echo "__puppet agent version:"
puppet agent --version

if ! grep -q puppet /etc/hosts ; then 
   echo "105.68.25.30  puppet" >> /etc/hosts 
fi
