resource "aws_eks_node_group" "public" {
  cluster_name    = aws_eks_cluster.eks.name
  node_group_name = "${var.cluster_name}-public-ng"
  node_role_arn   = aws_iam_role.eks_node_role.arn
  subnet_ids      = aws_subnet.public[*].id

  scaling_config {
    desired_size = 1
    max_size     = 2
    min_size     = 1
  }

  instance_types = [var.node_instance_type]
  force_update_version = true

  depends_on = [
    aws_iam_role_policy_attachment.node_AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.node_AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.node_ECRReadOnly
  ]
}
