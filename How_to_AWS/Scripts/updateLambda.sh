#$1 : path to your function, $2 name of the function (on aws), $3 extension of the function
cd $1
cd package
zip -r9 ${OLDPWD}/function.zip .
cd $OLDPWD
zip -g function.zip *.$3
aws lambda update-function-code --function-name $2 --zip-file fileb://./function.zip
rm function.zip
cd $OLDPWD
