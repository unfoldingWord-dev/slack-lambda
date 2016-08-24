#!/usr/bin/env bash
################################################################################
#
# The AWS environment variables will only be available when merging a
# pull request from develop into master due to travis security settings.
#
################################################################################

if [[ $TRAVIS_BRANCH == 'master' ]]
then
    thisDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    "${thisDir}/apex" deploy
fi
