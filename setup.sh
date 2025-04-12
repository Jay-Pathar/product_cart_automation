# !/bin/bash
python3 -m venv ../env
source ../env/bin/activate
pip install -r requirements.txt

export LT_USERNAME="jhanvipathar19"
export LT_ACCESS_KEY="LT_kO094ug1C9tIWGoAQHy6qjJfuUqZcUPholGjZOvMDnWUxnH"

alias runSeq='pytest tests/test_amazon_cart.py '
alias runParallel='pytest tests/test_amazon_cart.py -s -v -n 2' 


