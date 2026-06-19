# Generative AI Course (CampusX)

Welcome to the Complete Generative AI course repository! This repository contains code examples, notes, and practical exercises centered around building LLM applications using the **LangChain** ecosystem.

## 📁 Course Structure

The course is divided into several modules, each focusing on a core concept of LangChain and LLM application development:

- **[Models](./LandChain-Models)**: Working with various LLMs (Large Language Models) and Chat Models.
- **[Prompts](./LangChain_Prompts)**: Designing, managing, and utilizing prompt templates effectively.
- **[Document Loaders](./LangChian_DocumentLoaders)**: Ingesting data from various sources (PDFs, URLs, databases, etc.).
- **[Text Splitters](./LangChain_TextSplitters)**: Chunking and splitting large documents for efficient retrieval.
- **[Vector Stores](./langchain_VectorStores)**: Storing and managing vector embeddings.
- **[Retrievers](./LangChain_Retrivers)**: Fetching relevant context/documents for your LLM.
- **[Output Parsers](./LangChain_Output_Parser)**: Formatting and structuring the raw output from LLMs.
- **[Structured Output](./LangChain_Structured-Output)**: Enforcing strict schemas on LLM generations.
- **[Tools](./LangChain_Tools)**: Equipping LLMs with external capabilities (e.g., web search, calculators, API access).
- **[Runnables / LCEL](./LangChain_Runnables)**: Utilizing LangChain Expression Language (LCEL) for flexible chain compositions.
- **[Chains](./LangChain_Chains)**: Building end-to-end processing pipelines.
- **[AI Agents](./LangChain_AI_Agents)**: Creating autonomous agents that use reasoning to decide which tools to call.

*(Note: Folder names are preserved exactly as they exist in the repository.)*

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher.
- A code editor like VS Code or Jupyter Notebook.
- API keys for the LLMs you intend to use (e.g., OpenAI API Key, Anthropic, Google Gemini, etc.).

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd CampusX
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   Install required packages (e.g., `langchain`, `langchain-core`, `langchain-openai`, etc.) as needed for each module. 
   ```bash
   pip install langchain
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   OPENAI_API_KEY="your-openai-api-key"
   # Add other keys as required
   ```

## 📚 Learning Objectives
By following along with the code in these directories, you will learn how to:
- Build simple conversational bots.
- Create RAG (Retrieval-Augmented Generation) applications.
- Understand and implement advanced retrieval techniques.
- Build agents capable of using tools and APIs.
- Master the LangChain Expression Language (LCEL).
