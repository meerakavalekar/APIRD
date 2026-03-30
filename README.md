# APIRD# 🍃 MongoDB Drinks API

A simple REST API built using MongoDB to manage drinks data. This project demonstrates CRUD operations with a NoSQL database and basic API structure.

---

## 🚀 Features

- Create, Read, Update, Delete (CRUD) operations
- MongoDB database integration
- Lightweight and fast API
- JSON-based data handling
- Scalable NoSQL design

---

## 🛠️ Tech Stack

- Node.js / Python (depending on your implementation)
- MongoDB
- Express.js / Flask (if applicable)
- Mongoose / PyMongo

---

## 📁 Project Structure

APIMONGODB/
│── models/            # Database schema/models  
│── routes/            # API routes  
│── controllers/       # Business logic  
│── config/            # Database connection  
│── app.js / main.py   # Entry point  
│── package.json / requirements.txt  

---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone <your-repo-link>  
cd APIMONGODB  

### 2. Install dependencies
For Node.js:
npm install  

For Python:
pip install -r requirements.txt  

### 3. Start MongoDB
Make sure MongoDB is running locally:
mongod  

### 4. Run the server
For Node.js:
npm start  

For Python:
python main.py  

---

## 🌐 API Endpoints

| Method | Endpoint        | Description         |
|--------|----------------|---------------------|
| GET    | /drinks        | Get all drinks      |
| GET    | /drinks/:id    | Get single drink    |
| POST   | /drinks        | Add new drink       |
| PUT    | /drinks/:id    | Update drink        |
| DELETE | /drinks/:id    | Delete drink        |

---

## 📦 Example JSON

{
  "_id": "64f1a2b3c4d5e6f7",
  "name": "Pepsi",
  "description": "Cold beverage"
}

---

## 🔗 MongoDB Connection Example

mongodb://127.0.0.1:27017/drinksDB  

---

## 🧪 Testing

npm test  
or  
python -m unittest  

---

## 📌 Future Improvements

- Add authentication (JWT)
- Add validation & error handling
- Deploy using Docker
- Add API documentation (Swagger)

---

## 🧑‍💻 Author

- Your Name  

---

## 📜 License

This project is open-source and free to use.
