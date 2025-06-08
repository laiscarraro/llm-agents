# Musical Agents

This is is a repository for studying LLM Agents with musical agents. This means I'll be testing different frameworks, acrhitectures and functionalities to create LLM Agents that compose music.

## Requirements
In order to run these notebooks, you'll need:

1. Python >= 3.10.0
2. At least ~5GB of RAM available to use
3. (Recommended) VSCode
4. Download and setup [Ollama](https://ollama.com/) (I recommend you "quit" ollama before coding so you know when you're serving)
5. Clone this repository
6. Download the requirements
7. Run ```ollama pull {model}``` to install the an LLM model*
8. Run ```ollama serve``` before runing the code in the notebooks
9. (Strongly recommended) Download the "Resource Monitor" VSCode extension by ```mutantdino```. It displays how much CPU and RAM you're currently using, so you can prevent your PC from shutting down unexpectedly (as it happened to me many times).

I recommend you close all other tabs (specially google chrome) before running any cells with prompts. Also, if your VSCode seems to be taking up too much RAM, try to shut down any extension that is not essential.

*About which model to choose. I've used ```qwen2:7b``` in my first tests, but the model you're going to use depends on the available RAM in your PC. Here are my recommendations:
- 5GB < RAM < 8GB: ```ollama pull phi3:mini```
- 8GB < RAM < 20GB:  ```ollama pull qwen2:7b``` or ```ollama pull mistral:7b``` or the above.
- RAM >= 20GB: ```ollama pull deepseek-coder:7b``` or any of the above.

You can change the function ```choose_model()``` to choose the model automatically based on the rules above.