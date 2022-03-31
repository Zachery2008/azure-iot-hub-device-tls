# Simulate Device - IoT Hub TLS Connection with New DigiCert Global Root G2 Certificate

### Prerequisite 
- python 
- pip

### Reference: 
1. [IoT Hub and DPS CA change in June 2022](https://techcommunity.microsoft.com/t5/internet-of-things-blog/azure-iot-tls-critical-changes-are-almost-here-and-why-you/ba-p/2393169#:~:text=The%20time%20has%20come%20now,does%20not%20impact%20sovereign%20clouds.)
2. [Device client simulator](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support)

In `certs` folder, there are 2 root CA certificates: `BaltimoreCyberTrustRoot.crt.pem` and `DigiCertGlobalRootG2.crt.pem`. `BaltimoreCyberTrustRoot.crt.pem` is currently used by IoT Hub and DPS, but it will be retired after June - October 2022. `DigiCertGlobalRootG2.crt.pem` will be the new root CA. 

In simulation, the IoT Hub `g2cert.azure-devices.net` provided by Azure uses `DigiCertGlobalRootG2.crt.pem` only. The script `src/device_client.py` simulate the device connection to IoT Hub. Run the command `python3 ./src/device_client.py`, you will see the logs that device successfully connected to IoT Hub. 

To test the negate case, please comment out line 9 and uncomment line 8 of the script, and rerun the command `python3 ./src/device_client.py`, which uses `BaltimoreCyberTrustRoot.crt.pem` certificate. You will see error `[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed`. 