from app.link.models import Link

def increment_descendent_counts(parent_link_id):
    link = Link.queryById(parent_link_id)
    link.total_descendants += 1
    link.save()
    if link.parent_id == None:
        return
    else:
        increment_descendent_counts(link.parent_id)

def increment_child_counts(parent_link_id):
    link = Link.queryById(parent_link_id)
    link.total_children += 1
    link.save()
