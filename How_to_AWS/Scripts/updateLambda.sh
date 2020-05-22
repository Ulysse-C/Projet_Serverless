#$1 : path to your function, $2 name of the function (on aws), $3 extension of the function
zip -r9 function.zip $1/package    
zip -g function.zip $1/*.$3
aws lambda update-function-code --function-name $2 --zip-file fileb://./function.zip
rm function.zip