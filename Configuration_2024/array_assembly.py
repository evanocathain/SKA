





<!DOCTYPE html>
<html class="gl-light ui-neutral with-top-bar with-header " lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="width=device-width, initial-scale=1" name="viewport">
<title>src/ska_ost_array_config/array_assembly.py · master · SKAO / Observatory Support Tools / ska-ost-array-config · GitLab</title>
<script nonce="CQaS6OefbNR/UGnCo9kvFg==">
//<![CDATA[
window.gon={};gon.math_rendering_limits_enabled=true;gon.features={"inlineBlame":false,"blobOverflowMenu":true,"filterBlobPath":true,"blobRepositoryVueHeaderApp":true,"directoryCodeDropdownUpdates":true,"repositoryFileTreeBrowser":false,"repositoryLockInformation":false};gon.licensed_features={"fileLocks":true,"remoteDevelopment":true};
//]]>
</script>


<script nonce="CQaS6OefbNR/UGnCo9kvFg==">
//<![CDATA[
var gl = window.gl || {};
gl.startup_calls = null;
gl.startup_graphql_calls = [{"query":"query getBlobInfo(\n  $projectPath: ID!\n  $filePath: [String!]!\n  $ref: String!\n  $refType: RefType\n  $shouldFetchRawText: Boolean!\n) {\n  project(fullPath: $projectPath) {\n    __typename\n    id\n    repository {\n      __typename\n      empty\n      blobs(paths: $filePath, ref: $ref, refType: $refType) {\n        __typename\n        nodes {\n          __typename\n          id\n          webPath\n          name\n          size\n          rawSize\n          rawTextBlob @include(if: $shouldFetchRawText)\n          fileType\n          language\n          path\n          blamePath\n          editBlobPath\n          gitpodBlobUrl\n          ideEditPath\n          forkAndEditPath\n          ideForkAndEditPath\n          codeNavigationPath\n          projectBlobPathRoot\n          forkAndViewPath\n          environmentFormattedExternalUrl\n          environmentExternalUrlForRouteMap\n          canModifyBlob\n          canModifyBlobWithWebIde\n          canCurrentUserPushToBranch\n          archived\n          storedExternally\n          externalStorage\n          externalStorageUrl\n          rawPath\n          replacePath\n          pipelineEditorPath\n          simpleViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n          richViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n        }\n      }\n    }\n  }\n}\n","variables":{"projectPath":"ska-telescope/ost/ska-ost-array-config","ref":"master","refType":null,"filePath":"src/ska_ost_array_config/array_assembly.py","shouldFetchRawText":true}}];

if (gl.startup_calls && window.fetch) {
  Object.keys(gl.startup_calls).forEach(apiCall => {
   gl.startup_calls[apiCall] = {
      fetchCall: fetch(apiCall, {
        // Emulate XHR for Rails AJAX request checks
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
        // fetch won’t send cookies in older browsers, unless you set the credentials init option.
        // We set to `same-origin` which is default value in modern browsers.
        // See https://github.com/whatwg/fetch/pull/585 for more information.
        credentials: 'same-origin'
      })
    };
  });
}
if (gl.startup_graphql_calls && window.fetch) {
  const headers = {"X-CSRF-Token":"qvMHVL5NCmu0OKZFr7EivGqbyoaWOtzRdNb6ULT98tvdNy-41wBDv4MdtXIQBu-g8gmluhnVnjRqI0nqjLIehw","x-gitlab-feature-category":"source_code_management"};
  const url = `https://gitlab.com/api/graphql`

  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headers,
    }
  };

  gl.startup_graphql_calls = gl.startup_graphql_calls.map(call => ({
    ...call,
    fetchCall: fetch(url, {
      ...opts,
      credentials: 'same-origin',
      body: JSON.stringify(call)
    })
  }))
}


//]]>
</script>

<link rel="prefetch" href="/assets/webpack/monaco.e7302a17.chunk.js">

<link rel="stylesheet" href="/assets/application-6c8d471f1c2ea927c1cd2cf3c11b01964209bc82df6cc7e82d1cad6c42e4a824.css" />
<link rel="stylesheet" href="/assets/page_bundles/tree-0e21620e4f6de54309b03fef4b9c6f3d864fe68e4348ae075b0279f8ec03b2ff.css" /><link rel="stylesheet" href="/assets/page_bundles/projects-4ae0e1c17bb9215c0e20e1d00a7e46c3dc94b5452f3c1e50fb0b2199914d6a70.css" /><link rel="stylesheet" href="/assets/page_bundles/commit_description-1e2cba4dda3c7b30dd84924809020c569f1308dea51520fe1dd5d4ce31403195.css" /><link rel="stylesheet" href="/assets/page_bundles/work_items-baef88486741448f99cd3389dc6b0f7233bc4f390ee9d0732c78c412710e24e3.css" /><link rel="stylesheet" href="/assets/page_bundles/notes_shared-a4a075916eb03f69149eba8eaf8b8060cdc5a133c37fa9d2aa61ea06604e1104.css" />
<link rel="stylesheet" href="/assets/application_utilities-f77f86f78d4146d4c2c821bc481cee77b897df284886ad189d8dcb1234cb9651.css" />
<link rel="stylesheet" href="/assets/tailwind-2f1576c6086ebbf05c278b85c833a7e4c7f1af80a564dc6d8fd111f9a0a05cf8.css" />


