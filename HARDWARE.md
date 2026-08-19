# Hardware Connections

## 📷 Camera

The onboard OV2640 camera is integrated with the
Seeed Studio XIAO ESP32S3 Sense.

It is used to capture plant and soil images.

## ⚙️ Servo Motor

The SG90 servo motor is used for camera movement.

| Servo Pin | Connection |
|---|---|
| Signal | D2 / GPIO3 |
| VCC | 5V |
| GND | GND |

## 🔴 Relay Module

The relay will be used to control the water pump.

| Relay Pin | Planned Connection |
|---|---|
| IN | D1 / GPIO2 |
| VCC | 5V |
| GND | GND |

## 💧 Water Pump

The water pump will be controlled through the relay.

| Relay Terminal | Connection |
|---|---|
| COM | External power positive |
| NO | Pump positive |
| Pump negative | External power negative |

> The relay and pump connections should be tested before final deployment.

## 🔋 Power Supply

A suitable external power supply is used for the pump.
The XIAO, servo and relay require an appropriate regulated
power source.

## 📐 Hardware Setup

The XIAO ESP32S3 Sense, servo motor, relay and water pump
are assembled as part of the smart irrigation prototype.
