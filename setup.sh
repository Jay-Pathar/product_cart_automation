# !/bin/bash
python3 -m venv ../env
source ../env/bin/activate
pip install -r requirements.txt

export LT_USERNAME="patharjay20"
export LT_ACCESS_KEY="LT_khlHTTfml8bdWEKsEKrimss8wz8kLqNnzdCAx5HrOYR9s2t"

alias runSeq='pytest tests/test_amazon_cart.py '
alias runParallel='pytest tests/test_amazon_cart.py -s -v -n 2' 


