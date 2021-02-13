sudo rm /var/lib/dpkg/lock-frontend ; sudo rm /var/cache/apt/archives/lock ;

sudo apt update &&
sudo apt upgrade -y &&

sudo apt install python3-pip -y &&
sudo apt install python3-pyaudio -y ;
sudo apt install python3-tk -y ;
sudo apt install python3-os -y ;
sudo pip3 install chatterbot==1.0.0 ;
sudo pip3 install pytz ;
sudo pip3 install speechrecognition ;
sudo pip3 install gtts ;
sudo pip3 install playsound ;
sudo apt install gstreamer-1.0 -y ;
sudo apt install python3-gst-1.0 -y ;

sudo apt update ;
sudo apt upgrade -y ;

echo "########################################"
echo "#################TERMINOU###############"
echo "########################################"
