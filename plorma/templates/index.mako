<%inherit file="/main.mako" />
<%
mapping={'app_title': h.get_app_title()}
%>
<%def name="render_task(task)">
<a href="${request.route_path(h.get_action_routename(task, 'update'), id=task.id)}">
  <span class="label label-default">
     ${task}
     % if task.assignee:
     (${task.estimate} , ${task.assignee})
     % else:
     (${task.estimate})
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
      <h3>${sprint.title} (${h.prettify(request, sprint.start)} - ${h.prettify(request, sprint.end)})
        % if s.has_permission("update", sprint, request):
          <a class="btn btn-default" href="${request.route_path(h.get_action_routename(sprint, 'update'), id=sprint.id)}"><i class="glyphicon glyphicon-edit"></i></a>
        % else:
          <a class="btn btn-default"
            href="${request.route_path(h.get_action_routename(sprint, 'read'), id=sprint.id)}"><i class="glyphicon glyphicon-eye-open"></i></a>
        % endif
    </h3>
    <div class="row">
      <div class="col-md-9">
        <embed src="${request.route_path('renderburndown', id=sprint.id)}"  type="image/svg+xml"/>
      </div>
      <div class="col-md-3">
        <table class="table">
          <tr>
            <td>${_('Strength')}</td>
            <td>${sprint.strength}</td>
          </tr>
          <tr>
            <td>${_('Initial Story Points')}</td>
            <td>${sprint.size}</td>
          </tr>
          <tr>
            <td>${_('Remaining Story Points')}</td>
            <td>${sprint.estimate}</td>
          </tr>
          <tr>
            <td>${_('Velocity')}</td>
            <td>${sprint.velocity}</td>
          </tr>
          <tr>
            <td colspan="2">
              <a class="btn btn-default btn-block" href="${request.route_path(h.get_action_routename(sprint, 'board'), id=sprint.id)}"><i class="fa fa-table"></i> ${_('Open Sprintboard')}</a>
            </td>
          </tr>
        </table>
      </div>
    </div>
    ##<div class="row">
    ##  <div class="col-md-12">
    ##    <table class="table table-striped table-bordered">
    ##      <tr>
    ##         <th>${_('Open')}</th>
    ##         <th>${_('Assigned')}</th>
    ##         <th>${_('Testable')}</th>
    ##         <th>${_('Finished')}</th>
    ##      </tr>
    ##      <%
    ##        open_tasks = []
    ##        assigned_tasks = []
    ##        testable_tasks = []
    ##        finished_tasks = []
    ##        for task in sprint.tasks:
    ##          if task.task_state_id in [1,2,7]:
    ##            open_tasks.append(task)
    ##          elif task.task_state_id in [3]:
    ##            assigned_tasks.append(task)
    ##          elif task.task_state_id in [4]:
    ##            testable_tasks.append(task)
    ##          elif task.task_state_id in [5,6]:
    ##            finished_tasks.append(task)
    ##      %>
    ##      <tr>
    ##         <td>
    ##           % for task in open_tasks:
    ##             ${render_task(task)}
    ##           % endfor
    ##         </td>
    ##         <td>
    ##           % for task in assigned_tasks:
    ##             ${render_task(task)}
    ##           % endfor
    ##         </td>
    ##         <td>
    ##           % for task in testable_tasks:
    ##             ${render_task(task)}
    ##           % endfor
    ##         </td>
    ##         <td>
    ##           % for task in finished_tasks:
    ##             ${render_task(task)}
    ##           % endfor
    ##         </td>
    ##      </tr>
    ##    </table>
    ##  </div>
    ##</div>
    % endfor
  </div>
% endif
