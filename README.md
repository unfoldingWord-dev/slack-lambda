[![Build Status](https://travis-ci.org/unfoldingWord-dev/slack-lambda.svg)](https://travis-ci.org/unfoldingWord-dev/slack-lambda) [![Coverage Status](https://coveralls.io/repos/github/unfoldingWord-dev/slack-lambda/badge.svg?v=1)](https://coveralls.io/github/unfoldingWord-dev/slack-lambda)

# Slack Lambda Functions for Door43

### Installing Project Requirements

    ./install-requirements.sh
    
### Initialize Project with Apex
__NOTE: this has to be done whenever you want to deploy to new location. It will create the lambda role on AWS and create the project.json file with the proper role ID.  Make sure you have the correct AWS key set up.__

    cd ~/Projects/slack-lambda
    aws configure
    apex init

### Deploying with Apex
__NOTE: make sure the AWS key is set and that the role in the project.json file is pointing to the correct deployment destingation (e.g. test or prod).__

    cd ~/Projects/slack-lambda
    apex deploy

### Configure API Gateway

* In the AWS console, select `API Gateway`.
* Click on `Create API`
* Select `New Api` and set `API name` to slack_invite
* Click on `Create API`
* Click on `Actions` and select `Create Resource`
* Set `Resource Name` to `slack_invite`.
* Click on `Create Resource`
* Select `/invite`
* Click on `Actions` and select `Create Method`
* Select `GET` and click on checkmark.
* Click on method `GET`.
* Under `GET - Setup`
* Click on `Lambda Function`
* Set `Lambda Region` to `us-west-2`.
* Set `Lambda Function` to `slack-invite`.
* Click on `Save`
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
* Click on drop down `Body Mapping Template` to compact.
* Click `Save`.
* Click on the `Actions` button and pick `Deploy API`.
* Pick `prod` for the stage and click `Deploy`.
* Prod Stage Editor pops up.  Click on `Save Changes`

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

    python encrypt_token.py
