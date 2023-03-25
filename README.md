# GarageMonitor
---

This project uses a web server on an ESP32 microcontroller to report specific sensor data to any local device that asks for it. Namely, air quality and flood sensor data.

This project is very specific to the developer's hardware and sensor needs, but of course you can use and adapt this code for your own educational or informational purpose.

The user should not expect this project to protect lives or property from unsafe air or water. There are commercial products you can purchase if you are looking for a safety device. This project is for people who want to have a nice time with hobby electronics, and nothing more.

This project is not sufficient to calculate AQI. See [airnow.gov](https://www.airnow.gov) for details.

---

## Sensors

### Flood sensor
When a driveway drain is clogged with debris, excess rainwater can start to pool up near the garage door and can potentially damage property.

### CO sensor
CO levels should be monitored near where internal combustion engines are used or stored. Excess exposure can cause injury or death.

Recommended exposure limits for CO are typically averaged out over a period of hours, and is not a metric this project will tackle. In general, According to CPSC, symptoms from CO exposure begin at about 70ppm.


### NO2 sensor
NO2 levels should be monitored near where internal combustion engines are used or stored. Excess exposure can cause injury but is rarely fatal.

NIOSH recommends an airborne exposure limit of 1ppm.

---

## API
| URI                | Method | Notes 
| ---                | ---    | ---   
| /api/flood         | GET    | returns current flooded state true/false
| /api/flood/history | GET    | returns timestamped recent flood events
| /api/co            | GET    | returns current CO numerical reading
| /api/co/history    | GET    | returns timestamped recent CO danger events
| /api/no2           | GET    | returns current NO2 numerical reading
| /api/no2/history   | GET    | returns timestamped recent NO2 danger events
