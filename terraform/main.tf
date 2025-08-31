resource "aws_instance" "devops" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = var.instance_type

  user_data = file("terraform/user_data.sh")

  tags = {
    Name = "DevOpsAssignmentInstance"
  }
}
