from django.db import models
from django.contrib.auth.models import User

class Workflow(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Node(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='nodes')
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_start = models.BooleanField(default=False)
    is_end = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (Workflow: {self.workflow.name})"



class Edge(models.Model):
    from_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='outgoing_edges')
    to_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='incoming_edges')
    condition = models.CharField(max_length=200)
    workflow = models.ForeignKey(Workflow, related_name='edges', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_node.title} → {self.to_node.title} ({self.condition or 'no condition'})"


