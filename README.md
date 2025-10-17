# ABZ Agent SDK — Quick Setup Guide

### Create Your Own Agent  
You can easily create your own agent using **ABZ Agent SDK**.  

---

### Install the SDK  

If you're using **[Uv](https://github.com/astral-sh/uv)**:  
```bash
uv add abagentsdk
```

If you're using **pip**:  
```bash
pip install abagentsdk
```

---

### Setup Your Project  
Once installed, initialize your agent project by running:  
```bash
abagentsdk setup
```

---

### Example Setup Output  
When you run the command, it will prompt you for setup details:  

```
ABZ Agent SDK CLI — Project setup

Enter your GEMINI_API_KEY (leave blank to fill later): YOUR_GEMINI_API_KEY
Agent name [My Agent]: YOUR_AGENT_NAME
Agent instructions [Be helpful and concise.]: INSTRUCTIONS_HERE
Model id [gemini-2.0-flash]: GEMINI_MODEL_ID
Starter file name [agent.py]: ANYFILE_NAME
```

---

### Next Steps
1. Open the generated Python file (e.g., `agent.py`)
2. Make sure you set your api_key is set in .env
3. Run your agent using:
   ```bash
   abagentsdk run agent.py
   ```
4. Start chatting with your custom AI agent.
