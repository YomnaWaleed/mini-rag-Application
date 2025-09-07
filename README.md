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

## run the FastAPI server 

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```