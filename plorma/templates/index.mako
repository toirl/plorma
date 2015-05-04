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
  % for sprint in sprints:
  <h2>${_('Sprint')}: ${sprint}</h2>
  <div class="row">
    <div class="col-md-8">
      <embed src="${request.route_path('renderburndown', id=sprint.id)}"  type="image/svg+xml"/><br>
    </div>
    <div class="col-md-4">
      <table class="table">
        <tr>
          <td>${_('Strengh')}</td>
          <td>${sprint.strength}</td>
        </tr>
        <tr>
          <td>${_('Estimate')}</td>
          <td>${sprint.estimate}</td>
        </tr>
        <tr>
          <td>${_('Velocity')}</td>
          <td>0.42</td>
        </tr>
        <tr>
          <td>${_('Tasks')} <span class="badge">0</span></td>
          <td>
            <ul class="list-unstyled">
              <li>Unassigned <span class="badge">0</span></li>
              <li>Progress <span class="badge">0</span></li>
              <li>Testable <span class="badge">0</span></li>
              <li>Finished <span class="badge">0</span></li>
            </ul>
        </tr>
      </table>
      <a class="btn btn-default" href="${request.route_path(h.get_action_routename(sprint, 'update'), id=sprint.id)}">${_("Update")}</a>
      <a class="btn btn-default" href="${request.route_path(h.get_action_routename(sprint, 'update'), id=sprint.id)}">${_("Recalculate")}</a>

    </div>
  </div>
  % endfor
  </div>
% endif
