# ZK Compression Cost Visualizer

A web application built for the 1000x Breakout Hackathon to visualize rent cost savings of ZK Compression compared to regular Solana accounts. This tool helps developers understand the cost-efficiency of using compressed accounts on the Solana blockchain, leveraging Django, MySQL, Chart.js, and Tailwind CSS for a modern, user-friendly interface.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

## Overview

The ZK Compression Cost Visualizer is a submission for the ZK Compression track of the 1000x Breakout Hackathon, sponsored by Light Protocol, Helius, and the Solana Foundation. It calculates and visualizes the rent costs for compressed accounts versus regular Solana accounts, demonstrating the scalability benefits of ZK Compression. Users input the number of accounts, view a dynamic bar chart comparing costs, and track calculation history stored in a MySQL database. The app features a professional UI with Tailwind CSS, social links, and a footer with hackathon resources.

## Features

-   **Cost Calculation:** Computes rent costs for regular and compressed Solana accounts based on user-input account counts.
-   **Dynamic Visualization:** Displays cost comparisons using Chart.js bar charts.
-   **Persistent History:** Stores calculation history in a MySQL database, displayed in a responsive table.
-   **Modern UI/UX:** Built with Tailwind CSS for a clean, professional design, including a description section and footer.
-   **Social Integration:** Includes links to X, Telegram, and GitHub with Font Awesome icons.
-   **Hackathon Compliance:** Uses ZK Compression cost data (approximated from ZK Compression Docs) to meet eligibility requirements.

## Tech Stack

-   **Backend:** Python 3.11, Django 5.1
-   **Database:** MySQL 8.0 (via PyMySQL)
-   **Frontend:** HTML, Tailwind CSS (CDN), JavaScript, Chart.js (CDN), Font Awesome (CDN)
-   **Deployment:** Railway, Gunicorn, WhiteNoise
-   **Version Control:** Git, GitHub

## Prerequisites

