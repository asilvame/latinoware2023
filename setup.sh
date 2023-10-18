sudo usermod -aG dialout latinoware
sudo yum install screen
cd /home/latinoware
mkdir espmpy
cd espmpy
python -m venv mpy 
source /home/latinoware/espmpy/mpy/activate
pip install jupyter lab
pip install adafruit_ampy
