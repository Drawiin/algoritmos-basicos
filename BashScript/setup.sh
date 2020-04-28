# Um script que uso para intalar todos os programas que utilizo no linux(Ubunto)

# -y na frente de tudo

# atuazliar os ppas
echo 'iniciando.........'
if !sudo apt update -y
    echo 'ops alguma coisa deu errado.....'
fi
# build-essesntial
apt install build-essential -y

# git
apt install git -y

# curl
apt install curl -y

#wget

apt install wget -y

# chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install ./google-chrome-stable_current_amd64.deb

# nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# nodejs with nvm
# Open JDK
# golang
# ubunto kvm
# vscode
snap install code --classic -y

# qbittorent
add-apt-repository ppa:qbittorrent-team/qbittorrent-stable -y
apt-get update && sudo apt-get install qbittorrent -y

# spotfy
snap install spotify -y

# vlc
snap install vlc -y

# insomnia
snap install insomnia -y

# Intelij idead Comminity
sudo snap install intellij-idea-community --classic -y

# postgreSQL
sudo apt install postgresql postgresql-contrib -y

# oh my z shell






    