<link rel="stylesheet" href="/assets/fonts-fae5d3f79948bd85f18b6513a025f863b19636e85b09a1492907eb4b1bb0557b.css" />
<link rel="stylesheet" href="/assets/highlight/themes/white-4e2c1d00201832e6644c05ac01bd0bc4dae44d5d8cc10318f8b5adfb9f9bd562.css" />

<script src="/assets/webpack/runtime.d84d4603.bundle.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/main.9e57df68.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/tracker.8152d0f8.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/analytics.56c98ff1.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script nonce="CQaS6OefbNR/UGnCo9kvFg==">
//<![CDATA[
window.snowplowOptions = {"namespace":"gl","hostname":"snowplowprd.trx.gitlab.net","cookieDomain":".gitlab.com","appId":"gitlab","formTracking":true,"linkClickTracking":true}

gl = window.gl || {};
gl.snowplowStandardContext = {"schema":"iglu:com.gitlab/gitlab_standard/jsonschema/1-1-6","data":{"environment":"production","source":"gitlab-rails","correlation_id":"01JVZBFKD3SVJ30VFAAAD2G84R","plan":"gold","extra":{},"user_id":null,"global_user_id":null,"is_gitlab_team_member":null,"namespace_id":55066354,"ultimate_parent_namespace_id":3180705,"project_id":46018736,"feature_enabled_by_namespace_ids":null,"realm":"saas","instance_id":"ea8bf810-1d6f-4a6a-b4fd-93e8cbd8b57f","unique_instance_id":"b5fa1911-0638-5651-8ec4-5b892ef92e35","host_name":"gitlab.com","instance_version":"18.1.0","context_generated_at":"2025-05-23T19:56:21.034Z"}}
gl.snowplowPseudonymizedPageUrl = "https://gitlab.com/namespace55066354/project46018736/-/blob/:repository_path";
gl.maskedDefaultReferrerUrl = null;
gl.ga4MeasurementId = 'G-ENFH3X7M5Y';
gl.duoEvents = ["ai_question_category","perform_completion_worker","process_gitlab_duo_question","ai_response_time","click_purchase_seats_button_group_duo_pro_home_page","default_answer","detected_high_comment_temperature","detected_repeated_high_comment_temperature","error_answer","execute_llm_method","finish_duo_workflow_execution","forced_high_temperature_commenting","i_quickactions_q","request_ask_help","request_duo_chat_response","requested_comment_temperature","retry_duo_workflow_execution","start_duo_workflow_execution","submit_gitlab_duo_question","tokens_per_embedding","tokens_per_user_request_prompt","tokens_per_user_request_response"];
gl.onlySendDuoEvents = false;


//]]>
</script>
<link rel="preload" href="/assets/application_utilities-f77f86f78d4146d4c2c821bc481cee77b897df284886ad189d8dcb1234cb9651.css" as="style" type="text/css" nonce="Url54Gf9dFc9ME2Ds5vxBA==">
<link rel="preload" href="/assets/application-6c8d471f1c2ea927c1cd2cf3c11b01964209bc82df6cc7e82d1cad6c42e4a824.css" as="style" type="text/css" nonce="Url54Gf9dFc9ME2Ds5vxBA==">
<link rel="preload" href="/assets/highlight/themes/white-4e2c1d00201832e6644c05ac01bd0bc4dae44d5d8cc10318f8b5adfb9f9bd562.css" as="style" type="text/css" nonce="Url54Gf9dFc9ME2Ds5vxBA==">
<link crossorigin="" href="https://snowplowprd.trx.gitlab.net" rel="preconnect">
<link as="font" crossorigin="" href="/assets/gitlab-sans/GitLabSans-1e0a5107ea3bbd4be93e8ad2c503467e43166cd37e4293570b490e0812ede98b.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-sans/GitLabSans-Italic-38eaf1a569a54ab28c58b92a4a8de3afb96b6ebc250cf372003a7b38151848cc.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-mono/GitLabMono-08d2c5e8ff8fd3d2d6ec55bc7713380f8981c35f9d2df14e12b835464d6e8f23.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-mono/GitLabMono-Italic-38e58d8df29485a20c550da1d0111e2c2169f6dcbcf894f2cd3afbdd97bcc588.woff2" rel="preload">
<link rel="preload" href="/assets/fonts-fae5d3f79948bd85f18b6513a025f863b19636e85b09a1492907eb4b1bb0557b.css" as="style" type="text/css" nonce="Url54Gf9dFc9ME2Ds5vxBA==">



<script src="/assets/webpack/sentry.8635a9c8.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>

