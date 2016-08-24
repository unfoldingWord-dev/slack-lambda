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

while read line ; do
    echo ${line}
    key="${line%=*}"
    val="${line#*=}"

    if [ ${key} = "aws_access_key_id" ]
    then
        travis encrypt ${val} --add deploy.access_key_id
    fi

    if [ ${key} = "aws_secret_access_key" ]
    then
        travis encrypt ${val} --add deploy.secret_access_key
    fi

done < ${cred}

echo "Finished"
