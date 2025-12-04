variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "cluster_name" {
  type    = string
  default = "bank-app-eks"
}

variable "vpc_cidr" {
  type    = string
  default = "10.10.0.0/16"
}

variable "public_subnets" {
  type = list(string)
  default = ["10.10.0.0/24", "10.10.1.0/24"]
}

variable "private_subnets" {
  type = list(string)
  default = ["10.10.100.0/24", "10.10.101.0/24"]
}

variable "node_instance_type" {
  type    = string
  default = "t3.medium"
}

variable "desired_capacity" {
  type    = number
  default = 2
}

variable "owner" {
  type    = string
  default = "milind"
}
