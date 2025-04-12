# !/bin/bash
python3 -m venv ../env
source ../env/bin/activate
pip install -r requirements.txt

# Add your LambdaTest credentials below
export LT_USERNAME=""  # ADD LAMBDATEST USERNAME
export LT_ACCESS_KEY=""  # ADD LAMBDATEST ACCESS KEY

alias runSeq='pytest tests/test_amazon_cart.py '
alias runParallel='pytest tests/test_amazon_cart.py -s -v -n 2' 


