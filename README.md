# Musical Agents

This is is a repository for studying LLM Agents with musical agents. This means I'll be testing different frameworks, acrhitectures and functionalities to create LLM Agents that compose music.

## Requirements
In order to run these notebooks, you'll need:

1. Python >= 3.10.0
2. At least ~8GB of RAM available to use
3. Download and setup [Ollama](https://ollama.com/) (I recommend you "quit" ollama before coding so you know when you're serving)
4. Clone this repository
5. Download the requirements
6. Run ```ollama pull qwen:7b``` to install the same LLM model I've used
7. Run ```ollama serve``` before runing the code in the notebooks
8. (Optional but strongly recommended) Download the "Resource Monitor" VSCode extension by ```mutantdino```. It displays how much CPU and RAM you're currently using, so you can prevent your PC from shutting down unexpectedly (as it happened to me many times).

I recommend you close all other tabs (specially google chrome) before running any cells with prompts. Also, if your VSCode seems to be taking up too much RAM, try to shut down any extension that is not essential.