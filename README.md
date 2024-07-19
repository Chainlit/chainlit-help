# RAG Copilot

The Chainlit copilot for the Chainlit [documentation](https://docs.chainlit.io/get-started/overview).

## How to use?

### The Chainlit Application

- `cp app/.env.example app/.env`
- Obtain a Literal API key [here](https://docs.getliteral.ai/python-client/get-started/authentication#how-to-get-my-api-key)
- Get an OpenAI API key [here](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key)
- Find your Pinecone API key [here](https://docs.pinecone.io/docs/authentication#finding-your-pinecone-api-key)
- `pip install -r app/requirements.txt`
- `chainlit run app/app.py`

### The Chainlit Copilot

- Make sure the Chainlit application is running.
- `python -m http.server 3004 --directory copilot`

### Embed the documentation

To upload the latest embeddings to Pinecone:

- `cp embed-documentation/.env.example embed-documentation/.env`
- Get an OpenAI API key [here](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key)
- Find your Pinecone API key [here](https://docs.pinecone.io/docs/authentication#finding-your-pinecone-api-key)
- `pip install -r embed-documentation/requirements.txt`
- `./embed-documentation/main.sh`

## How to contribute?

Make all the changes you want to the application, then validate them in local against [Test dataset to ship RAG](https://cloud.getliteral.ai/projects/chainlit-doc-JicvnMkIcofi/datasets/a24f9233-d03e-4dc4-98c6-c5fec438f757).

Follow the `Experiments.ipynb` notebook to run your experiments against that dataset.

To have a locally exposed endpoint you can test with, run the `main.py` Fast API server from the root directory:

```shell
uvicorn --app-dir app main:app --host 0.0.0.0 --port 80
```

This will expose the http://localhost:80/app/ endpoint where you can put your question at the end.
