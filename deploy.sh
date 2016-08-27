#!/usr/bin/env bash
################################################################################
#
# The AWS environment variables will only be available when merging a
# pull request from develop into master due to travis security settings.
#
################################################################################

COLOR='\033[0;32m'
OFF='\033[0m'

if [[ $TRAVIS_EVENT_TYPE == "push" && $TRAVIS_BRANCH == "master" && $TRAVIS_SECURE_ENV_VARS == "true" ]]
then
    echo "Deploying..."
    repoDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    thisDir="$( dirname "${repoDir}" )"
    "${thisDir}/apex" deploy -C "${repoDir}"
else
    echo "Not deploying:"
    echo "  TRAVIS_EVENT_TYPE = ${COLOR}$TRAVIS_EVENT_TYPE${OFF} (must be 'mpush')"
    echo "  TRAVIS_BRANCH = ${COLOR}$TRAVIS_BRANCH${OFF} (must be 'mmaster')"
    echo "  TRAVIS_SECURE_ENV_VARS = ${COLOR}$TRAVIS_SECURE_ENV_VARS${OFF} (must be 'mtrue')"
fi
