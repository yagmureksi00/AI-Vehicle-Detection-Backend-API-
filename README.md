# AI-Based Vehicle Detection & Monitoring System - Backend API

## 📖 Project Description
This repository hosts the **Backend API infrastructure** for a real-time vehicle detection system. The project is designed to bridge the gap between an **AI-powered computer vision unit** and a **mobile monitoring application**.

The system processes vehicle data (images, types, tracking IDs, and timestamps) detected by edge devices and synchronizes this information with mobile clients instantly using **WebSocket** technology, while simultaneously logging historical data into a **MySQL database**.

## 🏗️ System Architecture & Workflow

The backend acts as the central nervous system of the project, managing data flow in two directions:

1.  **Ingestion (REST API):** The AI/Camera unit sends HTTP POST requests containing vehicle metadata and Base64-encoded images to the server.
2.  **Broadcasting (WebSocket):** The server processes this data and pushes real-time notifications to connected mobile applications without requiring page refreshes.
3.  **Persistence (MySQL):** All traffic data is structured and stored for future reporting and statistical analysis.

## 🚀 Key Features

* **Hybrid Communication Protocol:** Implements both **REST API** (for AI data ingestion) and **WebSocket** (for real-time client updates).
* **Real-Time Image Transmission:** Handles high-volume Base64 image strings to display vehicle snapshots on mobile devices instantly.
* **Persistent Logging:** detailed logging of vehicle types, unique tracking IDs, detection timestamps, and camera sources using **SQLAlchemy ORM**.
* **Dynamic Statistics:** Provides endpoints for fetching total vehicle counts and recent activity logs.

## 🛠️ Tech Stack

* **Framework:** FastAPI (Python)
* **Database:** MySQL / SQLAlchemy
* **Protocol:** HTTP & WebSocket
* **Data Validation:** Pydantic
* **Server:** Uvicorn (ASGI)

## 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/detect` | Receives vehicle data (ID, Type, Image) from the AI unit. |
| `WS` | `/ws` | WebSocket channel for real-time mobile app communication. |
| `GET` | `/api/stats` | Returns total vehicle count and recent logs. |
| `DELETE`| `/api/delete/{id}` | Removes an erroneous entry from the database. |