resource "aws_ecr_repository" "backend" {
  name = "${var.cluster_name}-backend"
  image_scanning_configuration { scan_on_push = true }
  tags = { Owner = var.owner }
}

resource "aws_ecr_repository" "frontend" {
  name = "${var.cluster_name}-frontend"
  image_scanning_configuration { scan_on_push = true }
  tags = { Owner = var.owner }
}
