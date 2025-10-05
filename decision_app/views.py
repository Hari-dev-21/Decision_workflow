from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from decision_app.forms import Edgeform, Nodeform, Workflowform
from .models import Workflow, Node, Edge



def workflow_list(request):
    workflows = Workflow.objects.all()

    return render(request, 'decision_app/workflow_list.html', {'workflows' : workflows} )

def workflow_detail(request, workflow_id):

    workflow = get_object_or_404(Workflow, id=workflow_id)

    nodes = Node.objects.filter(workflow=workflow)

    edges = Edge.objects.filter(from_node__workflow=workflow)

    context = {
        'workflow' : workflow,
        'nodes' : nodes,
        'edges' : edges

    }
    return render(request, 'decision_app/workflow_detail.html', context)
@login_required
def add_workflow(request):

    if request.method == 'POST':
        form = Workflowform(request.POST)
        if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = Workflowform()
    return render(request, 'decision_app/add_workflow.html', {'form':form })   


def add_node(request, workflow_id):

    workflow = get_object_or_404(Workflow, id = workflow_id)
    if request.method == 'POST':

        form = Nodeform(request.POST)
        if form.is_valid():
            node = form.save(commit=False)
            node.workflow = workflow
            node.save()
            return redirect('workflow_detail', workflow_id=workflow.id)

    else:
        form = Nodeform()

    return render(request, 'decision_app/add_node.html', {'form': form, 'workflow': workflow})           


def add_edge(request, workflow_id):

    workflow = get_object_or_404(Workflow, id=workflow_id)

    from_nodes = Node.objects.filter(workflow=workflow)
    to_nodes = Node.objects.filter(workflow=workflow)


    if request.method == 'POST':
        form = Edgeform(request.POST)
               
    else:
        form = Edgeform()

    form.fields['from_node'].queryset = from_nodes
    form.fields['to_node'].queryset = to_nodes  

    if request.method == 'POST' and form.is_valid():
        edge = form.save(commit=False)
        edge.workflow = workflow 
        edge.save()
        return redirect('workflow_detail', workflow_id=workflow.id)
          
           
    return render(request, 'decision_app/add_edge.html', {'form': form, 'workflow': workflow})    

def delete_workflow(request, workflow_id):
    workflow = get_object_or_404(Workflow, id=workflow_id)

    workflow.delete()

    return redirect('workflow_list')


def start_workflow(request, workflow_id):
    workflow = get_object_or_404(Workflow, id=workflow_id)

    try:
        start_node = Node.objects.get(workflow=workflow, is_start = True)

        return redirect('view_node', node_id=start_node.id)

    except Node.DoesNotExist:
        raise Http404("This workflow has no starting node defined.") 


def view_node(request, node_id):
    node = get_object_or_404(Node, id=node_id)
    edges = Edge.objects.filter(from_node = node)

    if node.is_end and not edges.exists():
        return render(request, 'decision_app/result.html', {'node': node})
    
    return render(request, 'decision_app/view_node.html', {
        'node': node,
        'edges': edges
    })


def visualize_workflow(request, workflow_id):
    workflow = get_object_or_404(Workflow, id=workflow_id)
    nodes = Node.objects.filter(workflow=workflow)
    edges = Edge.objects.filter(workflow=workflow)

    for node in nodes:
        if node.is_start:
            node.color = '#90ee90'  # light green
        elif node.is_end:
            node.color = '#ffcccb'  # light red
        else:
            node.color = '#d0d0ff'  # light blue

    return render(request, 'decision_app/visualize.html', {
        'workflow': workflow,
        'nodes': nodes,
        'edges': edges
    })

