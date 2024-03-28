name: Deploy to Staging

on:
  push:
    branches: [ staging ]

jobs:
  deploy: 
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run the program 
        env:
          ENVIRONMENT: staging
        run: python main.py
