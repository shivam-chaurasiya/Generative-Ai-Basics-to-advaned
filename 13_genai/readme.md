--------------- IN THIS CHAPTER WE ARE WORKING ON LARGE LANGUAGE MODEL -------------------------------

LLM: Large language models (LLMs) are a category of deep learning models trained on immense amounts of data, making them capable of understanding and generating natural language and other types of content to perform a wide range of tasks.

-Large Language Models (LLMs) are advanced AI systems built on deep neural networks designed to process, understand and generate human-like text.

GPT(Generative Pre-trained Transformer): GPT, or a generative pre-trained transformer, is a type of large language model (LLM) that utilizes deep learning to produce human-like text.

For more :- https://www.geeksforgeeks.org/artificial-intelligence/introduction-to-generative-pre-trained-transformer-gpt/

Tokenization in NLP: Tokenization is a fundamental step in Natural Language Processing (NLP). It involves dividing a Textual input into smaller units known as tokens. These tokens can be in the form of words, characters, sub-words or sentences. It helps in improving interpretability of text by different models. Let's understand How Tokenization Works.

--Tokenization is the process of breaking down input text into smaller pieces called tokens. These tokens are the building blocks that a Large Language Model (LLM) processes.

Transformers:  the transformer is a family of artificial neural network architectures based on the multi-head attention mechanism, in which text is converted to numerical representations called tokens

Prompt Engineering: Prompt engineering is a relatively new discipline for developing and optimizing prompts to efficiently use language models (LMs) for a wide variety of applications and research topics. Prompt engineering skills help to better understand the capabilities and limitations of large language models (LLMs).

Prompt: A prompt can contain information like the instruction or question you are passing to the model and include other details such as context, inputs, or examples. 

Prompting Technique: 
1. Zero-Shot Prompting: Zero-shot prompting means that the prompt used to interact with the model won't contain examples or demonstrations. The zero-shot prompt directly instructs the model to perform a task without any additional examples to steer it.

2.Few-Shot Prompting: Few-shot prompting can be used as a technique to enable in-context learning where we provide demonstrations in the prompt to steer the model to better performance.

--The demonstrations serve as conditioning for subsequent examples where we would like the model to generate a response.

Chain of Thought Prompting: chain-of-thought (CoT) prompting enables complex reasoning capabilities through intermediate reasoning steps. You can combine it with few-shot prompting to get better results on more complex tasks that require reasoning before responding.

Automatic Chain-of-Thought (Auto-CoT): When applying chain-of-thought prompting with demonstrations, the process involves hand-crafting effective and diverse examples. This manual effort could lead to suboptimal solutions

-an approach to eliminate manual efforts by leveraging LLMs with "Let's think step by step" prompt to generate reasoning chains for demonstrations one by one. This automatic process can still end up with mistakes in generated chains. To mitigate the effects of the mistakes, the diversity of demonstrations matter. This work proposes Auto-CoT, which samples questions with diversity and generates reasoning chains to construct the demonstrations.


Persona Prompting: Persona prompting is a technique where you instruct an AI to adopt a specific identity, role, or background before executing a task. By defining the role, tone, and context, you shape how the model filters its knowledge base to produce outputs tailored to a specific perspective