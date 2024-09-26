# Crunchy-Bot-Dev
Dev Container repo for Crunchy Bot

## Usage
1. Open VSCode and Clone this repo as a new Project
2. Install [Docker Desktop](https://www.docker.com/get-started/)
3. Install the VSCode extensions *Dev Containers* (maybe *Docker* too, just to be sure)
4. Open the .env file and fill out the env variables, put your forked repository in `DEV_REPO_URL`
5. Click the blue X looking thingy in the very bottom left of your IDE
6. select 'Reopen in Container'
7. Wait for the container to build.
8. Use Ctrl + Shift + P and type in "interpreter"
9. select "Python: Select Interpreter"
10. choose the 3.12.3 one in /usr/local/bin/python
11. done c:

## Rebuilding the Container
You will only need to rebuild the container when dependencies or environment variables change,
other than that you can just start your vs code and add your extensions of choice
just like you are used to.
