
# langchain-pr

Small demo project showing how to use LangChain + Hugging Face to build a simple interactive chat loop.

## What this project does

This tiny project demonstrates a minimal interactive chat script that uses the LangChain Hugging Face integration to call a text-generation/chat model (configured in `chats/chat_hugging_face.py`). It is intended as a learning / prototype example rather than a production-ready app.

## Key details

- Uses Python >= 3.13 (as declared in `pyproject.toml`).
- Dependencies (from `pyproject.toml`): `python-dotenv`, `langchain`, `langchain-huggingface`.
- The example script uses the model `deepseek-ai/DeepSeek-R1-0528` via the `HuggingFaceEndpoint` wrapper.

## Quick start

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the required packages:

```bash
pip install python-dotenv langchain langchain-huggingface
```

3. (Optional) If you plan to call private or rate-limited Hugging Face models, set your Hugging Face token in an environment variable. Create a `.env` file in the project root with:

```env
# .env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

The script uses `python-dotenv` to load `.env` automatically.

4. Run the chat script:

```bash
python chats/chat_hugging_face.py
```

Follow the prompts in the terminal. Type `y` when prompted to start the interactive loop, then ask questions. Press Enter (empty input) to stop.

## How the script works (contract)

- Input: user text prompts typed into the terminal.
- Output: the model-generated response printed to stdout.
- Error modes: missing network, missing HF token for private models, or model endpoint errors will raise exceptions from the underlying Hugging Face client.

Implementation notes (see `chats/chat_hugging_face.py`):

- The script builds a `HuggingFaceEndpoint` instance with a specified `repo_id` and passes it into `ChatHuggingFace` from `langchain_huggingface`.
- Parameters such as `max_new_tokens`, `do_sample`, and `repetition_penalty` are set in the script and can be tuned.

## Edge cases and tips

- If the model is private or your environment has rate limits, export `HUGGINGFACEHUB_API_TOKEN`.
- If responses are too short or repetitive, increase `max_new_tokens` or adjust `do_sample`/`temperature` settings in the script.
- For automated or production usage, avoid the interactive `input()` loop and call the model directly from a function; add error handling and retries.

## Files of interest

- `chats/chat_hugging_face.py` — the interactive chat example.
- `pyproject.toml` — project metadata and declared dependencies.

## License

This repository doesn't include an explicit license file. Consider adding a `LICENSE` (for example MIT) if you want to share the code publicly.

## Next steps (suggestions)

- Add a small tests/ or examples/ folder showing programmatic usage (non-interactive).
- Add a `requirements.txt` or update `pyproject.toml` with explicit pinned versions for reproducibility.

---
Generated README based on the project files in the repository.