<script src="/assets/webpack/commons-pages.admin.application_settings.service_accounts-pages.groups.analytics.dashboards-pages.gr-bf1d34a4.361e357e.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/commons-pages.search.show-super_sidebar.09856253.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/super_sidebar.3b9b9865.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-6b2e0f2b.0717aae8.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/4.753e28e0.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/commons-pages.admin.abuse_reports.show-pages.admin.topics.edit-pages.admin.topics.new-pages.groups.c-f0e34798.7fde970b.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/commons-pages.groups.packages-pages.groups.registry.repositories-pages.groups.security.policies.edit-429ebfda.33c57e6f.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/38.ad9c2367.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/105.6803a0fe.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/126.1aa6c516.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/125.8e415383.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show-pages.projects.tre-c684fcf6.9d2ae295.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.commit.show-pages.projects.merge_requests.rapid_diff-e17e687c.c78aef53.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/commons-pages.groups.show-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.4f4f8661.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.2fa6d6ac.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.tree.show.f34ae232.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>
<script src="/assets/webpack/pages.projects.blob.show.f37c9401.chunk.js" defer="defer" nonce="CQaS6OefbNR/UGnCo9kvFg=="></script>

<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="src/ska_ost_array_config/array_assembly.py · master · SKAO / Observatory Support Tools / ska-ost-array-config · GitLab" property="og:title">
<meta content="ska-ost-array-config" property="og:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://gitlab.com/ska-telescope/ost/ska-ost-array-config/-/blob/master/src/ska_ost_array_config/array_assembly.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="src/ska_ost_array_config/array_assembly.py · master · SKAO / Observatory Support Tools / ska-ost-array-config · GitLab" property="twitter:title">
<meta content="ska-ost-array-config" property="twitter:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="twitter:image">

<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="AklnqEy9GBDMRMLWBZVExC9FVg-QKRxUdVA47vXQHx11jU9EJfBRxPth0eG6IonYt9c5Mx_GXrFrpYtUzZ_zQQ" />
<meta name="csp-nonce" content="CQaS6OefbNR/UGnCo9kvFg==" />
<meta name="action-cable-url" content="/-/cable" />
<link href="/-/manifest.json" rel="manifest">
<link rel="icon" type="image/png" href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" id="favicon" data-original-href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/apple-touch-icon-b049d4bc0dd9626f31db825d61880737befc7835982586d015bded10b4435460.png" />
<link href="/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml">




<meta content="ska-ost-array-config" name="description">
<meta content="#ececef" name="theme-color">
</head>

<body class="tab-width-8 gl-browser-generic gl-platform-other body-fixed-scrollbar" data-group="ost" data-group-full-path="ska-telescope/ost" data-namespace-id="55066354" data-page="projects:blob:show" data-page-type-id="master/src/ska_ost_array_config/array_assembly.py" data-project="ska-ost-array-config" data-project-full-path="ska-telescope/ost/ska-ost-array-config" data-project-id="46018736">
<div id="js-tooltips-container"></div>

<script nonce="CQaS6OefbNR/UGnCo9kvFg==">
//<![CDATA[
gl = window.gl || {};
gl.client = {"isGeneric":true,"isOther":true};


//]]>
</script>


<header class="header-logged-out" data-testid="navbar">
<a class="gl-sr-only gl-accessibility" href="#content-body">Skip to content</a>
<div class="container-fluid">
<nav aria-label="Explore GitLab" class="header-logged-out-nav gl-flex gl-gap-3 gl-justify-between">
<div class="gl-flex gl-items-center gl-gap-1">
<span class="gl-sr-only">GitLab</span>
<a title="Homepage" id="logo" class="header-logged-out-logo has-tooltip" aria-label="Homepage" data-track-label="main_navigation" data-track-action="click_gitlab_logo_link" data-track-property="navigation_top" href="/"><svg aria-hidden="true" role="img" class="tanuki-logo" width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path class="tanuki-shape tanuki" d="m24.507 9.5-.034-.09L21.082.562a.896.896 0 0 0-1.694.091l-2.29 7.01H7.825L5.535.653a.898.898 0 0 0-1.694-.09L.451 9.411.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 2.56 1.935 1.554 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z"
        fill="#E24329"/>
  <path class="tanuki-shape right-cheek" d="m24.507 9.5-.034-.09a11.44 11.44 0 0 0-4.56 2.051l-7.447 5.632 4.742 3.584 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z"
        fill="#FC6D26"/>
  <path class="tanuki-shape chin" d="m7.707 20.677 2.56 1.935 1.555 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935-4.743-3.584-4.755 3.584Z"
        fill="#FCA326"/>
  <path class="tanuki-shape left-cheek" d="M5.01 11.461a11.43 11.43 0 0 0-4.56-2.05L.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 4.745-3.584-7.444-5.632Z"
        fill="#FC6D26"/>
</svg>

