sudo usermod -aG dialout latinoware
sudo yum install screen
sudo yum install podman-compose
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
