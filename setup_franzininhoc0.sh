cd ~
cd Documentos
scp 192.168.28.139:/home/latinoware/Documentos/*.zip .
yum -y install openjfx
unzip en.st-stm32cubeide_1.13.2_18220_20230914_1601_amd64.rpm_bundle.sh.zip
sudo sh st-stm32cubeide_1.13.2_18220_20230914_1601_amd64.rpm_bundle.sh
unzip en.stm32cubeprg-lin-v2-14-0.zip
./SetupSTM32CubeProgrammer-2.14.0.linux 
