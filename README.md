#Documentaiton
# Echo Server

<div align="center">

<img alt="GitHub Created At" src="https://img.shields.io/github/created-at/KieranPritchard/:repo">

<img alt="GitHub License" src="https://img.shields.io/github/license/KieranPritchard/:repo">

<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/KieranPritchard/:repo">

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KieranPritchard/:repo">

<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/KieranPritchard/:repo">

<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/KieranPritchard/:repo">

</div>
## Project Description
### Objective 
To build two programs to strengthen knowledge in Pythons socket library, as i haven't used it before. 
### Features
* Features both the client app and server app.
* Allows client program to send commands to the server program, then the server echoes back.
* Uses a JSON file for host and port configuration.
### Technologies and Tools Used
* **Language:** Python
* **Frameworks/Library's:** Sockets, JSON, and sys.
* **Tools:** Git, Github, VS Code.
### Challenges Faced
I have had trouble with wrapping my head around this library. I think it was mainly due to me not using it before however, I think in time I will become more familiar with it. 
### Outcome
Successfully created the echo server apps, for client and server. Started to build skill in using this python library, hoping to do more projects using this module.
### Next Steps
To use this library to build other projects and eventually gain advanced knowledge with this module.
## How to Use the Project

1. **Setup Configuration File**
	- Use the `config.json` file in the project directory.
	- Update it with the information you want.
2. **Run the Server**
	- Open a terminal and navigate to the project directory.
	- Run the server script using the command: `python server.py`
	* The server will start and begin listening for incoming client connections.
3. **Run the Client**
	- Open another terminal and navigate to the same project directory.
	- Run the client script using the command: `python client.py`
	- The client will connect to the server and you will be prompted to input a message.
4. **Send Messages**
	- From the client, type a message to send to the server and press Enter.
	- The server will receive the message and send it back as an echo.
	- The client will display the echoed message.
	- Type “quit” to close the connection.
5. **Close the Server**
	- The server will keep running until manually stopped.
	- To stop the server, press `Ctrl+C` in the server terminal.
## License
This is located in the root of the repository.