</a></div>
<ul class="gl-list-none gl-p-0 gl-m-0 gl-flex gl-gap-3 gl-items-center gl-grow">
<li class="header-logged-out-nav-item header-logged-out-dropdown md:gl-hidden">
<button class="header-logged-out-toggle" data-toggle="dropdown" type="button">
<span class="gl-sr-only">
Menu
</span>
<svg class="s16" data-testid="hamburger-icon"><use href="/assets/icons-1dc8580f14b5de4dcf11c6c7326e55d1b3fb7c05afa8655c3f51c47ac154a434.svg#hamburger"></use></svg>
</button>
<div class="dropdown-menu">
<ul>
<li>
<a href="https://about.gitlab.com/why-gitlab">Why GitLab
</a></li>
<li>
<a href="https://about.gitlab.com/pricing">Pricing
</a></li>
<li>
<a href="https://about.gitlab.com/sales">Contact Sales
</a></li>
<li>
<a href="/explore">Explore</a>
</li>
</ul>
</div>
</li>
<li class="header-logged-out-nav-item gl-hidden md:gl-inline-block">
<a href="https://about.gitlab.com/why-gitlab">Why GitLab
</a></li>
<li class="header-logged-out-nav-item gl-hidden md:gl-inline-block">
<a href="https://about.gitlab.com/pricing">Pricing
</a></li>
<li class="header-logged-out-nav-item gl-hidden gl-inline-block">
<a href="https://about.gitlab.com/sales">Contact Sales
</a></li>
<li class="header-logged-out-nav-item gl-hidden md:gl-inline-block">
<a class="" href="/explore">Explore</a>
</li>
</ul>
<ul class="gl-list-none gl-p-0 gl-m-0 gl-flex gl-gap-3 gl-items-center gl-justify-end">
<li class="header-logged-out-nav-item">
<a href="/users/sign_in?redirect_to_referer=yes">Sign in</a>
</li>
<li class="header-logged-out-nav-item">
<a class="gl-button btn btn-md btn-confirm !gl-inline-flex" href="/users/sign_up"><span class="gl-button-text">
Get free trial

</span>

</a></li>
</ul>
</nav>
</div>
</header>

