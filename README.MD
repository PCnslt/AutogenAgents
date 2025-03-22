
# PyAutoGen Commands Documentation

Below is an overview of available commands for different PyAutoGen agent classes, including common methods, parameter variations, and usage examples.

##Install autogen
```python
pip -m venv env
pip install pyautogen
```
OR
```python
pip -m venv env
echo pyautogen > requirements.txt
pip install -r requirments.txt
```

---

## ConversableAgents

| **Command**                | **Parameters**                                           | **Description**                                        | **Example** |
|----------------------------|----------------------------------------------------------|--------------------------------------------------------|-------------|
| `send_message`             | `message: str`, `recipient: Agent`<br>`urgent: bool=False` | Sends a message to a specified agent.                | `agent.send_message("Hello", recipient_agent)` |
| `receive_message`          | *None*                                                   | Receives the next incoming message.                  | `msg = agent.receive_message()` |
| `set_behavior`             | `behavior: str`<br>`mode: str=None`                      | Sets the agent's communication style.                | `agent.set_behavior("formal", mode="verbose")` |
| `get_conversation_history` | `limit: int=None`                                        | Retrieves conversation history, optionally limited.  | `history = agent.get_conversation_history(limit=50)` |

**Additional Permutations:**

- **Urgent Message Variant:**
  ```python
  agent.send_message("Urgent: System failure", recipient_agent, urgent=True)
  ```
- **Extended Behavior Settings:**
  ```python
  agent.set_behavior("casual", mode="quick", params={"emoji": True})
  ```

---

## AssistantAgents

| **Command**                | **Parameters**                                                      | **Description**                                       | **Example** |
|----------------------------|---------------------------------------------------------------------|-------------------------------------------------------|-------------|
| `assist`                   | `query: str`, `context: dict`<br>`priority: int=0`                   | Provides assistance based on a query and context.     | `assistant.assist("Reset password?", {"user_id": 123}, priority=1)` |
| `provide_information`      | `topic: str`<br>`detail_level: str="brief"`                           | Delivers information on a specified topic.           | `assistant.provide_information("AWS services", detail_level="detailed")` |
| `execute_command`          | `command: str`, `params: dict`                                       | Executes a given command with parameters.            | `assistant.execute_command("restart_service", {"service": "nginx"})` |
| `log_activity`             | `activity: str`<br>`timestamp: datetime=None`                         | Logs a specific activity with an optional timestamp.   | `assistant.log_activity("Executed restart_service")` |

**Additional Permutations:**

- **Extended Assist Example:**
  ```python
  assistant.assist("Need a code review", context={"repo": "github.com/example"}, priority=2)
  ```

---

## UserProxyAgents

| **Command**                | **Parameters**                                              | **Description**                                        | **Example** |
|----------------------------|-------------------------------------------------------------|--------------------------------------------------------|-------------|
| `simulate_user_input`      | `input: str`<br>`delay: float=0.0`                           | Simulates user input with an optional delay.           | `proxy.simulate_user_input("Click button", delay=0.5)` |
| `forward_command`          | `command: str`, `target_agent: Agent`                        | Forwards a command to another agent.                   | `proxy.forward_command("help", target_agent=assistant)` |
| `capture_user_feedback`    | `feedback: str`                                             | Captures and logs user feedback.                       | `proxy.capture_user_feedback("Interface is intuitive")` |

**Additional Permutations:**

- **No Delay Input Simulation:**
  ```python
  proxy.simulate_user_input("Submit form")
  ```

---

## GroupChatManagers

| **Command**                | **Parameters**                                              | **Description**                                        | **Example** |
|----------------------------|-------------------------------------------------------------|--------------------------------------------------------|-------------|
| `create_group_chat`        | `name: str`, `members: list`                                | Creates a new group chat with specified members.       | `manager.create_group_chat("Team Sync", members=[agent1, agent2])` |
| `add_member`               | `member: Agent`                                             | Adds a member to the group chat.                       | `manager.add_member(new_member)` |
| `remove_member`            | `member: Agent`                                             | Removes a member from the group chat.                  | `manager.remove_member(member_to_remove)` |
| `broadcast_message`        | `message: str`                                              | Sends a message to all group chat members.             | `manager.broadcast_message("Meeting in 5 minutes")` |
| `archive_conversation`     | `conversation_id: int=None`                                 | Archives a conversation (optionally by ID).            | `manager.archive_conversation(conversation_id=42)` |

**Additional Permutations:**

- **Creating a Group with No Initial Members:**
  ```python
  manager.create_group_chat("New Group", members=[])
  ```