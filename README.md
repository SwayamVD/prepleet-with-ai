# Flask API App Structure

flask_api_app/
│
├── app/
│ ├── **init**.py # Flask app factory
│ ├── routes/
│ │ ├── **init**.py
│ │ ├── questions.py # /questions endpoints
│ │ ├── analyze.py # /analyze, /gotstuck endpoints
│ │ ├── leetcode.py # /solve, /getquestionset endpoints
│ │ └── misc.py # testpage, home
│ ├── services/
│ │ ├── question_loader.py # load CSVs
│ │ ├── leetcode_api.py # GraphQL queries
│ │ └── ai_service.py # Google Gemini integration
│ ├── templates/ # Your HTML templates
│ └── static/ # CSS, JS, etc.
│
├── questions/ # Your CSV files
│
├── config.py # Configurations (API keys, env vars)
├── run.py # Entry point
├── requirements.txt
└── README.md

## Companies included

------------Non-Indian---------------
Accenture (Ireland) – ~700k employees
IBM (USA) – ~288k employees
Capgemini (France) – ~360k employees
Cognizant (USA) – ~350k employees
DXC Technology (USA) – ~130k employees
---------Indian IT Giants--------------
TCS – ~600k employees
Infosys – ~335k employees
Wipro – ~250k employees
HCLTech – ~225k employees
Tech Mahindra – ~150k employees
