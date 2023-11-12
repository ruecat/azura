<div align="center">
  <br>
  <a href="">
    <img src="res/github/azura-readme.png" width="200" height="200">
  </a>
  <h1>Azura</h1>
  <p>
    <b>Embrace the meow-nificent power of Azura, the cat-tastic Discord bot 😻</b><br>
    <b>🚧 Project is still WIP 🚧</b><br>
    <b>🐈 Feel free to contribute!</b><br>
  </p>
  <br>
  <p align="center">
    <img src="https://img.shields.io/github/downloads/ruecat/azura/total?color=green&style=for-the-badge"/>
    <a href="https://discord.gg/VHUYnFB4MS">
      <img src="https://dcbadge.vercel.app/api/server/VHUYnFB4MS"/>
    </a>
  </p>
  <br>
</div>

## Prerequisites
- [Docker](https://github.com/docker)
- [Docker-Compose](https://github.com/docker/compose)
- [Discord-Bot Token](https://discord.com/developers/applications)
## Installation (Docker-Compose)
+ Clone Repository
```
git clone https://github.com/ruecat/azura
```
+ Edit TOKEN variable in [docker-compose.yml](https://github.com/ruecat/azura/blob/main/docker-compose.yml) environment
```env
environment:
    - TOKEN=yourtoken
```
+ Run docker-compose
```
docker-compose up -d
```
+ You are all set!
## Installation (Non-Docker)
+ Install latest [Python](https://python.org/downloads)
+ Clone Repository
```
git clone https://github.com/ruecat/azura
```
+ Install requirements from azreqs.txt
```python
pip install -r azreqs.txt
```
+ Launch Azura
```python
python launch.py
```
If you have MacOS or Linux, use this command instead
```python
python3 launch.py
```
## Environment Configuration
|    Parameter     |                                            Description                                            |                                        Required?                                        | Default Value |            Example            |
|:----------------:|:-------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|:-------------:|:-----------------------------:|
|     `TOKEN`      | Your **Discord bot token**, you can obtain it [here](https://discord.com/developers/applications) |                                           Yes                                           |  `yourtoken`  | MTA0M****.GY5L5F.****g*****5k | 
| `BOOSTER_ROLEID` |                         Boosters' role, to give more experience and money                         |                      Optional. **Dependency:** Ecomomy and Levels                       |     None      |      123456789010111213       |
| `BOOSTER_MONEY`  |                        How much **_money_** booster will get per message.                         |                      Optional. **Dependency:** Ecomomy and Levels                       |       5       | Integer Values: 1 2 3 4, etc  |
|  `BOOSTER_EXP`   |                      How much _**experience**_ booster will get per message.                      |                      Optional. **Dependency:** Ecomomy and Levels                       |       5       | Integer Values: 1 2 3 4, etc  |
