variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "app_name" {
  description = "Name of the backend app"
  default     = "feedback-backend"
}

variable "image_url" {
  description = "Docker image URL for ECS task"
  type        = string
}

variable "container_port" {
  description = "Port container listens on"
  default     = 5000
}

variable "subnet_ids" {
  description = "List of subnet IDs for ECS networking"
  type        = list(string)
}

variable "security_group_ids" {
  description = "List of security group IDs"
  type        = list(string)
}
