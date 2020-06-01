# Um script que uso para intalar todos os programas que utilizo no linux(Ubunto)

# -y na frente de tudo

# atuazliar os ppas
echo 'iniciando.........'
echo '============================atualizando ppas===================================='
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

# vscode
echo '============================ instalando vscode===================================='
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg

sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/

sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
apt-get install apt-transport-https
apt-get update
apt-get install code -y

# Open JDK
echo '============================Instalando openJDK===================================='
apt install openjdk-8-jdk -y

# qbittorent
echo '============================instalando qbittorrent===================================='
add-apt-repository ppa:qbittorrent-team/qbittorrent-stable -y
apt-get update && sudo apt-get install qbittorrent -y

# spotfy
echo '============================  spotfy ===================================='
curl -sS https://download.spotify.com/debian/pubkey.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt-get update && sudo apt-get install spotify-client -y


# insomnia
echo '============================ insomnia ===================================='
# Add to sources
echo "deb https://dl.bintray.com/getinsomnia/Insomnia /" \
    | sudo tee -a /etc/apt/sources.list.d/insomnia.list

# Add public key used to verify code signature
wget --quiet -O - https://insomnia.rest/keys/debian-public.key.asc \
    | sudo apt-key add -

# Refresh repository sources and install Insomnia
sudo apt-get update
sudo apt-get install insomnia -y


# vlc
echo '============================ vlc ===================================='
sudo add-apt-repository ppa:videolan/stable-daily
sudo apt update
sudo apt install vlc -y

# Intelij idead Comminity
echo '============================ Intellijidea ===================================='
sudo snap install intellij-idea-community --classic





    
