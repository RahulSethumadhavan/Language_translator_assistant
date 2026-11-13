# Multi-Language Translator Assistant

A Python-based utility application built using the [Google Gemini API](https://pypi.org/project/google-genai/) and `python-dotenv` to translate sentences into multiple target languages (Hindi, Telugu, and French) utilizing system instructions and `GenerateContentConfig`.

---

## Features

- **Environment Configuration**: Securely loads API credentials using `python-dotenv`.
- **System Instructions**: Uses predefined prompt instructions mapped via a dictionary for targeted translations.
- **Configurable Generation**: Utilizes `types.GenerateContentConfig` to set parameters like temperature and max output tokens.
- **Gemini Integration**: Powered by the `gemini-3.5-flash-lite` model for fast, accurate text transformations.

---

## Prerequisites

- Python 3.10 or higher
- A Google Gemini API Key

---

## Installation & Setup

1. **Clone the repository or download the project files.**

2. **Install the required dependencies:**
   ```bash
   pip install python-dotenv google-genai
