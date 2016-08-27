#!/usr/bin/env bash
################################################################################
#
# The AWS environment variables will only be available when merging a
# pull request from develop into master due to travis security settings.
#
################################################################################

if [[ $TRAVIS_BRANCH == 'master' && $TRAVIS_SECURE_ENV_VARS == "true" ]]
then
    echo "Deploying..."
    repoDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    thisDir="$( dirname "${repoDir}" )"
    "${thisDir}/apex" deploy -C "${repoDir}"
else
    echo "$AWS_ACCESS_KEY_ID"
    echo "Not deploying:"
    echo "  TRAVIS_BRANCH = $TRAVIS_BRANCH (must be 'master')"
    echo "  TRAVIS_SECURE_ENV_VARS = $TRAVIS_SECURE_ENV_VARS (must be 'true')"
fi
