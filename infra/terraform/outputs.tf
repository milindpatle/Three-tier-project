output "ecr_backend_url" { value = aws_ecr_repository.backend.repository_url }
output "ecr_frontend_url" { value = aws_ecr_repository.frontend.repository_url }
output "cluster_name" { value = aws_eks_cluster.eks.name }
output "kubeconfig_command" { value = "aws eks update-kubeconfig --name ${aws_eks_cluster.eks.name} --region ${var.aws_region}" }
output "ci_access_key_id" { value = aws_iam_access_key.ci_key.id }
output "ci_secret_access_key" { 
  value = aws_iam_access_key.ci_key.secret
  sensitive = true
   }
