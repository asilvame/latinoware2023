sudo usermod -aG dialout latinoware
sudo usermod -aG dialout latinoware2023
sudo yum  -y install python3-pip
sudo yum -y install thonny
pip install pyserial
cd ~
curl https://raw.githubusercontent.com/asilvame/latinoware2023/main/Banco_de_informacoes_de_Hardware_BIH.pdf -o Banco_de_informacoes_de_Hardware_BIH.pdf 
curl https://downloads.arduino.cc/arduino-ide/arduino-ide_2.2.1_Linux_64bit.AppImage -o arduino-ide_2.2.1_Linux_64bit.AppImage 
chmod +x arduino-ide_2.2.1_Linux_64bit.AppImage
mkdir Arduino
mkdir Arduino/libraries
cd Arduino/libraries
git clone https://github.com/Franzininho/biblioteca-laboratorioFW-DIY.git laboratorioFW-DIY
git clone https://github.com/mobizt/Firebase-ESP-Client.git
sudo yum -y install screen
sudo yum -y install podman-compose
##Oficina Franzininho C0
sudo yum -y install openjfx
podman pull docker.io/library/nginx
podman pull docker.io/library/nginx
cd 
mkdir espmpy
cd espmpy
git clone https://github.com/micropython/webrepl.git
python -m venv mpy 
source ~/espmpy/mpy/bin/activate
pip install --upgrade pip
pip install jupyter lab
pip install adafruit_ampy
sudo shutdown -r now 