<div class="layout-page page-with-super-sidebar">
<aside class="js-super-sidebar super-sidebar super-sidebar-loading" data-command-palette="{&quot;project_files_url&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/files/master?format=json&quot;,&quot;project_blob_url&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/blob/master&quot;}" data-force-desktop-expanded-sidebar="" data-is-saas="true" data-root-path="/" data-sidebar="{&quot;whats_new_most_recent_release_items_count&quot;:5,&quot;whats_new_version_digest&quot;:&quot;566afbb607a8f17b7cdf2d7f1632a2a810c06b128e8b81b6c6a8780eb9955dd1&quot;,&quot;is_logged_in&quot;:false,&quot;context_switcher_links&quot;:[{&quot;title&quot;:&quot;Explore&quot;,&quot;link&quot;:&quot;/explore&quot;,&quot;icon&quot;:&quot;compass&quot;}],&quot;current_menu_items&quot;:[{&quot;id&quot;:&quot;project_overview&quot;,&quot;title&quot;:&quot;ska-ost-array-config&quot;,&quot;entity_id&quot;:46018736,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config&quot;,&quot;link_classes&quot;:&quot;shortcuts-project&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;manage_menu&quot;,&quot;title&quot;:&quot;Manage&quot;,&quot;icon&quot;:&quot;users&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/activity&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;activity&quot;,&quot;title&quot;:&quot;Activity&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/activity&quot;,&quot;link_classes&quot;:&quot;shortcuts-project-activity&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;members&quot;,&quot;title&quot;:&quot;Members&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/project_members&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;labels&quot;,&quot;title&quot;:&quot;Labels&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/labels&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;plan_menu&quot;,&quot;title&quot;:&quot;Plan&quot;,&quot;icon&quot;:&quot;planning&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/issues&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;project_issue_list&quot;,&quot;title&quot;:&quot;Issues&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/issues&quot;,&quot;link_classes&quot;:&quot;shortcuts-issues has-sub-items&quot;,&quot;pill_count_field&quot;:&quot;openIssuesCount&quot;,&quot;pill_count_dynamic&quot;:false,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;boards&quot;,&quot;title&quot;:&quot;Issue boards&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/boards&quot;,&quot;link_classes&quot;:&quot;shortcuts-issue-boards&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;milestones&quot;,&quot;title&quot;:&quot;Milestones&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/milestones&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;iterations&quot;,&quot;title&quot;:&quot;Iterations&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/cadences&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_wiki&quot;,&quot;title&quot;:&quot;Wiki&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/wikis/home&quot;,&quot;link_classes&quot;:&quot;shortcuts-wiki&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;requirements&quot;,&quot;title&quot;:&quot;Requirements&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/requirements_management/requirements&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;external_issue_tracker&quot;,&quot;title&quot;:&quot;Jira&quot;,&quot;link&quot;:&quot;https://jira.skatelescope.org?atlOrigin=eyJpIjoiY2QyZTJiZDRkNGZhNGZlMWI3NzRkNTBmZmVlNzNiZTkiLCJwIjoianN3LWdpdGxhYi1pbnQifQ&quot;,&quot;link_classes&quot;:&quot;shortcuts-external_tracker&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;code_menu&quot;,&quot;title&quot;:&quot;Code&quot;,&quot;icon&quot;:&quot;code&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/merge_requests&quot;,&quot;is_active&quot;:true,&quot;items&quot;:[{&quot;id&quot;:&quot;project_merge_request_list&quot;,&quot;title&quot;:&quot;Merge requests&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/merge_requests&quot;,&quot;link_classes&quot;:&quot;shortcuts-merge_requests&quot;,&quot;pill_count_field&quot;:&quot;openMergeRequestsCount&quot;,&quot;pill_count_dynamic&quot;:false,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;files&quot;,&quot;title&quot;:&quot;Repository&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/tree/master&quot;,&quot;link_classes&quot;:&quot;shortcuts-tree&quot;,&quot;is_active&quot;:true},{&quot;id&quot;:&quot;branches&quot;,&quot;title&quot;:&quot;Branches&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/branches&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;commits&quot;,&quot;title&quot;:&quot;Commits&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/commits/master?ref_type=heads&quot;,&quot;link_classes&quot;:&quot;shortcuts-commits&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;tags&quot;,&quot;title&quot;:&quot;Tags&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/tags&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;graphs&quot;,&quot;title&quot;:&quot;Repository graph&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/network/master?ref_type=heads&quot;,&quot;link_classes&quot;:&quot;shortcuts-network&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;compare&quot;,&quot;title&quot;:&quot;Compare revisions&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/compare?from=master\u0026to=master&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_snippets&quot;,&quot;title&quot;:&quot;Snippets&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/snippets&quot;,&quot;link_classes&quot;:&quot;shortcuts-snippets&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;file_locks&quot;,&quot;title&quot;:&quot;Locked files&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/path_locks&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;build_menu&quot;,&quot;title&quot;:&quot;Build&quot;,&quot;icon&quot;:&quot;rocket&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/pipelines&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;pipelines&quot;,&quot;title&quot;:&quot;Pipelines&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/pipelines&quot;,&quot;link_classes&quot;:&quot;shortcuts-pipelines&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;jobs&quot;,&quot;title&quot;:&quot;Jobs&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/jobs&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;pipeline_schedules&quot;,&quot;title&quot;:&quot;Pipeline schedules&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/pipeline_schedules&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;test_cases&quot;,&quot;title&quot;:&quot;Test cases&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/quality/test_cases&quot;,&quot;link_classes&quot;:&quot;shortcuts-test-cases&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;artifacts&quot;,&quot;title&quot;:&quot;Artifacts&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/artifacts&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;deploy_menu&quot;,&quot;title&quot;:&quot;Deploy&quot;,&quot;icon&quot;:&quot;deployments&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/releases&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;releases&quot;,&quot;title&quot;:&quot;Releases&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/releases&quot;,&quot;link_classes&quot;:&quot;shortcuts-deployments-releases&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;packages_registry&quot;,&quot;title&quot;:&quot;Package registry&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/packages&quot;,&quot;link_classes&quot;:&quot;shortcuts-container-registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;container_registry&quot;,&quot;title&quot;:&quot;Container registry&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/container_registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_registry&quot;,&quot;title&quot;:&quot;Model registry&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/ml/models&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;operations_menu&quot;,&quot;title&quot;:&quot;Operate&quot;,&quot;icon&quot;:&quot;cloud-pod&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/environments&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;environments&quot;,&quot;title&quot;:&quot;Environments&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/environments&quot;,&quot;link_classes&quot;:&quot;shortcuts-environments&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;infrastructure_registry&quot;,&quot;title&quot;:&quot;Terraform modules&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/terraform_module_registry&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;monitor_menu&quot;,&quot;title&quot;:&quot;Monitor&quot;,&quot;icon&quot;:&quot;monitor&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/incidents&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;incidents&quot;,&quot;title&quot;:&quot;Incidents&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/incidents&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;service_desk&quot;,&quot;title&quot;:&quot;Service Desk&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/issues/service_desk&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;analyze_menu&quot;,&quot;title&quot;:&quot;Analyze&quot;,&quot;icon&quot;:&quot;chart&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/value_stream_analytics&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;cycle_analytics&quot;,&quot;title&quot;:&quot;Value stream analytics&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/value_stream_analytics&quot;,&quot;link_classes&quot;:&quot;shortcuts-project-cycle-analytics&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;contributors&quot;,&quot;title&quot;:&quot;Contributor analytics&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/graphs/master?ref_type=heads&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;ci_cd_analytics&quot;,&quot;title&quot;:&quot;CI/CD analytics&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/pipelines/charts&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;repository_analytics&quot;,&quot;title&quot;:&quot;Repository analytics&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/graphs/master/charts&quot;,&quot;link_classes&quot;:&quot;shortcuts-repository-charts&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;code_review&quot;,&quot;title&quot;:&quot;Code review analytics&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/analytics/code_reviews&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;issues&quot;,&quot;title&quot;:&quot;Issue analytics&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/analytics/issues_analytics&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;insights&quot;,&quot;title&quot;:&quot;Insights&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/insights/&quot;,&quot;link_classes&quot;:&quot;shortcuts-project-insights&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_experiments&quot;,&quot;title&quot;:&quot;Model experiments&quot;,&quot;link&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/ml/experiments&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false}],&quot;current_context_header&quot;:&quot;Project&quot;,&quot;support_path&quot;:&quot;https://about.gitlab.com/get-help/&quot;,&quot;docs_path&quot;:&quot;/help/docs&quot;,&quot;display_whats_new&quot;:true,&quot;show_version_check&quot;:null,&quot;search&quot;:{&quot;search_path&quot;:&quot;/search&quot;,&quot;issues_path&quot;:&quot;/dashboard/issues&quot;,&quot;mr_path&quot;:&quot;/dashboard/merge_requests&quot;,&quot;autocomplete_path&quot;:&quot;/search/autocomplete&quot;,&quot;settings_path&quot;:&quot;/search/settings&quot;,&quot;search_context&quot;:{&quot;group&quot;:{&quot;id&quot;:55066354,&quot;name&quot;:&quot;Observatory Support Tools&quot;,&quot;full_name&quot;:&quot;SKAO / Observatory Support Tools&quot;},&quot;group_metadata&quot;:{&quot;issues_path&quot;:&quot;/groups/ska-telescope/ost/-/issues&quot;,&quot;mr_path&quot;:&quot;/groups/ska-telescope/ost/-/merge_requests&quot;},&quot;project&quot;:{&quot;id&quot;:46018736,&quot;name&quot;:&quot;ska-ost-array-config&quot;},&quot;project_metadata&quot;:{&quot;mr_path&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/merge_requests&quot;,&quot;issues_path&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/issues&quot;},&quot;code_search&quot;:true,&quot;ref&quot;:&quot;master&quot;,&quot;scope&quot;:null,&quot;for_snippets&quot;:null}},&quot;panel_type&quot;:&quot;project&quot;,&quot;shortcut_links&quot;:[{&quot;title&quot;:&quot;Snippets&quot;,&quot;href&quot;:&quot;/explore/snippets&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-snippets&quot;},{&quot;title&quot;:&quot;Groups&quot;,&quot;href&quot;:&quot;/explore/groups&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-groups&quot;},{&quot;title&quot;:&quot;Projects&quot;,&quot;href&quot;:&quot;/explore/projects/starred&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-projects&quot;}],&quot;terms&quot;:&quot;/-/users/terms&quot;}"></aside>


