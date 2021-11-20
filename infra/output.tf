# output of lambda arn
output "arn" {
  value = aws_lambda_function.test_lambda.arn
}