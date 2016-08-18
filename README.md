# Slack Lambda Functions for Door43

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
