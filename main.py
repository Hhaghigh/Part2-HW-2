# Clone the repository
git clone git@github.com:LittleYUYU/Gentopia-Mason.git
cd Gentopia-Mason

# Create a conda virtual environment
conda create --name gentenv python=3.10
conda activate gentenv
pip install -r requirements.txt

# Set up global environment
export PYTHONPATH="$PWD/Gentopia:$PYTHONPATH"

# Set up OpenAI API key
cd GentPool
touch .env
echo "OPENAI_API_KEY=<your_openai_api_key>" >> .env
