# Steps I took for deploying to AWS Lambda from Travis-CI using Apex

1. Add a `requirements.txt` file to the directory containing the function. Add the python requirements that must be installed in the directory with the function.
2. Add these to `.apexignore`:
    ```
    *.dist-info/
    .gitignore
    *.pyc
    requirements.txt
    ```
3. Create `.gitignore` in the same directory as .apexignore. Add the directories created for the dependencies in `requirements.txt` and the following:
    ```
    *.dist-info/
    *.pyc
    ```
4. Create script `travis-install-apex.sh` and make it executable. See the example in the current directory. This will download the latest Apex executable and install it in the parent directory of the repository on Travis-CI.
5. Create script `install-requirements.sh` and make it executable. See the example in the current directory. Travis CI will use this to install the python requirements from the `requirements.txt` file you created in step 1. This removes the need for checking the dependency files into Git.
6. Create script `deploy.sh` and make it executable. See the example in the current directory. After all the tests have passed, this script will check if the function is ready to be deployed to AWS Lambda. If it is ready, it will deploy the function using Apex.
7. Add `"./travis-install-apex.sh"` and the install for __awscli__ to the __before_install:__ section of `.travis.yml`. The quotation marks are required.
    ```
    before_install:
      - pip install awscli
      - "./travis-install-apex.sh"
    ```
8. Add `"./install-requirements.sh"` to the __install:__ section of `.travis.yml`. The quotation marks are required.
    ```
    install:
      - "./install-requirements.sh"
      - pip install coveralls
    ```
9. Add `"./deploy.sh"` to the __after_success:__ section of `.travis.yml`. The quotation marks are required.
    ```
    after_success:
      - coveralls
      - "./deploy.sh"
    ```
10. Add the following global environment variable to `.travis.yml`. This will prevent python from creating `*.pyc` files:
    ```
    env:
      global:
        - PYTHONDONTWRITEBYTECODE=true
    ```
11. Add __AWS_REGION__, __AWS_ACCESS_KEY_ID__, and __AWS_SECRET_ACCESS_KEY__ to the _Environment Variables_ section of the repository setting on travis-ci.org.

## Notes:

* I tried using the Travis cli to encrypt the AWS security values and include them in the `.travis.yml` but I couldn't get it to work. There were no error messages but the environment variables were not created either.
* It looks like local scripts must always be enclosed in quotation marks, even though the Travis CI documentation does not show this.
* There is a __deploy__ feature that can be included in the `.travis.yml` file but it won't work for this type of deployment. After the tests have succeeded and before the deploy script is run, Travis CI resets the git repository and deletes all files that are not in the repository, including the function dependencies that must be uploaded with the function.
