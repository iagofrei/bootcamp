variable "subnet_cidr_block" {
    type = list
    default = ["172.16.1.48/28", "172.16.1.64/28"]
    description = "CIDR block as subnets"
}

variable "subnet_availability_zone" {
  type = list
  default = ["us-east-1a", "us-east-1b"]
  description = "AZ para as subnets"
}

variable "subnet_count" {
  type = number
  default = 2
  description = "Número de subnets a serem criadas"
}