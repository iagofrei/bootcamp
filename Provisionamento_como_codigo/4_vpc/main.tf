terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region  = "us-east-1"
}

# Cria uma VPC, um tipo de rede privada dentro da AWS.
resource "aws_vpc" "dev-vpc" {
  cidr_block = "172.16.1.0/25"

  tags = {
    Name = "VPC 1 - DE-OP-009"
  }
}

# # Cria uma subnet que pertence àquela rede privada
# resource "aws_subnet" "private-subnet1" {
#   vpc_id            = aws_vpc.dev-vpc.id
#   cidr_block        = "172.16.1.48/28"
#   availability_zone = "us-east-1a"

#   tags = {
#     Name = "Subnet 1 - DE-OP-009"
#   }
# }

# # Cria outra subnet que pertence àquela rede privada
# resource "aws_subnet" "private-subnet2" {
#   vpc_id            = aws_vpc.dev-vpc.id
#   cidr_block        = "172.16.1.64/28"
#   availability_zone = "us-east-1b"

#   tags = {
#     Name = "Subnet 2 - DE-OP-009"
#   }
# }


resource "aws_subnet" "private-subnet" {
  count             = var.subnet_count
  vpc_id            = aws_vpc.dev-vpc.id
  cidr_block        = var.subnet_cidr_block[count.index] # "172.16.1.0/25" 172.16.1.48 até 172.16.1.64 
  availability_zone = var.subnet_availability_zone[count.index]

  tags = {
    Name = "Subnet ${count.index + 1} - DE-OP-009"
  }
}