#$1 : path to your function, $2 name of the function (on aws)
cd $1
zip -r function.zip *.js node_modules/
aws lambda update-function-code --function-name $2 --zip-file fileb://./function.zip
rm function.zip
cd $OLDPWD
