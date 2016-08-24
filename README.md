[![Build Status](https://travis-ci.org/unfoldingWord-dev/slack-lambda.svg)](https://travis-ci.org/unfoldingWord-dev/slack-lambda) [![Coverage Status](https://coveralls.io/repos/github/unfoldingWord-dev/slack-lambda/badge.svg)](https://coveralls.io/github/unfoldingWord-dev/slack-lambda)

# Slack Lambda Functions for Door43

### Installing Project Requirements

    ./install-requirements.sh
    
### Deploying with Apex

    cd ~/Projects/slack-lambda
    apex deploy

### Enable API

* In the AWS console, select `API Gateway`.
* Select the slack_invite API, click Resources, then select GET.
* Click on `Method Request` and enter the `URL Query String Parameters` needed.
* Click back.
* Click on `Integration Request`.
* Expand `Body Mapping Templates`.
* Select `When no template matches the request Content-Type header`.
* Click `Add a mapping template`.
* Enter `application/json` and then select `Method Request passthrough` from the Generate template dropdown.
* Click `Save`.
* Click back.
* Click `Integration Response`.
* Click the drop-down arrow in the first row.
* Drop down `Body Mapping Template`.
* Click `Add mapping template`.
* Enter `application/json` and then enter `$util.parseJson($input.json('$'))` in the template area.
* Click `Save`.
* Click on the `Actions` button and pick `Deploy API`.
* Pick `prod` for the stage and click `Deploy`.

### Installing Travis CLI

__NOTE: Ruby is required. I used Ruby version 2.2.2 and it worked.__

    gem install travis --no-rdoc --no-ri
    ln -s ~/.rbenv/versions/2.2.2/bin/travis ~/.local/bin/travis

### Installing AWS CLI

    sudo apt install awscli

### Configuring AWS CLI

    aws configure

### Installing Apex

    sudo curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sudo sh

### Encrypting the Slack API Token

Follow on-screen prompts:

    python functions/invite/encrypt.py
