<%inherit file="/main.mako" />
<%
mapping={'app_title': h.get_app_title()}
%>
<%def name="render_task(task)">
<a href="${request.route_path(h.get_action_routename(task, 'update'), id=task.id)}">
  <span class="label label-default">
     % if len(task.children) > 0:
       <i>${task}
         (<s>${task.total_estimate}</s>)</i>
     % else:
       ${task}
       % if task.assignee:
       (${task.total_estimate} , ${task.assignee})
       % else:
       (${task.total_estimate})
       % endif
     % endif
  </span>
</a>&nbsp;
</%def>
% if not request.user:
  <h1>${_('Welcome to ${app_title}!', mapping=mapping)}</h1>
  <div class="page-header"></div>
  <p>Plorma is a webapplication to <strong>pl</strong>an,
    <strong>or</strong>ganise and <strong>ma</strong>nage tasks.</p>
<a href="${request.route_path('login')}" class="btn btn-primary btn-large" title="${_('Login in the application')}">${_('Login')}</a>
% else:
  <h1>${_('Home')}</h1>
  <div class="page-header"></div>
  <div class="container-fluid">
  <h2>${_('Sprints')}</h2>
    % if len(sprints) == 0:
      ${_('No sprints available.')}
    % endif
  % for sprint in sprints:
  <h3>${sprint}
      % if s.has_permission("update", sprint, request):
        <a class="btn btn-default" href="${request.route_path(h.get_action_routename(sprint, 'update'), id=sprint.id)}">${_("Update")}</a>
      % else:
        <a class="btn btn-default" href="${request.route_path(h.get_action_routename(sprint, 'read'), id=sprint.id)}">${_("Read")}</a>
      % endif
  </h3>
  <div class="row">
    <div class="col-md-6">
    </div>
    <div class="col-md-6">
    </div>
  </div>
  <div class="row">
    <div class="col-md-8">
      <embed src="${request.route_path('renderburndown', id=sprint.id)}"  type="image/svg+xml"/><br>
    </div>
    <div class="col-md-4">
      <table class="table">
        <tr>
          <td>${_('Strength')}</td>
          <td>${sprint.strength}</td>
        </tr>
        <tr>
          <td>${_('Estimate')}</td>
          <%
            total = sprint.estimatelog[0].estimate
            current = sprint.estimatelog[-1].estimate
            done = total - current
            if not total:
              total = 1
            ready = round(float(done)/float(total)*100)
          %>
          <td>${current}/${total}/${done} (${ready}%)</td>
        </tr>
        <tr>
          <%
            velocity = (float(done)/float(sprint.strength))*100
          %>
          <td>${_('Velocity')}</td>
          <td>${done}/${sprint.strength} (${velocity}%)</td>
        </tr>
        <tr>
          <td>${_('Tasks')} <span class="badge">${len(sprint.get_tasks())}</span></td>
          <td>
            <ul class="list-unstyled">
              <li>${_('Open')} <span class="badge">${len(sprint.get_tasks('open'))}</span></li>
              <li>${_('Assigned')} <span class="badge">${len(sprint.get_tasks('progress'))}</span></li>
              <li>${_('Testable')} <span class="badge">${len(sprint.get_tasks('testable'))}</span></li>
              <li>${_('Finished')} <span class="badge">${len(sprint.get_tasks('finished'))}</span></li>
            </ul>
        </tr>
      </table>
    </div>
  </div>
  <h4>${_('Sprintboard')}</h4>
  <div class="row">
    <div class="col-md-12">
      <table class="table table-striped table-bordered">
        <tr>
          <th width="200">Story (${sprint.estimate})</th>
           <th>${_('Open')}</th>
           <th>${_('Assigned')}</th>
           <th>${_('Testable')}</th>
           <th>${_('Finished')}</th>
        </tr>
        % for task in sprint.tasks:
        <%
          subtasks = task.get_children()
          open_tasks = []
          assigned_tasks = []
          testable_tasks = []
          finished_tasks = []
          for stask in subtasks:
            if stask.task_state_id in [1,2,7]:
              open_tasks.append(stask)
            elif stask.task_state_id in [3]:
              assigned_tasks.append(stask)
            elif stask.task_state_id in [4]:
              testable_tasks.append(stask)
            elif stask.task_state_id in [5,6]:
              finished_tasks.append(stask)
        %>
        <tr>
           <td>
             <strong><a href="${request.route_path(h.get_action_routename(task, 'update'), id=task.id)}">${task}</a> (${task.total_estimate})</strong>
           </td>
           <td>
             % for stask in open_tasks:
               ${render_task(stask)}
             % endfor
           </td>
           <td>
             % for stask in assigned_tasks:
               ${render_task(stask)}
             % endfor
           </td>
           <td>
             % for stask in testable_tasks:
               ${render_task(stask)}
             % endfor
           </td>
           <td>
             % for stask in finished_tasks:
               ${render_task(stask)}
             % endfor
           </td>
        </tr>
        % endfor
      </table>
    </div>
  </div>
  % endfor
  </div>
% endif
