# AutoGen Framework: Comprehensive Guide

This document provides an in-depth overview of the AutoGen framework, focusing on its core components: `ConversableAgent`, `AssistantAgent`, `UserProxyAgent`, and `GroupChatManager`. It includes detailed instructions on class instantiation, command usage, parameter configurations, and customization of system messages.

---

## Table of Contents

- [AutoGen Framework: Comprehensive Guide](#autogen-framework-comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [1. Overview of Core Classes](#1-overview-of-core-classes)
    - [ConversableAgent](#conversableagent)
    - [AssistantAgent](#assistantagent)
    - [UserProxyAgent](#userproxyagent)
    - [GroupChatManager](#groupchatmanager)
  - [2. Instantiating Core Classes](#2-instantiating-core-classes)
    - [Instantiating ConversableAgent](#instantiating-conversableagent)

---

## 1. Overview of Core Classes

### ConversableAgent

`ConversableAgent` is a foundational class for agents capable of engaging in conversations. It can be customized to integrate Large Language Models (LLMs), human inputs, or tools.&#8203;:contentReference[oaicite:0]{index=0}

### AssistantAgent

:contentReference[oaicite:1]{index=1}&#8203;:contentReference[oaicite:2]{index=2}

### UserProxyAgent

:contentReference[oaicite:3]{index=3}&#8203;:contentReference[oaicite:4]{index=4}

### GroupChatManager

:contentReference[oaicite:5]{index=5}&#8203;:contentReference[oaicite:6]{index=6}

---

## 2. Instantiating Core Classes

Below are concise examples demonstrating how to instantiate each core class.

### Instantiating ConversableAgent

```python
from autogen.agentchat import ConversableAgent

SYSTEM_PROMPT = "You are a knowledgeable assistant that answers questions from your supervisor."
agent = ConversableAgent(
    name="agent",
    system_message=SYSTEM_PROMPT,
    human_input_mode="NEVER",
    llm_config={"model": "gpt-4", "api_key": "your_openai_api_key"}
)
