# Crypto Chatbot

This repository contains code for a crypto chatbot powered by OpenAI's GPT-3.5 Turbo model. The chatbot can provide real-time cryptocurrency prices and engage in conversational interactions.

## Features

- Get the price of a coin: The chatbot can retrieve the price of a specific coin using the Binance API. You can request the price by providing the correctly formatted coin name (e.g., BTCUST, ETHUSDT).

## Usage

To use the crypto chatbot, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your_username/your_repository.git
   ```

2. Set up the API key:
   
   - Obtain an API key from OpenAI.
   - Set the API key as an environment variable named `OPENAI_API_KEY`.

3. Install the required dependencies:

   ```shell
   pip install openai requests
   ```

4. Run the code:

   ```shell
   python chatbot.py
   ```

5. Interact with the chatbot:

   - Enter your message as a prompt.
   - The chatbot will respond with the generated output.

6. Quit the chatbot:

   - To exit the chatbot, type "quit".

## Examples

Here are a few examples of interacting with the chatbot:

```shell
You: What's the price of BTCUST?
Bot: Here are the results I got:
       <price information>
       If you want to know more about this coin, please visit: https://www.binance.com/en/trade/BTCUST

You: How is the market today?
Bot: <market analysis and trends>

You: quit
```

## Notes

- The chatbot uses OpenAI's GPT-3.5 Turbo model for generating responses.
- The Binance API is utilized to fetch real-time cryptocurrency prices.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributions

Contributions to improve the functionality or add new features to the chatbot are welcome. If you have any suggestions or ideas, please open an issue or submit a pull request.

Let's build something cool together!
