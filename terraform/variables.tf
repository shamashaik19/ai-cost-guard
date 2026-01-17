variable "region" {
  default = "ap-south-1"
}

variable "project_name" {
  default = "aws-cost-guard"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "public_subnet_cidrs" {
  type = list(string)
}

variable "azs" {
  type = list(string)
}