<div class="content-wrapper">
<div class="broadcast-wrapper">



</div>
<div class="alert-wrapper alert-wrapper-top-space gl-flex gl-flex-col gl-gap-3 container-fluid container-limited">































</div>
<div class="top-bar-fixed container-fluid" data-testid="top-bar">
<div class="top-bar-container gl-flex gl-items-center gl-gap-2">
<div class="gl-grow gl-basis-0 gl-flex gl-items-center gl-justify-start gl-gap-3">
<button class="gl-button btn btn-icon btn-md btn-default btn-default-tertiary js-super-sidebar-toggle-expand super-sidebar-toggle -gl-ml-3" aria-controls="super-sidebar" aria-expanded="false" aria-label="Primary navigation sidebar" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="sidebar-icon"><use href="/assets/icons-1dc8580f14b5de4dcf11c6c7326e55d1b3fb7c05afa8655c3f51c47ac154a434.svg#sidebar"></use></svg>

</button>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"SKAO","item":"https://gitlab.com/ska-telescope"},{"@type":"ListItem","position":2,"name":"Observatory Support Tools","item":"https://gitlab.com/ska-telescope/ost"},{"@type":"ListItem","position":3,"name":"ska-ost-array-config","item":"https://gitlab.com/ska-telescope/ost/ska-ost-array-config"},{"@type":"ListItem","position":4,"name":"Repository","item":"https://gitlab.com/ska-telescope/ost/ska-ost-array-config/-/blob/master/src/ska_ost_array_config/array_assembly.py"}]}


</script>
<div data-testid="breadcrumb-links" id="js-vue-page-breadcrumbs-wrapper">
<div data-breadcrumbs-json="[{&quot;text&quot;:&quot;SKAO&quot;,&quot;href&quot;:&quot;/ska-telescope&quot;,&quot;avatarPath&quot;:&quot;/uploads/-/system/group/avatar/3180705/skao_logo_2021_colour_rgb-ai__1_.png&quot;},{&quot;text&quot;:&quot;Observatory Support Tools&quot;,&quot;href&quot;:&quot;/ska-telescope/ost&quot;,&quot;avatarPath&quot;:null},{&quot;text&quot;:&quot;ska-ost-array-config&quot;,&quot;href&quot;:&quot;/ska-telescope/ost/ska-ost-array-config&quot;,&quot;avatarPath&quot;:null},{&quot;text&quot;:&quot;Repository&quot;,&quot;href&quot;:&quot;/ska-telescope/ost/ska-ost-array-config/-/blob/master/src/ska_ost_array_config/array_assembly.py&quot;,&quot;avatarPath&quot;:null}]" id="js-vue-page-breadcrumbs"></div>
<div id="js-injected-page-breadcrumbs"></div>
</div>


</div>
<div class="gl-flex-none gl-flex gl-items-center gl-justify-center gl-gap-3">
<div id="js-work-item-feedback"></div>

<div id="js-advanced-search-modal"></div>


</div>
</div>
</div>

<div class="container-fluid container-limited project-highlight-puc">
<main class="content" id="content-body" itemscope itemtype="http://schema.org/SoftwareSourceCode">
<div class="flash-container flash-container-page sticky" data-testid="flash-container">
<div id="js-global-alerts"></div>
</div>






