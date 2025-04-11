## SpendWise - ML-powered FinTech Platform

SpendWise is a secure and intelligent personal finance management platform that combines machine learning, fraud detection, and a chatbot interface. Built using React, Flask, MongoDB, and scikit-learn, it offers users a comprehensive solution for expense tracking, fraud prevention, and financial assistance.

---

### Features

- Full-stack expense tracking and management
- Fraud detection module using Random Forest (92% accuracy)
- Financial assistant chatbot powered by OpenAI API
- Add, update, and filter expenses
- Real-time insights through interactive charts and recommendations
- Secure and scalable backend integration

---

### Screenshots

| ![Screenshot 1](https://github.com/user-attachments/assets/5021e3aa-7a6c-41c7-ad55-c96e8c75d579) | ![Screenshot 2](https://github.com/user-attachments/assets/da40f799-bfe0-4a8f-b819-b1e97ddec293) | ![Screenshot 3](https://github.com/user-attachments/assets/232a9007-de9b-4df0-87a4-35b9ceefdc75) |

---

### Tech Stack

- Frontend: React.js, Bootstrap, Axios
- Backend: Flask (Python)
- Machine Learning: scikit-learn (Random Forest)
- Database: MongoDB
- AI Integration: OpenAI API (Chatbot)

---

### Setup Instructions

#### 1. Clone the Repository
```bash
git clone https://github.com/lalithya-k/my-spend-wise.git
cd my-spend-wise
```

#### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### 3. Frontend Setup
```bash
cd ../frontend
npm install
```

#### 4. Configure Environment Variables
Create a `.env` file in the backend directory with the following content:
```
MONGODB_URI=your_mongo_db_connection_string
OPENAI_API_KEY=your_openai_api_key
SECRET_KEY=your_flask_secret_key
```

#### 5. Start the Application
```bash
# In the backend directory
flask run

# In the frontend directory (use a separate terminal)
npm start
```

The app will run at `http://localhost:3000`

---


