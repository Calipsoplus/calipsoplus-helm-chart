export const environment = {
  production: false,
  servers: {
    api: {
      url: '/',
      basehref: 'services/'
    },
    guacamole: {
      integrated_remote_desktop_viewer : {
        enabled : false, // if true, the guacamole.url will be ignored as it isn't needed
        security: false,
        ignore_cert: true,
        disable_auth: true,
        cluster_url : 'cluster.local', // the server or cluster which contains all of the docker/kubernetes containers
        websocket_server : 'ws://java-server.cluster.local:8080/ws'
      },
      url: '/guac'
    },
    jupyterhub: {
      enabled: {{ .Values.jupyterhub.enabled }},
      url: {{ .Values.jupyterhub.url | quote }}
    }
  },
  auth: {
    oidc: {
      enabled: true,
      url: 'services/oidc/authenticate'
    },
    useroffice: {
      enabled: {{ .Values.userOffice.enabled }},
      url: {{ .Values.userOffice.url | quote }}
    }
  },
  frontend: {
    url: '/',
    facilityLogo: 'assets/images/facility-logo.png'
  },
  env: 'kubernetes'
};
