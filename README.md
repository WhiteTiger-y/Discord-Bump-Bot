# Discord Bump Bot

This is a Discord bot that automatically sends the `/bump` command in a specified channel every 130 minutes. The bot asks for the channel to use when it joins a new server and can also be configured using the `!setbumpchannel` command.

## Features

- Sends the `/bump` command in a specified channel every 130 minutes.
- Prompts the server owner to specify the bump channel upon joining a server.
- Allows the server owner to change the bump channel using the `!setbumpchannel` command.

## Prerequisites

- Python 3.6 or higher
- A Discord bot token
- A Discord bot client ID

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/discord-bump-bot.git
    cd discord-bump-bot
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file:**

    Create a file named `.env` in the project directory and add your bot token and client ID:

    ```env
    DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE
    DISCORD_CLIENT_ID=YOUR_CLIENT_ID_HERE
    ```

5. **Run the bot:**

    ```sh
    python bot.py
    ```

## Adding the Bot to Your Server

1. **Generate the OAuth2 URL:**

    Replace `YOUR_CLIENT_ID_HERE` with your bot's client ID in the following URL:

    ```plaintext
    https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID_HERE&scope=bot&permissions=92184
    ```

2. **Invite the bot:**

    Open the generated URL in your browser and invite the bot to your server.

## Usage

- **Setting the bump channel:**

    When the bot joins a server, it will ask the server owner to specify the channel for sending the `/bump` command. The server owner should mention the desired channel.

- **Changing the bump channel:**

    Use the `!setbumpchannel` command followed by mentioning the desired channel. For example:

    ```plaintext
    !setbumpchannel #general
    ```

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to the branch.
5. Create a new pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py) - Python wrapper for the Discord API
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Read environment variables from a `.env` file

