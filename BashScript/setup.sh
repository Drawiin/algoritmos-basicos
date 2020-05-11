# Um script que uso para intalar todos os programas que utilizo no linux(Ubunto)

# -y na frente de tudo

# atuazliar os ppas
echo 'iniciando.........'
echo '============================atulizando ppas===================================='
sudo apt update -y

# build-essesntial
echo '============================instalando build essentials===================================='
apt install build-essential -y

# git
echo '===================intalando git.======================'
apt install git -y

# curl
echo '============================Istalando curl===================================='
apt install curl -y

#wget
echo '============================Instalando Wget===================================='
apt install wget -y

# chrome
echo '============================Instalando chrome===================================='
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install ./google-chrome-stable_current_amd64.deb -y

# nvm
echo '============================Instalando nvm===================================='

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"

[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# nodejs with nvm
echo '============================Instalando NodeJS===================================='
nvm install --lts
# Open JDK
echo '============================Instalando openJDK===================================='
apt-get install openjdk-8-jdk
# golang
echo '============================Golang===================================='
add-apt-repository ppa:longsleep/golang-backports
apt update
apt install golang-go -y
# ubunto kvm
# vscode
echo '============================ instalando vscode===================================='
snap install code --classic

# qbittorent
echo '============================instalando qbittorrent===================================='
add-apt-repository ppa:qbittorrent-team/qbittorrent-stable -y
apt-get update && sudo apt-get install qbittorrent -y

# spotfy
echo '============================  spotfy ===================================='
snap install spotify

# vlc
echo '============================ vlc ===================================='
snap install vlc

# insomnia
echo '============================ insomnia ===================================='
snap install insomnia

# Intelij idead Comminity
echo '============================ Intellijidea ===================================='
sudo snap install intellij-idea-community --classic

# postgreSQL
echo '============================PostegreSQL===================================='
sudo apt install postgresql postgresql-contrib -y

# oh my z shell






    
