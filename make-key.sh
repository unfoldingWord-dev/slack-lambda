#!/bin/bash
########################################################################
#
# NAME make-key.sh  -  make travis keys from aws credentials
#
# USAGE: ./make-key.sh
#
# AWS credentials expected to be in ~/.aws/credentials
#
########################################################################

yaml=".travis.yml"
cred=~/.aws/credentials

cp ${yaml} ${yaml}.bak
grep -v 'secure:' ${yaml} > ${yaml}.tmp
mv ${yaml}.tmp ${yaml}
str=""

while read line ; do
    echo ${line}
    key="${line%=*}"
    val="${line#*=}"

    case ${key} in
        '['*|'#'*) ;; # ignore commented out credentials
        *)
            if [ "${str}" = "" ]
            then
                str="${key^^}=${val}"
            else
                str="${str} ${key^^}=${val}"
            fi
        ;;
    esac
done < ${cred}

travis encrypt ${str} --add env.global -r ~/Projects/slack-lambda

echo "Finished"
