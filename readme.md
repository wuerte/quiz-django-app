# Quiz App

## About the Project

This is a quiz app project built for educational purposes. The project includes the following functionalities:

- Single-player mode with random unique questions in each game
- High score classification
- Recent games list in the main menu
- Form for adding new questions

## Installation

To get started with the project, follow these steps:

1. Clone the repository.
2. Navigate to the `quiz-django/` directory.
3. Create a virtual environment:
    ```
    python3 -m venv your_venv
    ```
4. Activate the virtual environment:
    - For Linux/Mac:
        ```
        source your_venv/bin/activate
        ```
    - For Windows (Command Prompt):
        ```
        your_venv\Scripts\activate.bat
        ```
5. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
6. Go to the `quiz_django/` directory.
7. Run the server:
    ```
    python3 manage.py runserver
    ```
   - To run the server in the background, use:
     ```
     nohup python manage.py runserver 0.0.0.0:8000 &
     ```
   - To stop the server running in the background, use:
     ```
     tail -f nohup.out
     ps aux | grep runserver
     ```
     or:
     ```
     pkill -f runserver
     ```

## Dependencies

The project requires the following dependencies:
asgiref==3.6.0
Django==4.1.7
psycopg2-binary==2.9.5
sqlparse==0.4.3

## About the Author

My name is Radosław Wierzgała. I am a programmer since the beginning of 2023, with a background in electrical engineering from my bachelor's degree and a technical high school diploma in computer science. Currently, I am primarily focused on Python in web development and data science. I have a keen interest in exploring new technologies, the automotive industry, and trekking.

Feel free to connect with me and explore my projects on GitHub. If you have any questions or would like to collaborate, don't hesitate to reach out.

Thank you for visiting my project!