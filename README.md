# PipoCoin - Python

PipoCoin is just a bot (made for fun) that simulates "money"(pipo _Coin_) transactions on twitter.

## Notes

If you want to run this bot you'll need a [twitter dev account](https://developer.twitter.com/en) to have access to twitter API. [More information here](https://developer.twitter.com/en/apply-for-access)\
Once you have twitter api keys and tokens you just need to put it in a '.env' file at project root('/pipocoin-python/.env'). Example:

```.env
CONSUMER_KEY=yourConsumerKeyHere
CONSUMER_SECRET=yourConsumerSecretHere
ACCESS_TOKEN=yourAccessTokenHere
ACCESS_TOKEN_SECRET=yourAccessTokenSecretHere
```

## Installation

First you need to created python virtual environment, so navigate to the project folder:

```bash
cd "/path/to/pipocoin-python"
```

Create python _venv_:

```bash
python -m venv venv
```

Activate the _venv_:

```bash
source venv/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

If you intend to modify the code you also need to install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the code:

```bash
python pipocoin
```

## Author

- Pietro Bondioli ([@bondiolipietro](https://github.com/bondiolipietro))

## License

[MIT](https://opensource.org/licenses/MIT)
