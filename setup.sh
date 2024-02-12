#! /bin/sh
echo "installation started"
cd ~
sudo apt install python3.9
python3.9 -m venv search_env
echo "search_env path"
pwd
cd /root/Zania-ChatBot/
/root/search_env/bin/python3.9 -m pip install -r requirements.txt
git lfs install
mkdir -p logs
mkdir -p models
cd /root/Zania-ChatBot/models
git clone https://huggingface.co/BAAI/bge-reranker-base
git clone https://huggingface.co/BAAI/bge-small-en-v1.5
echo "installation complete"