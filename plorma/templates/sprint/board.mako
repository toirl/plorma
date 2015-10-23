## encoding: utf-8

<%inherit file="/base.mako" />
<%
  open_tasks = []
  assigned_tasks = []
  testable_tasks = []
  verified_tasks = []
  finished_tasks = []
  for task in item.tasks:
    if task.task_state_id in [1,2,7]:
      open_tasks.append(task)
    elif task.task_state_id in [3]:
      assigned_tasks.append(task)
    elif task.task_state_id in [4]:
      testable_tasks.append(task)
    elif task.task_state_id in [5]:
      verified_tasks.append(task)
    elif task.task_state_id in [6]:
      finished_tasks.append(task)
  open_estimate = sum([int(t.get_value('estimate', expand=True) or 0) for t in open_tasks])
  assigend_estimate = sum([int(t.get_value('estimate', expand=True) or 0) for t in assigned_tasks])
  testable_estimate = sum([int(t.get_value('estimate', expand=True) or 0) for t in testable_tasks])
  verified_estimate = sum([int(t.get_value('estimate', expand=True) or 0) for t in verified_tasks])
  finished_estimate = sum([int(t.get_value('estimate', expand=True) or 0) for t in finished_tasks])
%>
<%def name="render_task(task)">
  <div class="taskcard">
    <div class="taskcard-label">
      <div class="taskcard-issueno"><a href="${request.route_path(h.get_action_routename(task, 'update'), id=task.id, _query={'backurl': request.current_route_path()})}"><i class="glyphicon glyphicon-edit"></i></a></div>
      <div class="taskcard-estimate pull-right"><i class="fa fa-clock-o"></i> 
        % if task.estimate != None:
          ${_(task.get_value('estimate', expand=True))}
        % else:
          <span class="text-danger">${_('Unknown')}</span>
        % endif
      </div>
    </div>
    <div class="taskcard-content">
      <a href="${request.route_path(h.get_action_routename(task, 'update'), id=task.id, _query={'backurl': request.current_route_path(), 'form': 'taskcard'})}">
        <strong>#${task.id}:</strong>
        ${task.name}
      </a>
    </div>
    <div class="taskcard-footer">
      <div class="taskcard-status">
        <strong>${_('Assigned')}:</strong>
        % if task.assignee:
          ${task.assignee}
        % else:
          <span class="text-danger">${_('No')}</span>
        % endif
        % if task.task_state_id in [4]:
          </br><strong>${_('Resolution')}:</strong> ${_(task.get_value('resolution', expand=True))}
        % endif
      </div>
    </div>
  </div>
</%def>

<div class="container-fluid">
<h1>${item.title} (${h.prettify(request, item.start)} – ${h.prettify(request,
  item.end)}) <span class="pull-right">${item.estimate}/${item.size}</span></h1>
  <div class="row">
    <div class="col-md-12">
      <table class="table sprintboard">
        <thead>
          <tr>
            <th>${_('Open')} (${open_estimate})</th>
            <th>${_('In Progress')} (${assigend_estimate})</th>
            <th>${_('Done')} (${testable_estimate})</th>
            <th>${_('Verified')} (${verified_estimate})</th>
            <th>${_('Closed')} (${finished_estimate})</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              %for task in open_tasks:
                ${render_task(task)}
              %endfor
            </td>
            <td>
              %for task in assigned_tasks:
                ${render_task(task)}
              %endfor
            </td>
            <td>
              %for task in testable_tasks:
                ${render_task(task)}
              %endfor
            </td>
            <td>
              %for task in verified_tasks:
                ${render_task(task)}
              %endfor
            </td>
            <td>
              %for task in finished_tasks:
                ${render_task(task)}
              %endfor
            </td>
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <th>${_('Open')} (${open_estimate})</th>
            <th>${_('In Progress')} (${assigend_estimate})</th>
            <th>${_('Done')} (${testable_estimate})</th>
            <th>${_('Verified')} (${verified_estimate})</th>
            <th>${_('Closed')} (${finished_estimate})</th>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>
</div>
