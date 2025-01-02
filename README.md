# CaiClone

CaiClone is a Django-based web application designed to replicate the core functionalities of a popular platform. This project aims to provide a robust and scalable solution for users looking to create a similar service.

## Features

- User authentication and authorization
- Profile management
- Content creation and management
- Real-time notifications
- Responsive design

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CaiClone.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CaiClone
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Apply migrations:
   ```bash
   python manage.py migrate
   ```
7. Run ollama server on port 10273:
   ```bash
   OLLAMA_HOST=127.0.0.1:10273 ollama serve
   ```
8. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. Register a new account or log in with existing credentials.
3. Explore the features and functionalities of CaiClone.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact [your email address].
