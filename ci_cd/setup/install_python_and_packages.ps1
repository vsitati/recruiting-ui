# Install python
choco install -y python --version=3.10

# Refresh path
# refreshenv

# Update pip
python -m pip install --upgrade pip

# Install python packages
pip install -r ./requirements.txt
