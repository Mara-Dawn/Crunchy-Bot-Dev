# Crunchy-Bot-Dev
Dev Container repo for Crunchy Bot

## Usage
1. Open VSCode and Clone this repo as a new Project
2. Install [Docker Desktop](https://www.docker.com/get-started/)
3. Install the VSCode extensions *Dev Containers* (maybe *Docker* too, just to be sure)
4. Click the blue X looking thingy in the very bottom left of your IDE
5. select 'Reopen in Container'
6. Wait for the container to build.
7. Use Ctrl + Shift + P and type in "interpreter"
8. select "Python: Select Interpreter"
9. choose the 3.12.3 one in /usr/local/bin/python
10. done! c:

## Keys
After the initial build you will have a few .txt files in your workspace.
Those need to be filled with the corresponding API keys.

## Rebuilding the Container
You will only need to rebuild the container when dependencies change,
other than that you can just start your vs code and add your extensions of choice
just like you are used to.
