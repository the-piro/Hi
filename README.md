# Mega Links Checker Bot

A Telegram bot to check MEGA.nz links displays file/folder names, sizes, lists files and folders in with log channel support.


## Deployment Guide

<details>
  <summary><strong>Heroku (One-Click Deploy)</strong></summary>

  1. **Fork this repo**
  2. **Click:**  
      <a href="https://heroku.com/deploy?template=https://github.com/XalFH/Mega-Links-Checker">
        <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" />
      </a>
  3. **Fill required vars:**  
      - `BOT_TOKEN`  
      - `API_ID`  
      - `API_HASH`
  4. **Deploy and run!**

</details>

<details>
  <summary><strong>VPS / Locally</strong></summary>

  1. **Clone the repository:**
      ```sh
      git clone https://github.com/XalFH/Mega-Links-Checker.git
      cd Mega-Links-Checker
      ```

  2. **Install dependencies:**
      ```sh
      pip install -r requirements.txt
      ```

  3. **Configure bot:**
      - Edit `config.py` with your Telegram API ID, HASH, & BOT TOKEN.

  4. **Run the bot:**
      ```sh
      python3 main.py
      ```

</details>
