# 💖 Contributing to Ruka-Bot

We are thrilled that you are considering contributing to Ruka-Bot! This project thrives on community involvement, and every pull request, bug report, and feature idea helps us manage Telegram groups better.

Ruka-Bot is proudly powered by **DevsLab**, an open community of developers.

## 💡 How Can I Contribute?

There are several ways you can help make Ruka Sarashina better:

### 🐛 Reporting Bugs

If you find a bug (a command not working, an error trace, or unexpected behavior), please open an issue on GitHub.

* **Do not** report bugs in the Telegram support chat.
* **Include:** The steps to reproduce the bug, the expected behavior, the actual behavior, and any relevant logs or screenshots.

### ✨ Suggesting Features

We welcome new feature ideas! If you want Ruka to learn a new trick:

* **Check** if the feature has already been suggested in the Issues tab.
* If not, open a new Issue and prefix the title with `[FEATURE]`.
* Clearly describe the feature, why it is useful, and how you imagine it working.

### 💻 Code Contributions (The Fun Part!)

Ready to write some Python? We follow a standard open-source contribution workflow.

### Prerequisites

Before coding, ensure you have a working Python development environment:
* Python 3.9+ installed.
* Your Telegram **API_ID**, **API_HASH**, and **BOT_TOKEN**.

### Development Setup

1.  **Fork** the repository to your own GitHub account.
2.  **Clone** your forked repository:
    ```bash
    git clone https://github.com/ishikki-akabane/Ruka-Bot.git
    cd Ruka-Bot
    ```
3.  **Install** dependencies:
    ```bash
    pip3 install -U -r requirements.txt
    ```
4.  **Configuration:** Create a `.env` file and fill in your necessary environment variables (e.g., `API_ID`, `BOT_TOKEN`, `DB_URL`).
5.  **Run** your local copy for testing:
    ```bash
    python3 -m RUKA
    ```

### Pull Request Workflow

All code changes must be submitted via Pull Requests (PRs).

1.  **Create a New Branch:** Base your work off the `master` branch.
    ```bash
    git checkout master
    git pull origin master
    git checkout -b feature/your-awesome-feature
    ```
2.  **Implement** your changes.
3.  **Commit** your changes with a descriptive commit message (e.g., `feat: Add new anti-flood module`).
4.  **Push** your branch to your fork:
    ```bash
    git push origin feature/your-awesome-feature
    ```
5.  **Open a Pull Request (PR)** on the original `ishikki-akabane/Ruka-Sarashina` repository.

### Style and Standards

To keep the codebase clean and maintainable:

* **PEP 8 Compliance:** All code must adhere to [PEP 8](https://peps.python.org/pep-0008/) standards.
* **Type Hinting:** Please use Python [Type Hinting](https://docs.python.org/3/library/typing.html) where appropriate.
* **Framework Style:** Follow the general architecture and style of the existing **Pyrogram/Kurigram** code base.

## ⚖️ Code of Conduct

As members of the **DevsLab** community, we strive to keep our interactions positive and professional. By participating in this project, you agree to abide by the [DevsLab Community Guidelines](https://t.me/devslab) and the standard **Contributor Covenant Code of Conduct**.

---

### Thank you for being a part of Ruka-Bot!
**The Developer: Ishikki Akabane**