<div class="js-signature-container" data-signatures-path="/ska-telescope/ost/ska-ost-array-config/-/commits/8ee718cb2d0c574d4d01a2e201360c1c14c8f9e2/signatures?limit=1"></div>

<div class="tree-holder gl-pt-4" id="tree-holder">
<div data-blob-path="src/ska_ost_array_config/array_assembly.py" data-breadcrumbs-can-collaborate="false" data-breadcrumbs-can-edit-tree="false" data-breadcrumbs-can-push-code="false" data-breadcrumbs-can-push-to-branch="false" data-breadcrumbs-new-blob-path="/ska-telescope/ost/ska-ost-array-config/-/new/master" data-breadcrumbs-new-branch-path="/ska-telescope/ost/ska-ost-array-config/-/branches/new" data-breadcrumbs-new-dir-path="/ska-telescope/ost/ska-ost-array-config/-/create_dir/master" data-breadcrumbs-new-tag-path="/ska-telescope/ost/ska-ost-array-config/-/tags/new" data-breadcrumbs-upload-path="/ska-telescope/ost/ska-ost-array-config/-/create/master" data-escaped-ref="master" data-history-link="/ska-telescope/ost/ska-ost-array-config/-/commits/master" data-new-workspace-path="/-/remote_development/workspaces/new" data-project-id="46018736" data-project-path="ska-telescope/ost/ska-ost-array-config" data-project-root-path="/ska-telescope/ost/ska-ost-array-config" data-project-short-path="ska-ost-array-config" data-ref="master" data-ref-type="" data-root-ref="master" id="js-repository-blob-header-app"></div>
<div class="info-well">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-8ee718cb">
<div class="gl-self-start gl-block">
<a href="/sarrvesh.ss"><img alt="Sarrvesh Sridhar&#39;s avatar" src="https://secure.gravatar.com/avatar/30436fbb21f09ced4c8aa643dab51bea53448ce734ffc6076758c2c495e9992a?s=128&amp;d=identicon" class="avatar s32 gl-inline-block" title="Sarrvesh Sridhar"></a>
</div>
<div class="commit-detail flex-list gl-flex gl-justify-between gl-items-start gl-grow gl-min-w-0">
<div class="commit-content gl-self-center" data-testid="commit-content">
<div class="gl-flex sm:gl-hidden gl-gap-3 gl-items-center">
<div class="committer gl-text-sm">
<time class="js-timeago" title="May 1, 2025 3:59pm" datetime="2025-05-01T15:59:38Z" tabindex="0" aria-label="May 1, 2025 3:59pm" data-toggle="tooltip" data-placement="bottom" data-container="body">May 01, 2025</time>
</div>
<a class="gl-button btn btn-md btn-link commit-row-message js-onboarding-commit-item" href="/ska-telescope/ost/ska-ost-array-config/-/commit/8ee718cb2d0c574d4d01a2e201360c1c14c8f9e2"><svg class="s16 gl-icon gl-button-icon " data-testid="commit-icon"><use href="/assets/icons-1dc8580f14b5de4dcf11c6c7326e55d1b3fb7c05afa8655c3f51c47ac154a434.svg#commit"></use></svg>
<span class="gl-button-text">
8ee718cb

</span>

</a></div>
<div class="gl-hidden sm:gl-block">
<a href="https://jira.skatelescope.org/browse/OPS-286?atlOrigin=eyJpIjoiY2QyZTJiZDRkNGZhNGZlMWI3NzRkNTBmZmVlNzNiZTkiLCJwIjoianN3LWdpdGxhYi1pbnQifQ" data-reference-type="external_issue" data-project="46018736" data-external-issue="OPS-286" data-container="body" data-placement="top" title="Issue in Jira issues" class="gfm gfm-issue has-tooltip commit-row-message item-title js-onboarding-commit-item">OPS-286</a><a class="commit-row-message item-title js-onboarding-commit-item " href="/ska-telescope/ost/ska-ost-array-config/-/commit/8ee718cb2d0c574d4d01a2e201360c1c14c8f9e2"> fix typo</a>
<span class="commit-row-message d-inline d-sm-none">
&middot;
8ee718cb
</span>
<div class="committer gl-text-sm">
<a class="commit-author-link js-user-link" data-user-id="1979754" href="/sarrvesh.ss">Sarrvesh Sridhar</a> authored <time class="js-timeago" title="May 1, 2025 3:59pm" datetime="2025-05-01T15:59:38Z" tabindex="0" aria-label="May 1, 2025 3:59pm" data-toggle="tooltip" data-placement="bottom" data-container="body">May 01, 2025</time>
</div>


</div>
</div>
<div class="commit-actions gl-flex gl-items-center gl-gap-3">
<div class="gl-hidden sm:gl-flex gl-items-center gl-gap-3">

<div class="js-commit-pipeline-status" data-endpoint="/ska-telescope/ost/ska-ost-array-config/-/commit/8ee718cb2d0c574d4d01a2e201360c1c14c8f9e2/pipelines?ref=master"></div>
<div class="btn-group gl-hidden sm:gl-flex">
<span class="gl-button btn btn-label btn-md btn-default dark:!gl-bg-neutral-800" type="button"><span class="gl-button-text gl-font-monospace">
8ee718cb

