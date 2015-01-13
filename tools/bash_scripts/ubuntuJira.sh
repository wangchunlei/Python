#!/bin/bash

# get some parameters
echo "sudo password:"
read password

# install jdk
echo $password | sudo -S apt-get install openjdk-7-jdk -y

# setting the JAVA_HOME
echo $password | sudo -S sh -c 'echo JAVA_HOME="/usr/lib/jvm/java-7-openjdk-amd64" >> /etc/environment'
. /etc/environment

# download and extract the jira archive file
cd ~
mkdir tmp
cd tmp
wget http://downloads.atlassian.com/software/jira/downloads/atlassian-jira-6.3.6.tar.gz

mkdir -p ~/atlassian/jira
tar xzvf atlassian-jira-6.3.6.tar.gz -C ~/atlassian/jira

# create jira user account
echo $password | sudo -S /usr/sbin/useradd --create-home --comment "jira user" --shell /bin/bash jira

# set jira home
mkdir -p ~/jira_home
chown jira:jira ~/jira_home/
export JIRA_HOME=~/jira_home

# start jira
cd ~/atlassian/jira/atlassian-jira-6.3.6-standalone
./bin/start-jira.sh



