sudo usermod -aG dialout latinoware
sudo yum -y install screen
sudo yum -y install podman-compose
##Oficina Franzininho C0
sudo yum -y install openjfx
podman pull docker.io/library/nginx
podman pull docker.io/library/nginx
cd /home/latinoware
mkdir espmpy
cd espmpy
git clone https://github.com/micropython/webrepl.git
python -m venv mpy 
source /home/latinoware/espmpy/mpy/bin/activate
pip install --upgrade pip
pip install jupyter lab
pip install adafruit_ampy
sudo shutdown -r now 
