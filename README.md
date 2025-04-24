# AI Financial Advisor Dashboard

A modern, AI-powered financial dashboard built with Dash and Python that provides personalized investment advice, portfolio management, and real-time market insights.

## Features

- **Personalized Investment Planning**
  - AI-driven portfolio optimization
  - Custom investment goals analysis
  - Risk assessment and recommendations

- **Portfolio Dashboard**
  - Real-time portfolio performance tracking
  - Asset allocation visualization
  - Risk metrics and diversification analysis
  - Performance charts and metrics

- **Live Market Data**
  - Real-time stock price tracking
  - Live trade monitoring
  - Market sentiment analysis

- **News Tracker**
  - Financial news aggregation
  - Market sentiment analysis
  - AI-powered news insights

- **AI Insights**
  - Portfolio analysis and recommendations
  - Market sentiment analysis
  - Risk assessment and opportunities

## Prerequisites

- Python 3.7+
- SingleStore database
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd finance_demo
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
host=your_singlestore_host
port=your_singlestore_port
user=your_singlestore_user
password=your_singlestore_password
database=your_database_name
anthropic_api_key=your_anthropic_api_key
news_api_key=your_news_api_key
openai_api_key = your_openai_api_key
```

## Running the Application

1. Start the Dash application:
```bash
python dash_app.py
```

2. Open your web browser and navigate to:
```
http://localhost:8050
```

## Project Structure

```
finance_demo/
├── dash_app.py              # Main application file
├── components/             # UI components
│   ├── portfolio.py
│   ├── news.py
│   └── charts.py
├── services/              # Business logic services
│   ├── stock_service.py
│   ├── news_service.py
│   └── ai_service.py
├── utils/                 # Utility functions
│   └── data_utils.py
├── requirements.txt       # Python dependencies
└── .env                  # Environment variables
```

## Features in Detail

### Portfolio Management
- View and analyze your investment portfolio
- Track performance metrics
- Monitor asset allocation
- Get AI-powered recommendations

### Live Market Data
- Real-time stock price tracking
- Live trade monitoring
- Market sentiment analysis
- Customizable ticker selection

### AI-Powered Insights
- Portfolio analysis
- Risk assessment
- Market sentiment analysis
- Investment recommendations

### News Tracking
- Financial news aggregation
- Market sentiment analysis
- AI-powered news insights

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Dash and Plotly for the visualization framework
- SingleStore for the database
- Various financial data providers
