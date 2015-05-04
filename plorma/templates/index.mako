<%inherit file="/main.mako" />
<%
mapping={'app_title': h.get_app_title()}
%>
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
            velocity = round((float(done)/sprint.strength))
          %>
          <td>${_('Velocity')}</td>
          <td>${velocity}</td>
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
      <table class="table">
        <tr>
          <th width="150">Story (${sprint.estimate})</th>
           <th>${_('Open')}</th>
           <th>${_('Assigned')}</th>
           <th>${_('Testable')}</th>
           <th>${_('Finished')}</th>
        </tr>
        % for task in sprint.tasks:
        <tr>
           <th>
            <a href="${request.route_path(h.get_action_routename(task, 'read'), id=task.id)}">${task}</a> (${task.estimate})
           </th>
           <th></th>
           <th></th>
           <th></th>
           <th></th>
        </tr>
        % endfor
      </table>
    </div>
  </div>
  % endfor
  </div>
% endif
