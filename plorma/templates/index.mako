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
    <div class="row">
      <div class="col-md-12">
        <h2>${_("Workbench")}
          <%
            open_tasks = [t for t in request.user.tasks if t.task_state_id != 6]
            open_tasks.sort(key=lambda x: x.weight or -1, reverse=True)
            top_tasks = open_tasks[0:5]
            num_tasks = len(open_tasks)
          %>
          % if num_tasks < 5:
            <span class="label label-success">${num_tasks}</span>
          % elif num_tasks <= 10:
            <span class="label label-warning">${num_tasks}</span>
          % else:
            <span class="label label-danger">${num_tasks}</span>
          % endif
        </h2>
        <table class="table">
          <tr>
            <th>${_('Task')}</th>
            <th>${_('Priority')}</th>
            <th><span class="sr-only">${_('Action')}</span></th>
          </tr>
          % for task in top_tasks:
            <tr>
              <td><a href="${request.route_path(h.get_action_routename(task, "update"), id=task.id)}">${task}</td>
              <td>${task.weight}</td>
              <td></td>
            </tr>
          % endfor
        </table>
      </div>
      ##<div class="col-md-6">
      ##  <h2>${_("Stats")}
      ##</div>
    </div>
    <h2>${_("Sprints")}</h2>
    % if len(sprints) == 0:
      ${_('No sprints available.')}
    % endif
    % for sprint in sprints:
      <h3>${sprint.title} (${h.prettify(request, sprint.start)} - ${h.prettify(request, sprint.end)})</h3>
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
    % endfor
  </div>
% endif
