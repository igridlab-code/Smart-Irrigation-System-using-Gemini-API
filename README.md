# 🌱 Smart Irrigation System using Gemini AI

## 📌 Project Overview

Our Smart Irrigation System is an AI-based automatic irrigation system that monitors plant and soil/root conditions using a Seeed Studio XIAO ESP32S3 Sense camera.

The camera captures an image of the plant/soil area and sends the image through Wi-Fi for Gemini AI analysis. Gemini AI analyses the captured image and determines whether the observed condition is **Dry or Wet**.

If the condition is detected as **Dry**, the system activates the relay, which turns ON the water pump and supplies water to the plant. If the condition is **Wet**, the water pump remains OFF.

---

## ❗ Problem Statement

Traditional irrigation methods often depend on manual monitoring or fixed watering schedules. This can lead to unnecessary water usage and difficulty in continuously monitoring plant conditions.

---

## 🎯 Aim

The aim of this project is to develop an AI-powered smart irrigation system that uses camera-based monitoring and Gemini AI analysis to determine when irrigation is required and automatically control the water supply.

---

## 💡 Proposed Solution

Our proposed system combines **AI, IoT, Computer Vision and automated irrigation**.

A Seeed Studio XIAO ESP32S3 Sense camera captures the plant/soil image. The image is sent through Wi-Fi to the Gemini API for analysis.

Gemini AI determines whether the observed condition is **Dry or Wet**.

- **Dry → Relay ON → Water Pump ON → Irrigation**
- **Wet → Relay OFF → Water Pump OFF**

---

## 🏗️ System Architecture & Flowchart

![Smart Irrigation System Block Diagram and Flowchart](block%20diagram.png)

The diagram shows the complete system architecture and working flow from image capture and Gemini AI analysis to automatic irrigation.

---

## 🔄 Working Process

1. 📷 Camera captures the plant/soil image.
2. ⚙️ Seeed Studio XIAO ESP32S3 Sense handles the camera and system control.
3. 📡 The image is sent through Wi-Fi.
4. 🤖 Gemini AI analyses the captured image.
5. 🔍 AI determines whether the condition is **Dry or Wet**.
6. 💧 If Dry → Relay turns ON → Water Pump turns ON.
7. 🌱 Water is supplied to the plant.
8. 🛑 If Wet → Relay remains OFF → Water Pump remains OFF.
9. 🔁 The process can be repeated for continuous monitoring.

---

## 🔧 Hardware Components

- Seeed Studio XIAO ESP32S3 Sense
- Camera
- Servo Motor
- Relay Module
- Water Pump
- Battery
- Switch
- Water Pipe / Nozzle

- ## 🔌 Hardware Connections

| Component                  | Component Pin  | XIAO ESP32S3 Sense Connection | Status      |
| -------------------------- | -------------- | ----------------------------- | ----------- |
| **OV2640 Camera**          | Onboard Camera | Built into XIAO ESP32S3 Sense | ✅ Connected |
| **SG90 Servo Motor**       | Signal         | **D2 / GPIO3**                | ✅ Connected |
| **SG90 Servo Motor**       | VCC            | **5V**                        | ✅ Connected |
| **SG90 Servo Motor**       | GND            | **GND**                       | ✅ Connected |
| **1-Channel Relay Module** | IN             | **D1 / GPIO2**                | 🔄 Planned  |
| **1-Channel Relay Module** | VCC            | **5V**                        | 🔄 Planned  |
| **1-Channel Relay Module** | GND            | **GND**                       | 🔄 Planned  |
| **Water Pump**             | Positive (+)   | Relay **NO**                  | 🔄 Planned  |
| **Water Pump**             | Negative (−)   | External Power Supply −       | 🔄 Planned  |

### 📷 Camera

The OV2640 camera is integrated into the Seeed Studio XIAO ESP32S3 Sense and is used to capture plant/soil images.

### ⚙️ Servo Motor

The SG90 servo motor is connected to **D2 / GPIO3** and is used to move the camera to different positions.

### 🔴 Relay Module

The relay is planned to be connected to **D1 / GPIO2**. It will be used to control the water pump.

### 💧 Water Pump

The water pump will be controlled through the relay. The pump should use a suitable external power supply rather than drawing its operating current directly from an ESP32 GPIO pin.

> **Note:** Relay and pump connections are marked as **Planned** because they have not yet been physically connected and tested.


---

## 💻 Software & Technologies

- Gemini API
- Python
- AI Image Analysis
- IoT
- Computer Vision
- Embedded Programming
- Mobile Application

---

## 📱 Mobile Application

### 📷 Live Camera – Seed Studio Camera

<img width="720" height="1600" alt="WhatsApp Image 2026-08-19 at 12 57 08 PM" src="https://github.com/user-attachments/assets/a89571b3-51b7-41f6-a84e-3d023e3527df" />

### 🌱 Choose Image Source

<img width="720" height="1600" alt="WhatsApp Image 2026-08-19 at 12 57 07 PM (2)" src="https://github.com/user-attachments/assets/bcac9e5f-c351-4c58-b3f9-224fc1b04c1d" />

### 📊 Scan History

<img width="720" height="1600" alt="WhatsApp Image 2026-08-19 at 12 57 07 PM (1)" src="https://github.com/user-attachments/assets/c8320208-ca0b-45a7-b6e1-b69f5309905e" />

### 🤖 AI Analysis – Gemini AI

<img width="720" height="1600" alt="WhatsApp Image 2026-08-19 at 12 57 06 PM" src="https://github.com/user-attachments/assets/ae2f2765-07dc-4cb2-82a3-7c86bf8120f6" />
<img width="720" height="1600" alt="WhatsApp Image 2026-08-19 at 12 57 06 PM (1)" src="https://github.com/user-attachments/assets/a8e941f4-5eab-4933-8f75-f01c14f57779" />

The mobile application provides a user-friendly interface for monitoring the smart irrigation system.

The application is intended to display:

- Plant condition
- AI Dry/Wet analysis
- Irrigation status
- Water pump status
- Camera monitoring information

---

## ⭐ Key Features

- AI-based plant condition analysis
- Automatic irrigation
- Camera-based monitoring
- Gemini API integration
- Relay-controlled water pump
- Servo motor camera positioning
- Mobile application monitoring
- Reduced unnecessary water usage
- Minimizes manual intervention

---

## 🎯 Advantages

- 💧 Helps reduce unnecessary water usage
- 🤖 AI-based irrigation decision
- 📷 Camera-based plant monitoring
- ⚙️ Automatic pump control
- 📱 Mobile monitoring
- 🌱 Suitable for smart agriculture applications

---

## 🔮 Future Enhancements

- Multiple plant monitoring
- Real-time notifications
- Water-level monitoring
- Weather API integration
- Cloud-based plant monitoring
- Plant disease detection
- Advanced mobile application features

---

## 📂 Project Structure

```text
Smart-Irrigation-System-using-Gemini-API/
│
├── README.md
├── block diagram.png
│
├── camera/
│   └── camera_code
│
├── gemini-ai/
│   ├── gemini_analysis.py
│   └── requirements.txt
│
├── mobile-app/
│   └── mobile application source code
│
└── hardware/
    ├── circuit-diagram
    └── project-images
