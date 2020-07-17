from app.link.models import Link

def increment_descendent_counts(parent_link_id):
    oldLink = Link.incrementField(parent_link_id, "total_descendants")
    if oldLink.parent_id != None:
        increment_descendent_counts(oldLink.parent_id)

def increment_child_counts(parent_link_id):
    Link.incrementField(parent_link_id, "total_children")

def update_depth(parent_link_id, depth=1):
    link = Link.queryById(parent_link_id)
    if link.total_depth < depth:
        oldLink = Link.setField(parent_link_id, "total_depth", depth)
        if link.parent_id != None:
            update_depth(link.parent_id, depth=depth + 1)