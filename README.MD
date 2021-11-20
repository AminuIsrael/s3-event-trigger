### Lambda S3 Notifier

Steps:
* Run `terraform init` to initialize terraform in the infra folder
* fill in the missing values in the `terraform.tfvars` file
* NOTE: If the AWS SES sandbox is being used ensure the email addresses are verifed
* run  `terraform apply -var-file=terraform.tfvars` to build infrastructure on the AWS environment
* To destroy infrastructure run `terraform destroy` to destroy all running infrastructure on AWS