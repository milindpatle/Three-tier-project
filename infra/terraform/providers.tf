provider "aws" {
  region = var.aws_region
}

# kubernetes & helm providers are configured after EKS kubeconfig is available.
# You will run `aws eks update-kubeconfig` locally after terraform creates the cluster,
# then re-run terraform apply for helm/kubernetes resources (or run helm/kubectl manually).
