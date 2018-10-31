RED="\033[31m"
YELLOW="\033[33m"
BLUE='\033[1;34m'

echo Installing requirements ...

apt update -y
apt upgrade -y
pkg install python -y
pip install --upgrade pip
pip install requests
pkg install figlet 
pkg install toilet

clear
sleep 0 

echo -e $YELLOW  Author : 
echo -e $BLUE github.com/7rillionaire


echo
echo -e $RED ■■■■■■■■■■■■■■■■■■■

echo -e $YELLOW Errors? : 
echo -e $BLUE https://github.com/7rillionaire/search4/issues
echo
echo -e $RED ■■■■■■■■■■■■■■■■■■■
 
echo -e $YELLOW Dev on telegram : 
echo -e $BLUE https://t.me/trilli0n4ir3
echo 


sleep 2 
cd $HOME/Search4
chmod +x search4.py


