terraform {
  required_providers {
    aws = {      
      version = ">=4.9.0"
      source  = "hashicorp/aws"
    }
  } 
}

provider "aws" {
  profile                  = "prasanna-cloud-resume-challenge" 
  region                   = "us-east-1"
}