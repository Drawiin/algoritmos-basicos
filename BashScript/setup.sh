# Um script que uso para intalar todos os programas que utilizo no linux(Ubunto)
# nvm -> nodejs
# vscode -> instalar extensões code --install-extension 
# git -> (config user and emal -> create ssh key)
# insomnia

echo "Atualizando repositórios.."
if ! apt update
then
    echo “Não foi possível atualizar os repositórios. Verifique seu arquivo /etc/apt/sources.list”
    exit 1
fi

echo "intalliing chrome"
if wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
then
    dpkg -i google-chrome-stable_current_amd64.deb
fi

echo "installing Vscode"
if wget https://go.microsoft.com/fwlink/?LinkID=760868
then
    apt install ./google-chrome-stable_current_amd64.deb
fi


echo "intallando insomnia"

echo "deb https://dl.bintray.com/getinsomnia/Insomnia /" \
    | sudo tee -a /etc/apt/sources.list.d/insomnia.list

wget --quiet -O - https://insomnia.rest/keys/debian-public.key.asc \
    | sudo apt-key add -

sudo apt-get update
sudo apt-get install insomnia

echo "intall NVM"

if wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
then
    export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
fi