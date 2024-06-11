# agrosensors

# Collections
The structure defined for the BD consists in 4 collections: records, recordsxdev, sensors, nodes.

## records collection
- _id: id record
- ts: timestamp

## recordsxdev collection
- _id: id record
- id_dev: id device
- type_dev: device type (sensor or node)
- sent: indicates if the register was sent

## sensors
- _id: id record
- id_dev: id device
- moisture: percentage of moisture sensed
- temp: temperature in celsius

## nodes
- _id: id record
- id_dev: id device
- soc: state of charge for the battery node
- cpu_temp: temperature of the cpu device

# Installation

## Install Docker
- sudo curl -sSL https://get.docker.com | sh
- sudo usermod -aG Docker [user]

## get MongoDB 4.0 image (compatible with ARM8.0A)
- sudo docker pull mongo:4.0

## run the image
- sudo docker run -d -p 2717:27017 -v ~[path] --name mongodb --restart always mongo:4.0

## More info to install mongodb (versión compatible with ARMV8)
- MongoDB - ARM64 (v8) Debian (64-bit)
https://github.com/Inqnuam/MongoDB-ARMv8


## additional commands
https://askubuntu.com/questions/16584/how-to-connect-and-disconnect-to-a-network-manually-in-terminal