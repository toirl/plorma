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
%>
<%def name="render_task(task)">
  <div class="taskcard">
    <div class="taskcard-label">
      <div class="taskcard-issueno"><a
          href="${request.route_path(h.get_action_routename(task, 'update'),
          id=item.id, _query={'backurl': request.current_route_path()})}"><i class="glyphicon glyphicon-edit"></i></a></div>
      <div class="taskcard-estimate pull-right"><i class="fa fa-clock-o"></i> 
        % if task.estimate != None:
          ${_(task.get_value('estimate', expand=True))}
        % else:
          <span class="text-danger">${_('Unknown')}</span>
        % endif
      </div>
    </div>
    <div class="taskcard-content">
      <strong>#${task.id}:</strong>
      ${task.name}
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

<div class="container">
<h1>${item.title} (${h.prettify(request, item.start)} – ${h.prettify(request, item.end)})</h1>
  <div class="row">
    <div class="col-md-12">
      <table class="table sprintboard">
        <thead>
          <tr>
            <th>${_('Open')}</th>
            <th>${_('In Progress')}</th>
            <th>${_('Done')}</th>
            <th>${_('Verified')}</th>
            <th>${_('Closed')}</th>
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
            <th>${_('Open')}</th>
            <th>${_('In Progress')}</th>
            <th>${_('Done')}</th>
            <th>${_('Verified')}</th>
            <th>${_('Closed')}</th>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>
</div>
