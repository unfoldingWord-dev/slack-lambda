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

while read k e v ; do
  uk=${k^^} # uppercase credential names

  case ${k} in
    '['*|'#'*) ;; # ignore commented out credentials
    *)
      echo ${uk}
      echo ${v}
      res="$res $uk=$v "  # add a variable to the list
      ;;
  esac
done < ${cred}

#travis encrypt ${res} --add

echo "Finished"
