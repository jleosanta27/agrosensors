# Configuration
- Install arduino
- add the url: https://github.com/Heltec-Aaron-Lee/WiFi_Kit_series/releases/download/0.0.7/package_heltec_esp32_index.json

- go to board manager and install heltec esp32

open the terminal an run the following
```bash
mv ~/.arduino15/packages/Heltec-esp32/tools/esptool_py/3.3.0 ~/.arduino15/packages/Heltec-esp32/tools/esptool_py/3.3.0.bak
wget https://github.com/espressif/esptool/archive/refs/tags/v4.6.1.zip
unzip v4.6.1.zip
rm v4.6.1.zip
mv esptool-4.6.1 ~/.arduino15/packages/Heltec-esp32/tools/esptool_py/3.3.0
```