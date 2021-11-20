environment            = "dev"
function_name          = "S3_Notifier"
handler_name           = "lambda_function"
runtime                = "python3.6"
timeout                = "900"
sender_email           = ""
receiver_email         = ""
lambda_role_name       = "s3_notifer_lambda_iam_role"
lambda_iam_policy_name = "s3_notifer_lambda_iam_policy"
bucket_name            = "s3-notifier-test-bucket-245"


