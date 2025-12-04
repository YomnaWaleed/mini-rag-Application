# mini-rag
This is a minimal implementation of the RAG model for question answering.

## Requriements

- Python 3.8 or later 

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://www.anaconda.com/docs/getting-started/miniconda/main#quick-command-line-install)

2) create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```

3) Activate the environment:
```bash
$ conda activate mini-rag
```

### (Optional) setup uou command line interface for better reliability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages

```bash
$ pip install -r requirments.txt
```

### Setup the environment variables

```bach
$ cp .env.example .env
```

Set your environment varibles in the `.env` file. Like `OPENAI_API_KEY` value.

## Run Docker Compose Services 

```
$ cd docker 
$ cp .env.example .env
```

- update `.env` with your credentials

```
$ cd docker 
$ sudo docker compose up -d 
```

## run the FastAPI server 

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## Practical Example — Quick Setup for WSL + Ollama

If you are running your app inside WSL, and Ollama is running on Windows, follow these steps:

### 1)Run Ollama on Windows

Open PowerShell as Administrator:

```bash
# Allow Ollama to listen on all interfaces
setx OLLAMA_HOST "http://0.0.0.0:11434"

# Open a new PowerShell window and start Ollama server
ollama serve

```

### 2)Test the connection from WSL

From your WSL terminal:

```bash
curl -v http://172.27.240.1:11434/v1/models

```

Note: Replace 172.27.240.1 with your Windows host IP as seen from WSL (ipconfig -> vEthernet WSL).


### 3)Update .env in your WSL project

```bash
# Open the .env file and update the lines:
OPENAI_API_KEY="ollama"
OPENAI_API_URL="http://172.27.240.1:11434/v1"

```

### 4)Restart your FastAPI server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000

```
Now your mini-rag app should be able to communicate with Ollama running on Windows.