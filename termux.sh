cd
pkg update
pkg upgrade
pkg install git
pkg install pip
pkg install python
git clone https://github.com/x11-repo/jamspymer.git
pip install -r requirements.txt
cd ~/JamSpymer
python JamSpymer.py
