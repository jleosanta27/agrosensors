# agrosensors

Install Docker
sudo curl -sSL https://get.docker.com | sh
sudo usermod -aG Docker [user]

get MongoDB 4.0 image (compatible with ARM8.0A)
sudo docker pull mongo:4.0
sudo docker -d -p 2717:27017 -v ~/test_mongodb/mongodb_docker/db --name mongodb mongo:4.0

Install mongodb (versión compatible with ARMV8)
MongoDB - ARM64 (v8) Debian (64-bit)
https://github.com/Inqnuam/MongoDB-ARMv8


https://askubuntu.com/questions/16584/how-to-connect-and-disconnect-to-a-network-manually-in-terminal