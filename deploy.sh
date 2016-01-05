#!/bin/bash

R=`dirname $0`

export AWS_DEFAULT_PROFILE=ogrodnek

rm -rf $R/.build
cactus build && aws s3 sync $R/.build s3://photos.ogrodnek.com
