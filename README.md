# Mozio API Integration

## Configuration

The Mozio API Authorization Key must be set in order to run. Then, you will need set up this on `.env` like below.
```
MOZIO_INTEGRATION_API_KEY=Your Mozio API Key here
```
Obs.: I really recommend you create a `.env.secrets` to keep this sensitive information safe.

## Run
```
python main.py
```

## Test
```
pytest
```

## Linting
```
flake8
```
