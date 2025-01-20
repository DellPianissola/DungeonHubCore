# DungeonHub Core

This repository contains the back-end development of an online platform for managing and organizing RPG sessions, built with **Python** and **Django Rest Framework (DRF)**.

## Project Description

The platform aims to provide a collaborative and user-friendly environment for RPG players and game masters. Key features include:

- **Session Management:** Create and manage RPG sessions with support for multiple rule systems.
- **Character Management:** Handle playable characters and NPCs with centralized information.
- **Real-Time Updates:** Asynchronous synchronization so all participants can see updates instantly.

## Technologies Used

- **Language:** Python
- **Framework:** Django Rest Framework (DRF)
- **Database:** PostgreSQL

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/DellPianissola/DungeonHubCore.git
   ```

2. Navigate to the project directory:
   ```bash
   cd repository-name
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure the environment variables in the `.env` file (example available in `.env.example`).

6. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Contact

For questions or suggestions, reach out:

- **Email:** Dell.pianissola@outlook.com
- **LinkedIn:** [Gabriel N Pianissola](https://www.linkedin.com/in/gabriel-n-pianissola/)
