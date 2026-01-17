provider "aws" {
  region = var.region
}

module "vpc" {
  source               = "./modules/vpc"
  vpc_cidr             = var.vpc_cidr
  vpc_name             = var.project_name
  public_subnet_cidrs  = var.public_subnet_cidrs
  azs                  = var.azs
}