</span>

</span><button class="gl-button btn btn-icon btn-md btn-default " title="Copy commit SHA" aria-label="Copy commit SHA" aria-live="polite" data-toggle="tooltip" data-placement="bottom" data-container="body" data-html="true" data-category="primary" data-size="medium" data-clipboard-text="8ee718cb2d0c574d4d01a2e201360c1c14c8f9e2" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="copy-to-clipboard-icon"><use href="/assets/icons-1dc8580f14b5de4dcf11c6c7326e55d1b3fb7c05afa8655c3f51c47ac154a434.svg#copy-to-clipboard"></use></svg>

</button>

</div>
</div>
<div class="gl-block sm:gl-hidden">
<button class="gl-button btn btn-icon btn-md btn-default button-ellipsis-horizontal text-expander js-toggle-button" data-toggle="tooltip" data-container="body" data-collapse-title="Toggle commit description" data-expand-title="Toggle commit description" title="Toggle commit description" aria-label="Toggle commit description" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="ellipsis_h-icon"><use href="/assets/icons-1dc8580f14b5de4dcf11c6c7326e55d1b3fb7c05afa8655c3f51c47ac154a434.svg#ellipsis_h"></use></svg>

</button>
</div>
<div data-event-tracking="click_history_control_on_blob_page" data-history-link="/ska-telescope/ost/ska-ost-array-config/-/commits/master/src/ska_ost_array_config/array_assembly.py" id="js-commit-history-link"></div>
</div>
</div>
<div class="gl-block sm:gl-hidden">
<div class="gl-hidden js-toggle-content gl-mt-6">
<a href="https://jira.skatelescope.org/browse/OPS-286?atlOrigin=eyJpIjoiY2QyZTJiZDRkNGZhNGZlMWI3NzRkNTBmZmVlNzNiZTkiLCJwIjoianN3LWdpdGxhYi1pbnQifQ" data-reference-type="external_issue" data-project="46018736" data-external-issue="OPS-286" data-container="body" data-placement="top" title="Issue in Jira issues" class="gfm gfm-issue has-tooltip commit-row-message item-title js-onboarding-commit-item">OPS-286</a><a class="commit-row-message item-title js-onboarding-commit-item " href="/ska-telescope/ost/ska-ost-array-config/-/commit/8ee718cb2d0c574d4d01a2e201360c1c14c8f9e2"> fix typo</a>
<div class="committer gl-text-sm">
<a class="commit-author-link js-user-link" data-user-id="1979754" href="/sarrvesh.ss">Sarrvesh Sridhar</a> authored <time class="js-timeago" title="May 1, 2025 3:59pm" datetime="2025-05-01T15:59:38Z" tabindex="0" aria-label="May 1, 2025 3:59pm" data-toggle="tooltip" data-placement="bottom" data-container="body">May 01, 2025</time>
</div>

</div>
</div>
</li>

</ul>
</div>
<div class="gl-hidden sm:gl-block">
<div data-blob-path="src/ska_ost_array_config/array_assembly.py" data-branch="master" data-branch-rules-path="/ska-telescope/ost/ska-ost-array-config/-/settings/repository#js-branch-rules" data-project-path="ska-telescope/ost/ska-ost-array-config" id="js-code-owners"></div>

</div>
</div>
<div class="blob-content-holder js-per-page" data-blame-per-page="1000" id="blob-content-holder">
<div data-blob-path="src/ska_ost_array_config/array_assembly.py" data-can-download-code="true" data-duo-workflow-invoke-path="/api/v4/ai/duo_workflows/workflows" data-explain-code-available="false" data-new-workspace-path="/-/remote_development/workspaces/new" data-original-branch="master" data-project-path="ska-telescope/ost/ska-ost-array-config" data-ref-type="" data-resource-id="gid://gitlab/Project/46018736" data-show-duo-workflow-action="false" data-user-id="" id="js-view-blob-app">
<div class="gl-spinner-container" role="status"><span aria-hidden class="gl-spinner gl-spinner-md gl-spinner-dark !gl-align-text-bottom"></span><span class="gl-sr-only !gl-absolute">Loading</span>
</div>
</div>
</div>

</div>
<script nonce="CQaS6OefbNR/UGnCo9kvFg==">
//<![CDATA[
  window.gl = window.gl || {};
  window.gl.webIDEPath = '/-/ide/project/ska-telescope/ost/ska-ost-array-config/edit/master/-/src/ska_ost_array_config/array_assembly.py'


//]]>
</script>
<div data-ambiguous="false" data-ref="master" id="js-ambiguous-ref-modal"></div>

</main>
</div>


</div>
</div>


<script nonce="CQaS6OefbNR/UGnCo9kvFg==">
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded');
    img.dataset.testid = 'js-lazy-loaded-content';
  });
}

//]]>
</script>
<script nonce="CQaS6OefbNR/UGnCo9kvFg==">
//<![CDATA[
gl = window.gl || {};
gl.experiments = {};


//]]>
</script>

</body>
</html>

