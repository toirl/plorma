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
% endif
