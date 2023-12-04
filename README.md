# Talkinglands

Created 2 lambdas for operational logics as per needed conditions and modified the relevant specifications, used the postman to send a request using API gateway, or the postman took that request from the event and performed the logics.

Deploy the stack using cloud formation

Steps:
    1. Install the libraries
        - pip install -r requirements.txt -t libs/python
    2. Validate the template
        - sam validate --lint -t template.yaml
    3. Build the template
        - sam build -t template.yaml
    4. Deploy the stack
        - sam deploy --guided

