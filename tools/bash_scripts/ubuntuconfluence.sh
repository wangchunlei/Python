#!/bin/bash

# get some parameters
echo "sudo password:"
read password

# install jdk
echo $password | sudo -S apt-get install openjdk-7-jdk -y

# setting the JAVA_HOME
echo $password | sudo -S sh -c 'echo JAVA_HOME="/usr/lib/jvm/java-7-openjdk-amd64" >> /etc/environment'
. /etc/environment

# download and extract the confluence archive file
cd ~
mkdir tmp
cd tmp
# wget http://downloads.atlassian.com/software/confluence/downloads/atlassian-confluence-5.4.4.tar.gz

mkdir -p ~/atlassian/confluence
tar xzvf atlassian-confluence-5.4.4.tar.gz -C ~/atlassian/confluence

# copy crack

cp ~/tmp/con/Confluence_Crack/atlassian-extras-2.4.jar ~/tmp/con/Confluence_Crack/atlassian-extras-decoder-v2-3.1.1.jar ~/atlassian/confluence/atlassian-confluence-5.4.4/confluence/WEB-INF/lib
cp ~/tmp/con/Confluence_Crack/atlassian-universal-plugin-manager-plugin-2.14.jar ~/atlassian/confluence/atlassian-confluence-5.4.4/confluence/WEB-INF/atlassian-bundled-plugins

# create confluence user account
echo $password | sudo -S /usr/sbin/useradd --create-home --comment "confluence user" --shell /bin/bash confluence

# set confluence home
mkdir -p ~/confluence_home
chown confluence:confluence ~/confluence_home/
export confluence_HOME=/root/confluence_home
sed -i "s/^# confluence.home.*/confluence.home = \/root\/confluence_home/g" ~/atlassian/confluence/atlassian-confluence-5.4.4/confluence/WEB-INF/classes/confluence-init.properties

# start confluence
cd ~/atlassian/confluence/atlassian-confluence-5.4.4
./bin/start-confluence.sh



