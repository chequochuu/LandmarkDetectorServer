# LandmarkDetectorServer
export LC_ALL=C  
sudo apt-get install python3-pip  
pip install -r requirements.txt

mkdir ~/.ssh  
chmod 700 ~/.ssh  
ssh-keygen -t rsa  

sudo add-apt-repository ppa:picaso/octave
sudo apt-get update ; sudo apt-get install octave


python3 ./server.py 
