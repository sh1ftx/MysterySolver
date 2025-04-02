# MysterySolver Game

## Overview
MysterySolver is an interactive game that challenges players to solve mysteries through clues and puzzles. This project utilizes Python for the backend, SQLite for data storage, and HTML/CSS/JavaScript for the frontend.

## Project Structure
```
MysterySolver
├── controllers
│   └── __init__.py
├── database
│   ├── mystery_solver.db
│   └── __init__.py
├── views
│   ├── templates
│   │   └── index.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── main.py
└── README.md
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd MysterySolver
   ```

2. **Install dependencies**:
   Ensure you have Python installed. You may need to install Flask or any other required libraries. Use the following command:
   ```
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   The SQLite database is located in the `database` directory. You can initialize it with the necessary tables and data as needed.

4. **Run the Application**:
   Start the application by running:
   ```
   python main.py
   ```

5. **Access the Game**:
   Open your web browser and navigate to `http://localhost:5000` to start playing the MysterySolver game.

## Usage
Follow the on-screen instructions to navigate through the game, solve puzzles, and uncover the mystery.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.