-   Python 3.11
-   MySQL 8.0
-   Git
-   Railway account (for deployment)
-   Solana CLI (optional, for real blockchain integration)

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/hack3rvirus/ZK-Compression-Cost-Visualizer.git](https://github.com/hack3rvirus/ZK-Compression-Cost-Visualizer.git)
    cd ZK-Compression-Cost-Visualizer
    ```

2.  **Set Up Virtual Environment:**
    ```bash
    python -m venv .venv
    ```
    Activate the environment:
    -   On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure MySQL:**
    * Create a MySQL database (e.g., `hackathon_db`):
        ```sql
        CREATE DATABASE hackathon_db;
        ```
    * Update `hackathon/settings.py` with your MySQL credentials:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'hackathon_db',         
                'USER': 'my_mysql_username',
                'PASSWORD': 'my_mysql_password',
                'HOST': 'localhost',            
                'PORT': '3306',                  
            }
        }
        ```

5.  **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Collect Static Files:**
    ```bash
    python manage.py collectstatic
    ```

7.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    Visit `http://127.0.0.1:8000/` in your browser to access the app.

## Usage

1.  **Input Accounts:** Enter the number of accounts in the input field (e.g., `100`).
2.  **Calculate:** Click the "Calculate" button to compute the costs.
3.  **View Results:**
    * A Chart.js bar chart will dynamically display the cost comparison between regular and compressed Solana accounts.
    * The history table below the chart will show all previous calculations, which are persistently stored in the MySQL database.
4.  **Explore:** Read the "About" section for more context on ZK Compression and the project. Check the footer for links to hackathon resources and social media profiles.

## Deployment

The application is configured for deployment on Railway. The example deployment URL is `https://your-app.up.railway.app`. To deploy your own instance:

1.  **Push to GitHub:**
    Ensure your code, including `Procfile`, `railway.json`, and `runtime.txt`, is pushed to a public or private GitHub repository.

2.  **Set Up Railway Project:**
    * Create a new project in Railway.
    * Link your GitHub repository to this Railway project.
    * Add a MySQL database service from the Railway marketplace. Railway will provide a `DATABASE_URL`.
    * Configure the following environment variables in your Railway project settings:
        ```env
        DJANGO_SECRET_KEY=your_strong_unique_secret_key_here
        DEBUG=False
        ALLOWED_HOSTS=your-app-name.up.railway.app,localhost,127.0.0.1
        DATABASE_URL=mysql://user:password@host:port/dbname # Provided by Railway MySQL service
        ```

3.  **Configuration Files (ensure these are in your repository):**
    * **`Procfile`**: Defines the processes for your application.
        ```
        web: gunicorn hackathon.wsgi --log-file -
        release: python manage.py migrate
        ```
    * **`railway.json`**: (Optional, Railway often auto-detects settings but can be used for explicit configuration)
        Specifies build and deployment commands if needed beyond Nixpacks/Buildpacks defaults.
        Example (may vary based on Railway's detection):
        ```json
        {
          "$schema": "[https://railway.app/railway.schema.json](https://railway.app/railway.schema.json)",
          "build": {
            "builder": "NIXPACKS",
            "nixpacksConfig": {
              "startCommand": "gunicorn hackathon.wsgi --log-file -"
            }
          },
          "deploy": {
            "startCommand": "gunicorn hackathon.wsgi --log-file -",
            "healthcheckPath": "/",
            "restartPolicyType": "ON_FAILURE",
            "restartPolicyMaxRetries": 10
          }
        }
        ```
    * **`runtime.txt`**: Specifies the Python version for Railway.
        ```
        python-3.11.9
        ```

4.  **Deploy:**
    * Railway typically automatically deploys your application when you push changes to the linked GitHub branch.
    * The `release` command in the `Procfile` should run database migrations. If not, you may need to run them manually via the Railway CLI or dashboard shell: `python manage.py migrate`.

## Project Structure

ZK-Compression-Cost-Visualizer/
├── hackathon/                # Django project directory
│   ├── init.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Root URLs
│   ├── wsgi.py               # WSGI config
│   └── asgi.py               # ASGI config
├── cost_visualizer/          # Django app directory
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/           # Database migrations
│   │   └── init.py
│   ├── models.py             # CostHistory model
│   ├── static/               # App-specific static files
│   │   └── cost_visualizer/
│   │       └── (e.g., custom.css, chart_config.js)
│   ├── templates/            # HTML templates
│   │   └── cost_visualizer/
│   │       └── index.html
│   ├── tests.py
│   ├── urls.py               # App URLs
│   └── views.py              # Cost calculation logic and views
├── .gitignore                # Specifies intentionally untracked files
├── manage.py                 # Django management script
├── Procfile                  # Railway process configuration
├── railway.json              # Railway deployment configuration (optional if auto-detected)
├── requirements.txt          # Python dependencies
├── runtime.txt               # Python version for PaaS
└── README.md                 # This file

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature/your-amazing-feature`).
3.  Make your changes and commit them (`git commit -m 'Add some amazing feature'`).
4.  Push to the branch (`git push origin feature/your-amazing-feature`).
5.  Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file (you'll need to create this file if it doesn't exist) for details.

## Credits

-   **Developer:** [Frank Oge]
    -   X (Twitter): `[https://x.com/blackhatVIRUS]` 
    -   Telegram: `[https://t.me/HACK3RVIRUS]` 
    -   GitHub: `[https://github.com/hack3rvirus]` 
-   **Hackathon:** 1000x Breakout Hackathon
-   **Resources & Inspiration:**
    -   ZK Compression Docs (Link to actual docs if available)
    -   Light Protocol GitHub (Link to Light Protocol GitHub if available)
    -   Solana Foundation Rules (Link to rules if available)
-   **Tools Used:**
    -   Django
    -   MySQL
    -   Chart.js
    -   Tailwind CSS
    -   Font Awesome
    -   Railway
