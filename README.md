# 🛒 Amazon Cart Automation

A Selenium-based automation script to search, select, and add Amazon products to the cart — with support for captcha solving, location configuration, and price extraction.

---

### 🔁 End-to-End Product Workflow
- Executes a full automated workflow:
  - 🛒 Opens `amazon.com`
  - 🔐 Handles captchas
  - 📍 Sets location
  - 🔍 Searches and selects the product
  - ➕ Adds to cart
  - ❌ Skips extra offers
  - 📝  Logs the final price

---

## 🧰 Key Dependencies

- `selenium`: v4.27.1
- `pytest`: v8.3.5
- `pytest-xdist`: v3.6.1
- `amazoncaptcha`: v0.5.11

## 🛠️ Installation and Setup

Add your LambdaTest credentials to `setup.sh`, then execute the below command to install dependencies:
```bash
source setup.sh
```

## Running the Automation

Run one of the following commands in the terminal based on your preference:

- For sequential execution:

    ```bash
    runSeq
    ```

- For parallel execution:

    ```bash
    runParallel
    ```

